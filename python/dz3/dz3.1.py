array = [5, 7, 11,15,19]
i = 1
n = -2

while i < (len(array)/2):
	summa = array[i] + array[n]
	print(summa)
	summa = 0
	i = i + 2
	n = n - 2
	