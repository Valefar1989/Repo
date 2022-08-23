x,y = map(int, input("Введите координаты для точки а:").split())
a = []
a.append(x)
a.append(y)
x,y = map(int, input("Введите координаты для точки b:").split())
b = []
b.append(x)
b.append(y)
print(((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5))
