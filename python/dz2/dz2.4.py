import math

n = int(input())
listOfNums = []
indexes = []
numsForMultyply = []
result = 1

for i in range(-n, n + 1):
    listOfNums.append(i)
print(listOfNums)

with open(r"D:\repo\python\dz2\file.txt") as f:
    F = f.read()
    nums = F.split('\n')

for n in nums:
    indexes.append(int(n))
print(indexes)

def Mult(indexes, listOfNums):
    for i in range(len(listOfNums)):
        for j in range(len(indexes)):
            if (i == indexes[j]):
                numsForMultyply.append(listOfNums[i])
            else:
                continue
    return math.prod(numsForMultyply)
print(Mult(indexes, listOfNums))


def Mult(indexes, listOfNums):
    for j in indexes:
        numsForMultyply.append(listOfNums[j])

    return math.prod(numsForMultyply)
print(Mult(indexes, listOfNums))