import numpy as np
import matplotlib.pyplot as plt
import math


##### Create a class for Point (x,y) coordinates
class Point:
    def__init__(self,x,y):
        self.x=x
        self.y=y

        
initial_points = [(-7,8),(-4,6),(2,6),(6,4),(8,6),(7,-2),(4,-6),(8,-7),(0,0)]
#(3,-1),(6,-10),(0,-6),(-9,-5),(-8,-2),(-8,0),(-10,3),(-2,2),(-10,4)


points=[]
for point in initial_points:
    points.append(Point(point[0],point[1]))
n = len(points)
print('The number of points is : ',n)
# 9


points[0].x , points[0].y
# (-7,8)


names=''.join(['%c' % x for x in range(65, 65+n)])
names
# 'ABCDEFGHI'
names[0]
# 'A'
names[n-1]
# 'I'


def plotPoints(points,n,names):
    plt.figure(figsize=(5,5))
    for p in range(0,n):
        x = points[p].x
        y = points[p].y
        name = names[p]
        plt.plot(x,y,'bo',markersize=7)
        plt.text(x+0.025,y+0.025,name)
    plt.grid()
    plt.show()

    
'''    
print(points[0].x,points[0].y)    
pltfigure(figsize(3,3))
plt.plot(points[0].x,points[0].y,'bo',markersize=10)
plt.text(points[0].x+0.025,points[0].y+0.025,'A')
plt.grid()
#gridlines
plt.show()
#show the figure
'''


plotPoints(points,n,names)
# graph will be plotted


def findMin(points,n):
    ymin=points[0].ymin
    mindex = 0
    for p in range(1,n):
        y = points[p].y
        if(ymin>y):
            ymin = y
            mindex = p
    return mindex


min = findMin(points,n)
points[0],points[min] = points[min],points[0]


math.atan2(points[4].y-points[0].y,points[4].x-points[0].x)
# 1.57079632


math.atan2(points[3].y-points[0].y,points[3].x-points[0].x)
# 1.75064982


def findPolarAngles(points,n):
    origin = points[0]
    theta = []
    for p in range(0,n):
        angle = math.atan2(points[p].y-origin.y,points[p].x-origin.x)
        theta.append(angle)
    theta = np.round(theta,4)
    print(theta)
    return theta


plotPoints(points,n,)
theta = findPolarAngles(points,n)
print(theta)


indices = np.argsort(theta)
print(theta)
print(indices)


points_sorted = []
for p in range(0,n):
    points_sorted.append(points[indices[p]])
    

plotPoints(points_sorted,n,names)
# graph will be plotted
#(advantage of modularity : reusibility of code)


points = points_sorted


S = []
S.append(points[0])
S.append(points[1])
S.append(points[2])


def orientation(p, q, r):
    d = ((q.y-p.y)*(r.x-p.x)) - ((q.x-p.x)*(r.y-p.y))
    if d==0:
        return 0
    elif d>0:
        return 1
    else:
        return 2


'''
for c in range(3,n):
    if(orientation(S[-2],S[-1],points(c))!=1):
        S.append(points(c))
    else:
        while(S and orientation(S[-2],S[-1],points(c))==1):
            S.pop()
'''
c = 3
while(c<n):
    if(orientation(S[-2],S[-1],points(c))!=1):
        S.append(points(c))
        c=c+1
    else:
        S.pop()
        
        
for i in range(-len(S),0,1):
    print('Points are : ',S[i].x,S[i].y)
# all convexHull points will be printed


def plotConvexHull(points, hull , n, names):
    plt.figure(figsize=(5,5))
    for p in range(0,n):
        x = points[p].x
        y = points[p].y
        name = names[p]
        plt.plot(x, y, 'bo', markersize=7)
        plt.text(x+0.25, y+0.25, name)
    for c in range(-len(hull), 0, 1):
        xvalues = [hull[c].x, hull[c+1].x]
        yvalues = [hull[c].y, hull[c+1].y]
        plt.plot(xvalues, yvalues, 'bo', markersize='--', color='black')
    plt.grid()
    plt.show()
    
    
plotConvexHull(points, S, n, names)