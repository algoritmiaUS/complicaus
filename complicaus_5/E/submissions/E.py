n=int(input())
d = {}
for _ in range(n):
    t = input().strip()
    if t in d:
        d[t]+=1
    else:
        d[t]=1
        
winner = "NONE"
for k, v in d.items():
    if v > n - v:
        winner = k
        break
print(winner)