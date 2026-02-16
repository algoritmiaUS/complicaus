from fractions import Fraction

def leer_numeros(k: int):
    parts = input().strip().split()
    return list(map(int, parts))

t = int(input())
for _ in range(t):
    k = int(input())
    nums = leer_numeros(k)
    full = (1 << k) - 1

    memo = {}  # (mask, Fraction) -> frozenset(int)

    def dfs(mask: int, acc: Fraction):
        key = (mask, acc)
        if key in memo:
            return memo[key]

        if mask == full:
            if acc.denominator == 1 and acc.numerator > 0:
                memo[key] = frozenset([int(acc)])
            else:
                memo[key] = frozenset()
            return memo[key]

        res = set()

        # Evita repetir ramas si hay valores repetidos disponibles
        seen_vals = set()
        for i in range(k):
            bit = 1 << i
            if mask & bit:
                continue
            x = nums[i]
            if x in seen_vals:
                continue
            seen_vals.add(x)

            fx = Fraction(x, 1)

            res |= dfs(mask | bit, acc + fx)
            res |= dfs(mask | bit, acc - fx)
            res |= dfs(mask | bit, acc * fx)
            if x != 0:
                res |= dfs(mask | bit, acc / fx)

        memo[key] = frozenset(res)
        return memo[key]

    ans = set()

    # Elegir el primer número (sin operación previa)
    seen_start = set()
    for i in range(k):
        x = nums[i]
        if x in seen_start:
            continue
        seen_start.add(x)
        ans |= set(dfs(1 << i, Fraction(x, 1)))

    print(len(ans))

