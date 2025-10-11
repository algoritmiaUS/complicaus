_, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def can_make(x):
    need = 0
    for ai, bi in zip(a, b):
        req = ai * x - bi
        if req > 0:
            need += req
            if need > k: 
                return False
    return need <= k

lo, hi = 0, 10**12 
while lo < hi:
    mid = (lo + hi + 1) // 2
    if can_make(mid):
        lo = mid
    else:
        hi = mid - 1

print(lo)

