#def finalSum(input):
input = open("Inputs/Day-1.txt")
s = []
for line in input:
    #if line.find("\n") != -1:
        #line = input.readline()#.split('\n')[0]
    #print(line)
    s.append(int(line))
print(sum(s))

freq = 0
track = []
for n in s:
    freq += n
    s.append(n)
    if freq not in track:
        track.append(freq)
    else:
        break
print(freq)





#print(finalSum(open("Inp uts/Day-1.txt")))
#print(twice(open("Inputs/Day-1.txt")))
#print(twice())
