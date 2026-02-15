#!/usr/bin/env python3

import heapq
from math import pi

s = pi / 2

h, w = map(int, input().split())
b = [input() for _ in range(h)]
g = [[1000000.0] * (2 * w + 1) for _ in range(2 * h + 1)]
pq = [(1.0, (0, 1)), (1.0, (1, 0))]
while pq:
    d, (r, c) = heapq.heappop(pq)
    if d > g[r][c]:
        continue
    if r + c == 2 * h + 2 * w - 1:
        print(f"{5*(d+1):.10}")
        break
    if r + 1 <= 2 * h and c + 1 <= 2 * w:
        e = d + (s if b[r // 2][c // 2] == "O" else 2)
        if e < g[r + 1][c + 1]:
            g[r + 1][c + 1] = e
            heapq.heappush(pq, (e, (r + 1, c + 1)))
    if r % 2 == 1:
        if r + 2 <= 2 * h:
            if d + 2 < g[r + 2][c]:
                g[r + 2][c] = d + 2
                heapq.heappush(pq, (d + 2, (r + 2, c)))
    else:
        if c + 2 <= 2 * w:
            if d + 2 < g[r][c + 2]:
                g[r][c + 2] = d + 2
                heapq.heappush(pq, (d + 2, (r, c + 2)))
