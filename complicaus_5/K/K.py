from collections import defaultdict
T = int(input())
for _ in range(T):
    n = int(input())
    d = defaultdict(lambda: -1)
    for _ in range(n):
        a,c = [int(x) for x in input().split(" ")]
        d[a] = max(d[a], c)
    
    q = int(input())
    for _ in range(q):
        x,k = [int(y) for y in input().split(" ")]
        if d[x]>= k:
            print("SI")
        else:
            print("NO")