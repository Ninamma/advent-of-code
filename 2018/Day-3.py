import numpy as np
def dayThree(file,size):
    input = open(file)
    fabric = np.zeros((size,size))
    areas = []
    for line in input:
        mes = line.split(" ")
        loc = mes[2].split(",")
        dim = mes[3].split("x")

        ID = int(mes[0][1:])
        left = int(loc[0])
        top = int(loc[1][:-1])
        width = int(dim[0])
        height = int(dim[-1])
        right = left + width
        bottom = top + height
        areas.append(width*height)
        np.place(fabric[top:bottom,left:right],fabric[top:bottom,left:right]!=0,-1)
        np.place(fabric[top:bottom,left:right],fabric[top:bottom,left:right]==0,int(ID))
    print((fabric == -1).sum())
    count = 1
    for i in areas:
        if (fabric == count).sum() == i:
            return(count)
        count += 1

print(dayThree("Inputs/Day-3.txt",1000))
