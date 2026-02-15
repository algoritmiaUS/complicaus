#!/usr/bin/env python3
h, w = map(int, input().split())
b, dp = [input() for _ in range(h)], [[0] * (2 * w + 1) for _ in range(2 * h + 1)]
for i, j in ((i, j) for i in range(1, 2 * h + 1) for j in range(1, 2 * w + 1) if (i + j) % 2):
    dp[i][j] = max(dp[i][j - 2], dp[i - 1][j - 1] + (b[i // 2 - 1][j // 2] == "O")) if i % 2 == 0 \
        else max(dp[i - 2][j], dp[i - 1][j - 1] + (b[i // 2][j // 2 - 1] == "O"))
print(10*((w + h) - (max(dp[-1][-2], dp[-2][-1])) * (1 - __import__("math").pi / 4)))
