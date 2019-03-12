input = open("Inputs/Day-6.txt")

""" 
To avoid confusion, 'given point' is used for the specific coordinates given in the input, with a name that is a number.
'Coordinate' is used for when referring to any generic coordinate in a grid.
"""

x = []
y = []
names = []

count = 1
for line in input:
    splt = line.split(', ')
    x.append(int(splt[0]))
    y.append(int(splt[1]))
    names.append(str(count)) #Naming given points
    count += 1

Grid = [0] * (max(y) + 1) #Adding 1 to make 0,0 the origin - in case of edge cases
for i in range(max(y) + 1):
    Grid[i] = [0]* (max(x) + 1)

#Populate points on grid
coords = zip(x,y) #Creates a zip object
crds = list(coords) #Extracting given points

count = 0
for point in coords:
    Grid[point[1]][point[0]] = names[count] #Plotting names of given points
    count += 1

#Listing all coordinates in grid
allPoints = []
for num in range(max(x) + 1):
    xCoord = num
    for num in range(max(y) + 1):
        yCoord = num
        allPoints.append([xCoord,yCoord])

def ManDist(x,y): #Calculating Manhattan distances between a coordinate (x,y) and given point
    dist = []
    for point in crds:
        xDiff = abs(x - point[0])
        yDiff = abs(y - point[1])
        dist.append(xDiff+yDiff)
    return dist

def findClosest(x,y): #Finding the closest given point(s) from coordinate (x,y)
    dist = ManDist(x,y)
    occurance = dist.count(min(dist))
    if occurance > 1: #Coordinates that are equidistant from more than one given point
        Grid[y][x] = '.'
    else:
        Grid[y][x] = names[dist.index(min(dist))]

for point in allPoints:
    x = point[0]
    y = point[1]
    findClosest(x,y)

#If name of a given point is on the outer edges of the grid, it has infinite area
infinite = [] 
#Checking top and bottome rows
for name in names:
    if name in Grid[0] and name not in infinite:
        infinite.append(name)
    if name in Grid[-1] and name not in infinite:
        infinite.append(name)

#Checking left and right columns
for row in Grid:
    if row[0] not in infinite:
        infinite.append(row[0])
    if row[-1] not in infinite:
        infinite.append(row[-1])

for name in infinite:
    if name != '.':
        names.remove(name) #Removing given points with infinite areas

areas = []
for remaining in names:
    area = 0
    for row in Grid:
        area += row.count(remaining)
        areas.append(area) 

print("Part 1 - Largest area of a given point, that isn't infinite:", max(areas))


count = 1
for point in allPoints:
    x = point[0]
    y = point[1]

    dist = ManDist(x,y)
    if sum(dist) < 10000:
        Grid[y][x] = "yo"
        count += 1
area = 0
for row in Grid:
    area += row.count("yo")

print("Part 2 - Area of coordinates with sum of Manhattan distances from all given points that is less than 10000:", area)