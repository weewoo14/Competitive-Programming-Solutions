from collections import deque
r = int(input())
c = int(input())
grid = [list(input()) for i in range(r)]
sy = int(input())
sx = int(input())
pos = [(0,1),(0,-1),(1,0),(-1,0)]
q = deque([(sy,sx)])
visit = [[False for i in range(c)] for _ in range(r)]
visit[sy][sx] = True
total = 0
def valid(y,x,v):
    if y < 0 or y >= r or x < 0 or x >= c:
        return False
    elif grid[y][x] == '*':
        return False
    elif v[y][x]:
        return False
    return True
while q:
    cy,cx = q.popleft()
    if grid[cy][cx] == 'S':
        total += 1
    elif grid[cy][cx] == 'M':
        total += 5
    else:
        total += 10
    for x,y in pos:
        ny,nx = cy + y,cx + x
        if valid(ny,nx,visit):
            visit[ny][nx] = True
            q.append([ny,nx])
print(total)