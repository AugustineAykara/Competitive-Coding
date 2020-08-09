from math import sqrt, radians, cos, sin, asin
n=int(input())
lat = list(map(float,input().split()))
lon = list(map(float,input().split()))
h = list(map(int,input().split()))
jas = list(map(float,input().split()))
r = 6371
tow = list(zip(lat,lon,h))
def distance(lat1,lat2,lon1,lon2) :
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    dis = sin(dlat / 2) * 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) * 2
    c = 2 * asin(sqrt(dis))
    return c * r
def g(h) :
    p = 2 * h* r
    dist = pow(p,0.5)
    return dist
def possible(tow,jas) :
    x = g(tow[2])
    y = distance(tow[0],jas[0],tow[1],jas[1])
    return y <= x
count = 0
for i in range(0,n) :
    if possible(tow[i],jas) :
        count += 1
print(count)