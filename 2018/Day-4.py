#Yup... this is all terrible... don't judge me...
input = open("Inputs/Day-4.txt")

nonChron = []
count = 0

for line in input:
    nonChron.append(line.split('\n')[0])
chron = sorted(nonChron)

guards = []
indicies = []
for entry in chron:
    if "Guard" in entry:
        guard = entry.split('#')[1].split(' ')[0]
        #if guard not in guards:
        guards.append(guard)
        indicies.append(chron.index(entry))

details = []
count = 1
for loc in indicies[:-1]:
    details.append(chron[loc+1:indicies[count]])
    count += 1
details.append(chron[indicies[-1]+1:])
#print(details)
mins = []

#The minute the guard falls asleep and wakes up at
count = 0
for day in details:
    mins.append([])
    for timestamp in day:
        timestamp = timestamp.split(':')[1][0:2]
        mins[count].append(int(timestamp))
    count += 1
#print(mins)
#How long the guard is asleep for each day
asleep = []
count = 0
for day in mins:
    x = len(day)-1
    asleep.append([])
    while x > 0:
        asleep[count].append(day[x]-day[x-1])
        x -= 2
    asleep[count].reverse()
    count += 1
#print(asleep)

totals = []
count = 0 #initially tried to use same index as day in asleep but doesn't work if 2 days have the same value
for day in asleep:
    #totals.append([])
    totals.append(sum(day))
    count += 1
#print(totals)

combined = zip(guards, totals)

guardsUnique = []
for guard in guards:
    if guard not in guardsUnique:
        guardsUnique.append(guard)

#print(guardsUnique)

tots = [0]*(len(guardsUnique))
for day in combined:
    guardindex = guardsUnique.index(day[0])
    tots[guardindex] += day[1]
#print(tots)

sleepyGuard = (guardsUnique[tots.index(max(tots))])

def whenMostAsleep(grd):
    sleepyisAsleep = []

    count = 0
    for guard in guards:
        if guard == grd:
            sleepyisAsleep.append(mins[count])
        count += 1
    #print(sleepyisAsleep)


    asleep = []

    for day in sleepyisAsleep:
        count = 1
        for min in day:
            if day.index(min)%2 == 0:
                for i in range(min, day[count]):
                    asleep.append(i)
                count += 2

    if asleep == []:
        fave = 0
    else:
        fave = (max(set(asleep), key=asleep.count))

    return([asleep.count(fave),fave])

print("Part 1:", whenMostAsleep(sleepyGuard)[1]*int(sleepyGuard))

nums = []
faves = []
for guard in guardsUnique:
    #print(guard, whenMostAsleep(guard))
    nums.append(whenMostAsleep(guard)[0])
    faves.append(whenMostAsleep(guard)[1])

where = nums.index(max(nums))

print("Part 2:", int(guardsUnique[where])*faves[where])

"""
isAsleep = []
count = 0
for day in mins:
    isAsleep.append([])
    for min in day:
        if day.index(min)%2 == 0:
            isAsleep[count].append(min)
        else:
            isAsleep[count].append(min-1)
    count += 1
print(isAsleep)

sleepyisAsleep = []

count = 0
for guard in guards:
    if guard == sleepyGuard:
        sleepyisAsleep.append(isAsleep[count])
    count += 1
print(sleepyisAsleep)

asleep = []

for day in sleepyisAsleep:
    for min in day:
        if day.index(min)%2 == 0:
            for i in range(min:)

#count = (guards.count(sleepyGuard))
#while count > 0:



faveSleeps = []
for day in sleepyisAsleep:
    for i in day:
        faveSleeps.append(i)

fave = (max(set(faveSleeps), key=faveSleeps.count))


print(faveSleeps)
print(int(sleepyGuard))
print(fave*int(sleepyGuard))



found = []
for entry in chron:
    string = "Guard #" + str(sleepyGuard)
    if string in entry:
        found.append(chron.index(entry))
print(found)


indicies = []
for entry in chron:
    if "Guard" in entry:
        indicies.append(chron.index(entry))
count = 0

lsts = []
for i in indicies[:-1]:
    start = i
    end = indicies[count+1]
    lsts.append(chron[start:end])
    count += 1

for i in lsts:
    num = i[0].split(']')[1].split('#')[1].split(' ')[0]
    for j in i:
        if "falls asleep" in j:
            asleep = datetime.strptime(j[12:17], "%H:%M").time()
            print(asleep)




for i in lsts:
    print(i)

        num = re.search(r'\d+',entry.split(']')[1]).group()
        if num not in guards:
            lsts.append([])
            guards.append(num)
            count += 1
        lsts[count].append(chron.index(entry))

print(lsts)

for g in guards:
    indx = enumerate(chron)
    print(chron[indx])
"""
