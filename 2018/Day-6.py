input = open("Inputs/Day-6.txt")

#Make smallest size of grid
x = []
y = []
names = []

count = 1
for line in input:
    splt = line.split(', ')
    x.append(int(splt[0]))
    y.append(int(splt[1]))
    names.append(str(count))
    count += 1

Grid = [0] * max(y)
for i in range(max(y)):
    Grid[i] = [0]*max(x)

#Populate points on Grid, origin at 1,1
coords = zip(x,y)
crds = []

count = 0
for point in coords:
    #print(point[0],point[1])
    Grid[point[1]-1][point[0]-1] = names[count]
    count += 1
    crds.append(point)
    #print(point[0]*point[1])

 #Find coordinates of all points on grid
allPoints = []
for num in range(max(x)):
    xCoord = num + 1
    for num in range(max(y)):
        yCoord = num + 1

        allPoints.append([xCoord,yCoord])


def ManDist(x,y):
    dist = []
    #return x,y, coords
    for point in crds:
        #print(point[0],point[1])
        xDiff = abs(x - point[0])
        yDiff = abs(y - point[1])
        dist.append(xDiff+yDiff)
    return dist

def findClosest(x,y):
    dist = ManDist(x,y)
    occurance = dist.count(min(dist))
    if occurance > 1:
        Grid[y-1][x-1] = '.'
    else:
        Grid[y-1][x-1] = names[dist.index(min(dist))]
for point in allPoints:
    x = point[0]
    y = point[1]
    #print(x,y)
    findClosest(x,y)


infinite = []
#top and bottom
for let in names:
    if let in Grid[0] and let not in infinite:
        infinite.append(let)
    if let in Grid[-1] and let not in infinite:
        infinite.append(let)

#left and right
for row in Grid:
    if row[0] not in infinite:
        infinite.append(row[0])
    if row[-1] not in infinite:
        infinite.append(row[-1])
#print(infinite)

for letter in infinite:
    if letter != '.':
        names.remove(letter)
areas = []
for remaining in names:
    area = 0
    for row in Grid:
        area += row.count(remaining)
        areas.append(area)

print("Part 1:", max(areas))
count = 1
for point in allPoints:
    x = point[0]
    y = point[1]
    tup = (x,y)
    #if tup not in crds:
    dist = ManDist(x,y)
    if sum(dist) < 10000:
        Grid[y-1][x-1] = "yo"
        count += 1
a = 0
for row in Grid:
    a += row.count("yo")

print("Part 2:", a)


"""

def everyCoord(grid):
    points = []
    countY = 1
    for row in grid:
        y = countY
        countY += 1
        countX = 1
        for point in row:
            x = countX
            countX += 1
            points.append(str(x)+","+str(y))
    return points

print(everyCoord(Grid))
"""
