import heapq

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))

dist = [float("inf")] * (n + 1)
dist[1] = 0

pq = [(0, 1)]  # (distance, node)
while pq:
    d, u = heapq.heappop(pq)
    if d != dist[u]:
        continue
    for v, w in adj[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

print(' '.join(str(dist[i]) for i in range(1, n + 1)))
