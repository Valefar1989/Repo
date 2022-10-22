with open('file1.txt', 'r') as polinom1:
    my_str1 = polinom1.read()
with open('file2.txt', 'r') as polinom2:
    my_str2 = polinom2.read()

my_list1 = my_str1.split(' + ')
my_list2 = my_str2.split(' + ')

dictionary1 = {}

for i in range(len(my_list1)):
    if 'x' in my_list1[i]:
        posX = my_list1[i].find('x')
        dictionary1[int(my_list1[i][posX + 2:])] = int(my_list1[i][:posX])
    else:
        posEqualy = my_list1[i].find(' =')
        dictionary1[0] = int(my_list1[i][:posEqualy])

print(dictionary1)
dictionary2 = {}

for i in range(len(my_list2)):
    if 'x' in my_list2[i]:
        posX = my_list2[i].find('x')
        dictionary2[int(my_list2[i][posX + 2:])] = int(my_list2[i][:posX])
    else:
        posEqualy = my_list2[i].find(' = ')
        dictionary2[0] = int(my_list2[i][:posEqualy])

print(dictionary2)

maxDegree = max(max(dictionary1.keys()), max(dictionary2.keys()))

with open('file3.txt', 'w') as two_polinom:
    for i in range(maxDegree, 0, -1):
        koef = 0
        if i in dictionary1.keys():
            koef += dictionary1[i]
        if i in dictionary2.keys():
            koef += dictionary2[i]
        if koef != 0:
            two_polinom.write(f'{koef}x^{i} + ')
    koef = 0
    if 0 in dictionary1.keys():
        koef += dictionary1[0]
    if 0 in dictionary2.keys():
         koef += dictionary2[0]
    if koef != 0:
         two_polinom.write(f'{koef} = 0')