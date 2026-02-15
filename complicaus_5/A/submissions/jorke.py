#!/usr/bin/env python3
import math
h,w = [int(i) for i in input().split()]
grid = [input() for i in range(h)]
a = [.5,.5]
for i in range(h+w-1):
    b = [h+w]*(2*i+4)
    b[:-2:2] = [c+1 for c in a[::2]]
    b[3::2] = [c+1 for c in a[1::2]]
    for x in range(w):
        y = i-x
        if y in range(h):
            if grid[y][x] == 'X':
                b[2*x+1] = min(b[2*x+1],a[2*x]  +1)
                b[2*x+2] = min(b[2*x+2],a[2*x+1]+1)
            else:
                b[2*x+1] = min(b[2*x+1],a[2*x]  +math.pi/4)
                b[2*x+2] = min(b[2*x+2],a[2*x+1]+math.pi/4)
    a = b
print(10*(min(b)+.5))
