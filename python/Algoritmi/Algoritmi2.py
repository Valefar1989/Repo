l_1 = [6, 5, 1, 4, 2]

def insetr_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while array[j] > temp and j >=0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
        
insetr_sort(l_1)
print(l_1)