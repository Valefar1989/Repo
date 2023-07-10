# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

drob_a ='1/3'
drob_b ='2/5'

# Превращаем строку в список по разделителю
def razdel(drob):
    dr_l = drob.split('/')
    return dr_l

# Сложение
def slozhenie(drob_ls_1, drob_ls_2):
    znam = int(drob_ls_1[1])*int(drob_ls_2[1])
    cheslit = (int(drob_ls_1[0])*int(drob_ls_2[1]))+(int(drob_ls_2[0])*int(drob_ls_1[1]))
    new_drob = str(cheslit)+'/'+str(znam)
    return new_drob

# Произведение
def mult(drob_ls_1, drob_ls_2):
    znam = int(drob
    _ls_1[1])*int(drob_ls_2[1])
    cheslit = int(drob_ls_1[0])*int(drob_ls_2[0])
    new_drob = str(cheslit)+'/'+str(znam)
    return new_drob

dr_l_a = razdel(drob_a)
dr_l_b = razdel(drob_b)

print(slozhenie(dr_l_a, dr_l_b))
print(mult(dr_l_a, dr_l_b))