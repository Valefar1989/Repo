array = [2, 5, 7, 8]
new_array = []
i = 0
n = -1

while i < (len(array)/2):
	mult = array[i]*array[n]
	new_array.append(mult)
	mult = 0
	i = i + 1
	n = n - 1

print(new_array)