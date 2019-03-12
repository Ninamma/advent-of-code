import string
input = open("Inputs/test.txt")
#input = open("Inputs/test.txt")
steps = []
orders = []
def getSteps(input):
    for line in input:
        broken = line.split(' ')
        firstLetter = broken[1]
        secondLetter = broken[7]
        if firstLetter not in steps:
            steps.append(firstLetter)
        if secondLetter not in steps:
            steps.append(secondLetter)
        order = [firstLetter, secondLetter]
        orders.append(order)
getSteps(input)

before = []
def neededBefore(steps):
    for step in steps:
        needed = []
        for order in orders:
            if order[1] == step:
                needed.append(order[0])
        if needed == []:
            needed = [0]
        before.append(needed)
neededBefore(steps)
beforeCopy = []
for i in before:
    beforeCopy.append(i)

#Find first
ordered = []
possible = []
for a in before:
    if a == [0]:
        possible.append(steps[before.index(a)])
        before[before.index(a)] = []
possible.sort()
ordered.append(possible[0])
possible.remove(possible[0])
#print(before)
#Second
def getOrder(before):
    for left in before:
        if all(let in ordered for let in left) and left != []:
            possible.append(steps[before.index(left)])
            before[before.index(left)] = []
    if possible != []:
        possible.sort()
        ordered.append(possible[0])
        possible.remove(possible[0])


while any(left != [] for left in before):
    getOrder(before)
#print("Part 1:", ''.join(ordered))

#print(ordered)


letters = []
times = []
count = 1
for letter in string.ascii_uppercase:
    letters.append(letter)
    times.append(count)
    count += 1
#print(times, letters)

orderedTimes = []
addSixty = len(ordered)*60
for let in ordered:
    time = times[letters.index(let)]
    orderedTimes.append(time)
print(orderedTimes)

time = 0
done = [[0]]
count = 1



#print(beforeCopy)


#Reorder before
#print(steps, beforeCopy)
beforeReordered = []
for letter in ordered:
    found = steps.index(letter)
    beforeReordered.append(beforeCopy[found])
print(beforeReordered)
#print(ordered)
#for i in beforeReordered:
#    print(steps[beforeReordered.index(i)])
started = []
for needed in beforeReordered:
    if needed in done:
        time += orderedTimes[beforeReordered.index(needed)]
        done.append(ordered[beforeReordered.index(needed)])
        beforeReordered[beforeReordered.index(needed)] = [0]
print(beforeReordered)


"""


workers = [0,0]
#for worker in workers:
#    if worker == 0:
        #assign work


time = 0
done = []
for task in beforeReordered:
    if task == [0]:
        times[letters.index()]






for b in before:
    for c in b:
        if c in ordered:
            possible.append(b.index(ordered[0]))
            before.remove(b)
possible.sort()
print(ordered)

#ordered.append(possible[0])

#Third
for c in before:
    if c in ordered:
        possible.append(c)
        before.remove(c)
possible.sort()
#ordered.append(possible[0])


#print(ordered)
def reorder(steps):
    for order in orders:
        print(order)
        first = steps.index(order[0])
        second = steps.index(order[1])
        if first > second:
            steps[first] = order[1]
            steps[second] = order[0]

reorder(steps)



#print(steps)



        order.append(firstLetter)
        order.append(secondLetter)
    print(order)
"""
