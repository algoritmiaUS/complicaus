s = input().strip()

x = 0
y = 0

for c in s:
    x *= 2
    y *= 2
    n = ord(c) - ord('0')
    if n & 1:
        x += 1
    if n & 2:
        y += 1

print(len(s), x, y)
