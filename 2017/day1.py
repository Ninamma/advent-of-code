num = open("2017/inputs/day1.txt")

num1 = "1122"
num2 = "1111"
num3 = "1234"
num4 = "91212129"
num5 = num.read()

def sumMatches(n):
    lst = []
    for i in n.strip():
        lst.append(int(i))
    length = len(lst)

    matches = []

    if lst[0] == lst[-1]:
        matches.append(lst[0])

    for i in range(0,length-1):
        if lst[i] == lst[i+1]:
            matches.append(lst[i])

    return (sum(matches))

print (sumMatches(num1))
print (sumMatches(num2))
print (sumMatches(num3))
print (sumMatches(num4))
print (sumMatches(num5))
