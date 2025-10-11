_ = int(input())
num = list(map(int, input().split()))

num.sort()

for i, n in enumerate(num, start=1):
    if i != n:
        print(i)
        break
else:
    print(len(num) + 1)
