from random import randint

power = int(input('Введите натуральную степень многочлена (наивысшая степень в полиноме): '))


def polinom(power):
    with open('file2.txt', 'w') as polinom:
        for i in range(power, -1, -1):
            koef = randint(0, 100)
            if i > 0:
                if koef > 0:
                    polinom.write(f'{str(koef)}x^{str(i)} + ')
            else:
                if koef > 0:
                    polinom.write(f'{str(koef)} = 0')
                else:
                    polinom.write(' = 0')