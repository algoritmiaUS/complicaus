import sys
import math
import random
from collections import Counter

# Miller-Rabin
def is_probable_prime(n: int) -> bool:
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17]
    for p in small_primes:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d & 1 == 0:
        d >>= 1
        s += 1
    for a in small_primes:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

# Pollard-Rho factorization
def _rho_f(x, c, mod):
    return (x * x + c) % mod

def pollard_rho(n: int) -> int:
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    while True:
        x = random.randrange(2, n - 1)
        y = x
        c = random.randrange(1, n - 1)
        d = 1
        while d == 1:
            x = _rho_f(x, c, n)
            y = _rho_f(_rho_f(y, c, n), c, n)
            d = math.gcd(abs(x - y), n)
        if d != n:
            return d

def factor(n: int, out: dict):
    if n == 1:
        return
    if is_probable_prime(n):
        out[n] = out.get(n, 0) + 1
        return
    d = pollard_rho(n)
    factor(d, out)
    factor(n // d, out)

def all_divisors_from_factors(pf: dict) -> list:
    divs = [1]
    for p, e in pf.items():
        mults = []
        cur = 1
        for _ in range(e):
            cur *= p
            for v in divs:
                mults.append(v * cur)
        divs += mults
    return divs


n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(a[0])

half = (n + 1) // 2
ans = 1
g = math.gcd

cnt = Counter(a)
uniq_vals = list(cnt.items())

K = min(n, 10)
rng = random.SystemRandom()
idxs = {0, n // 2, n - 1}
while len(idxs) < K:
    idxs.add(rng.randrange(0, n))
samples = [a[i] for i in idxs]

for x in samples:
    if x <= ans:
        continue

    pf = {}
    factor(x, pf)
    divs = all_divisors_from_factors(pf)
    divs.sort()
    D = len(divs)
    idx_of = {v: i for i, v in enumerate(divs)}

    freq = [0] * D
    xi = x
    for v, c in uniq_vals:
        gi = g(v, xi)
        freq[idx_of[gi]] += c

    support = freq[:]
    for p in pf.keys():
        for i in range(D - 1, 0, -1):
            si = support[i]
            if si == 0:
                continue
            vi = divs[i]
            if vi % p == 0:
                support[idx_of[vi // p]] += si

    for i in range(D - 1, -1, -1):
        if support[i] >= half and divs[i] > ans:
            ans = divs[i]
            break

print(ans)