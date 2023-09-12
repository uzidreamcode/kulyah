from math import sqrt

def minkowski_distance(a,b,p):
    return sum(abs(e1-e2)**p for e1,e2 in zip(a,b))**(1/p)

row1 = [10,20,15,10,5]
row2 = [12,24,18,8,7]

dist = minkowski_distance(row1,row2,1)

print(dist)
dist = minkowski_distance(row1,row2,2)
print(dist)