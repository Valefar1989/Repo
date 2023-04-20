import random
import datetime
l_1 = [6, 5, 1, 4, 2]

def insetr_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while (array[j] > temp and j >=0):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
        
#insetr_sort(l_1)
#print(l_1)

def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


array_1 = [random.randint(0, 10) for i in range(10001)]
array_2 = array_1.copy()

start_time = datetime.datetime.now()
quicksort(array_1)
end_time = datetime.datetime.now()
print(end_time - start_time)

start_time = datetime.datetime.now()
insetr_sort(array_2)
end_time = datetime.datetime.now()
print(end_time - start_time)