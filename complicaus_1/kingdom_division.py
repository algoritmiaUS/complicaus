import sys
import os
from collections import defaultdict

MOD = 10**9 + 7

def kingdomDivision(n, roads):

    # Primero me construyo la lista de adyacencias

    adj = defaultdict(list)
    for u, v in roads:
        adj[u].append(v)
        adj[v].append(u)

    dp0 = [0] * (n+1) # numero de formas si tiene el mismo color que su padre
    dp1 = [0] * (n+1) # numero de formas si tiene color distinto de su padre
    
    def dfs(u, parent):
        prod_all = 1
        prod_diff_only = 1

        for v in adj[u]:
            if v == parent:
                continue
            dfs(v, u)

            a, b = dp0[v], dp1[v]

            prod_all = (prod_all * (a + b)) % MOD 
            prod_diff_only = (prod_diff_only * b) % MOD # las que tengo que restar son
                # las que son un color distindo al padre, que son los casos que no queremos que se den
        dp0[u] = prod_all
        dp1[u] = (prod_all - prod_diff_only + MOD) % MOD

    
    dfs(1, 0)  #recorremos en profundidad calculando eso empezando en el vertice 1

    # Como la solucion la he calculado asumiendo que la raiz es de un color en concreto,
    # la tengo que devolver multiplicada por dos, porque todas esas soluciones son igual
    # de válidas para exactamente los mismos colores pero a la inversa
    return (2 * dp1[1]) % MOD



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(sys.stdin.readline().strip())
    roads = [list(map(int, sys.stdin.readline().split())) for _ in range(n - 1)]

    result = kingdomDivision(n, roads)
    fptr.write(str(result) + '\n')
    fptr.close()


    '''
    # ENTRADA SALIDA MANUAL
    n = int(input().strip())
    carreteras = []
    for _ in range(n-1):
        carretera = list(map(int, input().split()))
        carreteras.append(carretera)
    print(kingdomDivision(n, carreteras))
    '''
            
