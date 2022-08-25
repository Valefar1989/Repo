n = int(input())
i = 1
num = []
while i <= n:
	num.append(i)
	i = i+1
mult_num = []
for j in num:
	d = 0
	mult = 1
	while d <= num.index(j):
		mult = mult*num[d]
		d = d+1
	mult_num.append(mult)
print(mult_num)
	
		
	
		
	
	
	