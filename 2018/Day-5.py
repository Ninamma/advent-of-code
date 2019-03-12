#Will get you the right answer, but will take a bloody long time...
import string
input = open("Inputs/Day-5.txt")

def shift(txt):
    if txt == txt.lower():
        return txt.upper()
    else:
        return txt.lower()

def remDupe(string):
        list = []
        for l in string:
            list.append(l)

        count = 0
        while count < len(list) - 1:
            try:
                for let in list:
                    if shift(let) == list[count+1]:
                        list[count] = ''
                        list[count+1] = ''
                    count += 1
                return list
            except:
                return list

lne = []
for line in input:
    lne.append(line)

def fullReact(string):
    while string != ''.join(remDupe(string)):
        string = ''.join(remDupe(string))
    return string
print("Part 1:", len(fullReact(lne[0])))

removedLengths= []
for let in string.ascii_lowercase:
    str = lne[0]
    nolittle = str.maketrans('','',let)
    str = str.translate(nolittle)
    nobig = str.maketrans('','',let.upper())
    str = str.translate(nobig)
    removedLengths.append(len(fullReact(str)))
    #print(len(fullReact(str)))
print("Part 2:", min(removedLengths))


"""
#alphabet = []
removedLengths= []
for let in string.ascii_lowercase:
    str = lne[0].replace(let,"").replace(shift(let),"")
    removedLengths.append(len(fullReact(str)))
    print(len(fullReact(str)))
print(min(removedLengths))


removedLengths= []
for let in line:
    if let.lower() not in units:
        str = lne[0].replace(let,"").replace(shift(let),"")
        removedLengths.append(len(fullReact(str)))
        units.append(let.lower())
        print(len(fullReact(str)))
print(min(removedLengths))

for unit in units:
    str = lne[0].replace(unit,"").replace(shift(unit),"")
    removedLengths.append(len(fullReact(str)))

for i in range(300):
    try:
        lne[0] = (''.join(remDupe(lne[0])))
    except:
        print(lne[0])
print(len(lne[0]))
"""
