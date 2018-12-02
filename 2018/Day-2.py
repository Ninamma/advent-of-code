def dayTwo(file):
    file = open(file)
    input = []
    for line in file:
        input.append(line.split('\n')[0])

    countTwo = 0
    countThree = 0
    for string in input:
        two = 0
        three = 0
        track = []
        for let in string:
            if let not in track:
                count = string.count(let)
                if count == 2:
                    two += 1
                elif count ==3:
                    three += 1
                track.append(let)

        if two != 0:
            countTwo += 1
        if three != 0:
            countThree +=1
    print("Checksum:", countTwo*countThree)


    for string in input:
        first = string
        for leftover in input[1:]:
            results = zip(first,leftover)
            matches = 0
            umm = ""
            for i in results:
                if i[0] == i[1]:
                    matches += 1
                    umm += i[0]
            if matches == len(string)-1:
                return(umm)

print(dayTwo("Inputs/Day-2.txt"))
