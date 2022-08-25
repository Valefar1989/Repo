n =str(float(input()))
n_array = n.split('.')
num_one = list(n_array[0])
num_two = list(n_array[1])
i = 0
result = 0

while i < len(num_one):
	result = result + int(num_one[i])
	i = i + 1
	
i = 0

while i < len(num_two):
	result = result + int(num_two[i])
	i = i + 1
print(result)