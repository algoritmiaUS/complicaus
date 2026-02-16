import sys
sys.setrecursionlimit(10**7)

N, A = map(int, input().split())
M, B = map(int, input().split())

V = [input().strip() for _ in range(A)]
H = [input().strip() for _ in range(B)]


# Trie vertical
children = []
term = []
depth = []

def new_node(d):
    children.append({})
    term.append(False)
    depth.append(d)
    return len(children) - 1

root = new_node(0)

for w in V:
    u = root
    for i, ch in enumerate(w):
        c = ord(ch) - 97
        nxt = children[u].get(c)
        if nxt is None:
            nxt = new_node(depth[u] + 1)
            children[u][c] = nxt
        u = nxt
    term[u] = True

by_depth = [[] for _ in range(N + 1)]
for i in range(len(children)):
    d = depth[i]
    if d <= N:
        by_depth[d].append(i)

# --- Minimización por firma (term, transiciones a clases, profundidad) ---
node_class = [-1] * len(children)
sig_to_class = {}
class_trans = []
class_term = []

# Vamos de profundidad N hacia 0
for d in range(N, -1, -1):
    for u in by_depth[d]:
        items = []
        for c, v in children[u].items():
            if depth[v] <= N:
                items.append((c, node_class[v]))
        items.sort()
        sig = (d, term[u], tuple(items))
        cid = sig_to_class.get(sig)
        if cid is None:
            cid = len(class_trans)
            sig_to_class[sig] = cid
            tr = [-1] * 26
            for c, cv in items:
                tr[c] = cv
            class_trans.append(tr)
            class_term.append(term[u])
        node_class[u] = cid

root_class = node_class[root]

# --- Frecuencias de palabras horizontales ---
freq = {}
row_words = []
for w in H:
    code = 0
    digs = [0] * M
    for i, ch in enumerate(w):
        x = ord(ch) - 97
        digs[i] = x
        code = code * 26 + x
    # si hay repetidas, suman
    if code in freq:
        freq[code][0] += 1
    else:
        freq[code] = [1, digs]

row_words = [(f_d[0], f_d[1]) for f_d in freq.values()]

# --- DP por filas sobre clases de columnas ---
dp = {tuple([root_class] * M): 1}

for r in range(N):
    ndp = {}
    for state, ways in dp.items():
        # Intentar cada palabra horizontal existente
        for f, digs in row_words:
            nxt_state = []
            ok = True
            for j in range(M):
                nc = class_trans[state[j]][digs[j]]
                if nc == -1:
                    ok = False
                    break
                nxt_state.append(nc)

            if not ok:
                continue

            # Si estamos cerrando la última fila, las columnas deben terminar en palabra vertical
            if r == N - 1:
                for nc in nxt_state:
                    if not class_term[nc]:
                        ok = False
                        break
                if not ok:
                    continue

            t = tuple(nxt_state)
            ndp[t] = ndp.get(t, 0) + ways * f

    dp = ndp

ans = sum(dp.values())
print(ans)