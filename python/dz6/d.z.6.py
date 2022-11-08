
# Задача из 5 урока
my_string = 'абв напр опалоабв оапио абврн аыом'

my_list = list(filter(lambda x: 'абв' not in x, my_string.split()))

print(' '.join(my_list))


# Задача из 1 урока
x, y = map(int, input('Введите через пробел координаты: ').split())
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    if x > 0 and y < 0:
        print(4)