def addEdge(u, v):
    adj[u].append(v)
    adj[v].append(u)

def DFS(v, visited):
    visited[v] = True

    i = 0
    while i != len(adj[v]):
        if (not visited[adj[v][i]]):
            DFS(adj[v][i], visited)
        i += 1

def isConnected():
    visited = [False] * V

    DFS(0, visited)

    for i in range(1, V):
        if (visited[i] == False):
            return False

    return True


def isBridge(u, v):

    indU = adj[v].index(u)
    indV = adj[u].index(v)
    del adj[u][indV]
    del adj[v][indU]

    res = isConnected()

    # Adding the edge back
    addEdge(u, v)

    return (res == False)



ip = list(map(int, input().split()))
V = ip[1]
adj = [[] for i in range(V)]
edge = []
flag = 0

for i in range(ip[0]):
    arr = list(map(int, input().split()))
    edge.append(arr)

for i in range(ip[0]):
    addEdge(edge[i][0], edge[i][1])

resultList = set()

for i in range(ip[0]):
    if isBridge(edge[i][0], edge[i][1]):
        resultList.add(edge[i][0])
        resultList.add(edge[i][1])
        flag = 1

resultList = sorted(resultList)

if(flag == 1):
    for i in resultList:
        print(i)

elif flag == 0:
    print(-1)
