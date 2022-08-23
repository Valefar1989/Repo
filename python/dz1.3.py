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