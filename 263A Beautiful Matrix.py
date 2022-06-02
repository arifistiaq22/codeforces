matrix = (list(map(int, input().split())),list(map(int, input().split())),list(map(int, input().split())),list(map(int, input().split())),list(map(int, input().split())))
for x in range(5):
    for y in range(5):
        if matrix[x][y] == 1:
            row = x+1
            col = y+1
print(abs(3-row)+abs(3-col))
