n = int(input())
b = list(map(int, input().split()))

min_b = min(b)
max_b = max(b)
diff = max_b - min_b

if diff == 0:
    ways = n * (n - 1) // 2
else:
    cnt_min = b.count(min_b)
    cnt_max = b.count(max_b)
    ways = cnt_min * cnt_max

print(diff, ways)
