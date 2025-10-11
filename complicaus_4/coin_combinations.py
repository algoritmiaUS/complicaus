MOD = 10**9 + 7

n, x = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()

dp = [0] * (x + 1)
dp[0] = 1

for c in coins:
    for s in range(c, x + 1):
        dp[s] = (dp[s] + dp[s - c]) % MOD

print(dp[x])
