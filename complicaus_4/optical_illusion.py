import math

n, r = map(float, input().split())
s = math.sin(math.pi / n)
R = (r * s) / (1 - s)
print(f"{R:.10f}")