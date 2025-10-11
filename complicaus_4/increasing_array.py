n = int(input().strip())
a = list(map(int, input().split()))

moves = 0
prev = a[0]

for x in a[1:]:
    if x < prev:
        moves += prev - x
    else:
        prev = x

print(moves)