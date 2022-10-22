i = 2
multipliers = []
while i ** 2 <= user_number:
    while user_number % i == 0:
        multipliers.append(i)
        user_number = user_number // i
    i = i + 1
if user_number > 1:
    multipliers.append(user_number)
print(multipliers)
