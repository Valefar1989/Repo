from decimal import Decimal

pi = '3.14159265358979323846'
accuracy = lambda x: Decimal(x).quantize(Decimal(input('Введите точность d в виде 0.001: ')))
print(accuracy(pi))