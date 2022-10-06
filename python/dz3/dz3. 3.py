from decimal import Decimal
import math

array = [5.43, 6.77, 4.84, 8.56]
new_array = []

for i in array:
	num = math.floor(i)
	num_d = Decimal(str(i)) - Decimal(str(num))
	new_array.append(str(num_d))

new_array_s = sorted(new_array)
dif_result = Decimal(new_array_s[-1]) - Decimal(new_array_s[0])

print(float(dif_result))
