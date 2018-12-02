#Second half is incredibly slow...  I will work on it!!
def dayOne(file):
    input = open(file)
    nums = []
    for line in input:
        nums.append(int(line))
    print(sum(nums))

    freq = 0
    track = []
    for n in nums:
        freq += n
        nums.append(n)
        if freq not in track:
            track.append(freq)
        else:
            break
    return(freq)

print(dayOne("Inputs/Day-1.txt"))
