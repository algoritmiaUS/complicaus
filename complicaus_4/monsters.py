from collections import deque

n, m = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(n)]

DIRS = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]

INF = float("inf")
mon_time = [[INF]*m for _ in range(n)]
q = deque()

# Locate monsters and A
sx = sy = None
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'M':
            mon_time[i][j] = 0
            q.append((i, j))
        elif grid[i][j] == 'A':
            sx, sy = i, j

# 1) Multi-source BFS from all monsters to compute earliest monster arrival times
while q:
    x, y = q.popleft()
    t = mon_time[x][y]
    for dx, dy, _ in DIRS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#' and mon_time[nx][ny] == INF:
            mon_time[nx][ny] = t + 1
            q.append((nx, ny))

if sx == 0 or sy == 0 or sx == n-1 or sy == m-1:
    if 0 < mon_time[sx][sy]:
        print("YES")
        print(0)
        print()
        exit()

# 2) BFS for the player ensuring we never step into a cell at time >= monster arrival
parent = [[None]*m for _ in range(n)]
move_ch = [[None]*m for _ in range(n)]
dist = [[INF]*m for _ in range(n)]

dq = deque()
dq.append((sx, sy))
dist[sx][sy] = 0

escaped_end = None

while dq:
    x, y = dq.popleft()
    t = dist[x][y]
    for dx, dy, ch in DIRS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#':
            # We would arrive at time t+1; must be strictly earlier than monsters
            if dist[nx][ny] == INF and t + 1 < mon_time[nx][ny]:
                dist[nx][ny] = t + 1
                parent[nx][ny] = (x, y)
                move_ch[nx][ny] = ch
                dq.append((nx, ny))
                # If boundary reached, we have an escape
                if nx == 0 or ny == 0 or nx == n-1 or ny == m-1:
                    escaped_end = (nx, ny)
                    dq.clear()  # Stop BFS early; path found
                    break

if not escaped_end:
    print("NO")
else:
    # Reconstruct path
    path = []
    x, y = escaped_end
    while (x, y) != (sx, sy):
        ch = move_ch[x][y]
        path.append(ch)
        x, y = parent[x][y]
    path.reverse()
    print("YES")
    print(len(path))
    print(''.join(path))
