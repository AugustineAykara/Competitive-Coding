def manhattanDistance(a, b, x, y):
    return(abs(x-a) + abs(y-b))


def distanceFromWarShip(island, a, b):
    x1, y1, x2, y2 = island['x1'], island['y1'], island['x2'], island['y2']

    # eq to find coordinates of opposite vertices of a square
    x3, y3 = ((x1 + x2) + (y1 - y2)) / 2, ((y1 + y2) - (x1 - x2)) / 2
    x4, y4 = ((x1 + x2) - (y1 - y2)) / 2, ((y1 + y2) + (x1 - x2)) / 2

    distance = min(manhattanDistance(a, b, x1, y1), manhattanDistance(a, b, x2, y2), manhattanDistance(a, b, x3, y3), manhattanDistance(a, b, x4, y4))
    return(distance)


n = int(input())
islands = []

for islandCoordinates in range(n):
    x1, y1, x2, y2 = list(map(int, input().split()))
    dictionary = {
        'x1' : x1,
        'y1' : y1,
        'x2' : x2,
        'y2' : y2,
        'index' : islandCoordinates+1
    }
    islands.append(dictionary)

a, b = list(map(int, input().split()))
islands.sort(key = lambda x : distanceFromWarShip(x, a, b))

for island in islands:
    print(island['index'], end=' ')
