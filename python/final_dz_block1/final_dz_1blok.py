array = ["Hello", "in", "world", "i", "2"]
new_array = []
i = 0
while i < len(array):
    if len(array[i]) <= 3:
        new_array.append(array[i])
    i += 1
print(new_array)



