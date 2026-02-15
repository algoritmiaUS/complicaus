#!/usr/bin/env python3

(h, w), hpi, oo = map(int, input().split()), __import__("math").pi / 2, 1e18
grid, res = [input() for _ in range(h)], [list(range(2 * w + 1)), *([y + 1, *([0] * (2 * w))] for y in range(2 * h))]
for y in range(1, 2 * h + 1, 2):
    # Odd row. Going direct down from two spaces up, or right-and-down from the space to the left-and-up.
    for x in range(2, 2 * w + 1, 2): res[y][x] = \
        min(res[y - 2][x] + 2 if y > 1 else oo, res[y - 1][x - 1] + (2 if grid[y // 2][x // 2 - 1] == "X" else hpi))
    # Even row. Going direct right from two spaces left, or down-and-right from the space to the left-and-up.
    for x in range(1, 2 * w, 2): res[y + 1][x] = \
        min(res[y + 1][x - 2] + 2 if x > 1 else oo, res[y][x - 1] + (2 if grid[y // 2][x // 2] == "X" else hpi))
print(10 * (min(res[-2][-1], res[-1][-2]) / 2 + .5))
