n1, n2, n12 = map(int, input().split())
a = (n1 + 1) * (n2 + 1)
b = (n12 + 1)
ans = a // b - 1
print(ans)

