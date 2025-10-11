n = int(input())
cont = 0
for _ in range(n):
    team = list(map(int, input().split()))
    if sum(team) >= 2:
        cont += 1

print(cont)