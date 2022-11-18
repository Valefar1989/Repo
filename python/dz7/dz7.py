import csv

first_name, last_name = map(str, input('Введите фамилию и имя: ').split())
tel = int(input('Введите номер телефона: '))
tel_number_names = []

tel_number_names.append(first_name), tel_number_names.append(last_name), tel_number_names.append(tel)

with open('file.txt', 'a', encoding= 'utf-8') as data:
    data.write(f'Фамилия: {tel_number_names[0]}\nИмя: {tel_number_names[1]}\nНомер телефона: {tel_number_names[2]}\n\n')

with open('file.csv', 'a', encoding= 'utf-8') as data:
    data.write(f'{tel_number_names[0]};{tel_number_names[1]};{tel_number_names[2]}\n')


