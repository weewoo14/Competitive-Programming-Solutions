need = list(input())
n = len(need)-1
counter = 0
r = int(input())
c = int(input())
grid = [list(input().split()) for i in range(r)]
adj8 = {(0,1):'right',(0,-1):'left',(1,0):'up',(-1,0):'down',(1,1):'downright',(1,-1):'downleft',(-1,1):'upright',(-1,-1):'upleft'}
cmds = {'any':set(['right','left','up','down','upright','downright','downleft','upleft']),'right':set(['up','down','right']),'left':set(['up','down','left']),
        'up':set(['left','right','up']),'down':set(['left','right','down']),'upright':set(['upleft','upright','downright']),
        'upleft':set(['upright','upleft','downleft']),'downleft':set(['upleft','downleft','downright']),'downright':set(['downright','downleft','upright'])}
def findword(i,j,idx,cmd,alr90):
    global n
    global counter
    if idx == n:
        counter += 1
    else:
        for x,y in adj8.keys():
            nx,ny = i+x,j+y
            if nx >= 0 and nx <= r-1 and ny >= 0 and ny <= c-1:
                if grid[nx][ny] == need[idx+1]:
                    if cmd == 'any':
                        findword(nx,ny,idx+1,adj8[tuple([x,y])],False)
                    else:
                        if adj8[tuple([x,y])] == cmd:
                            findword(nx,ny,idx+1,cmd,alr90)
                        elif adj8[tuple([x,y])] in cmds[cmd]:
                            if not alr90:
                                findword(nx,ny,idx+1,adj8[tuple([x,y])],True)
for i in range(r):
    for j in range(c):
        if grid[i][j] == need[0]:
            findword(i,j,0,'any',False)
print(counter)