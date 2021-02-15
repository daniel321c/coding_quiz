
m = [   [1,0,1],
        [1,1,1],
        [1,0,1]]

move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def validPoint(point, area, visited):
    return point[0]<len(area) and point[0]>-1 and point[1]<len(area[0]) and point[1]>-1 and not visited[point[0]][point[1]]

def moveback(point, direction):
    nextMove = move[(direction+2)%4]
    tmp_point = moveNext(point, nextMove)
    point[0] = tmp_point[0]
    point[1] = tmp_point[1]
    
def moveNext(point, nextMove):
    nextPoint = [point[0]+nextMove[0], point[1]+nextMove[1]]
    return nextPoint

def startClean(area, point, direction, visited):

    nextMove = move[direction%4]
    nextPoint = moveNext(point, nextMove)
    # print(visited)
    print("attempt: ", nextPoint)
    if(validPoint(nextPoint, area, visited)):
        point[0] = nextPoint[0]
        point[1] = nextPoint[1]
        print("Move Next: ", point)
        visited[point[0]][point[1]] = True
        for nextDir in range(4):
            startClean(area, point, nextDir, visited)
    
        # print("current: ", point, " direction: ", direction)
        moveback(point, direction)
        print("Move back: ", point)

def start(area, point):
    visited = [[True for x in range(len(area[0]))] for y in range(len(area))]

    
    for x in range(len(area)):
        for y in range(len(area[0])):
            if(area[x][y]==1):
                visited[x][y]=False
    
    visited[point[0]][point[1]] = True

    # print(visited)
    for nextDir in range(4):
        startClean(area, point, nextDir, visited)
start(m, [0, 2])
json_s = '[{"x":"love", "y":"hehe"}, {"x":"lve", "y":"hee"}]'