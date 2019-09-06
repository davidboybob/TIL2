Alpha = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M':12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'L': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

def DFS(x, y, d):
    global Max
    if Max < d:
        Max = d
    if Max == 26:
        return True
    visit[Alpha[lst[x][y]]] = True

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        tx, ty = x + dx, y + dy
        if tx < 0 or tx == R or ty < 0 or ty == C or visit[Alpha[lst[tx][ty]]]: continue
        if DFS(tx, ty, d + 1): return True
    visit[Alpha[lst[x][y]]] = False
    return False

R, C = 2, 4 #map(int, input().split())
lst = ['CAAB', 'ADCB'] #[input() for _ in range(R)]

visit = [False] * 26

Max = 0
DFS(0, 0, 0)
print(Max + 1)

