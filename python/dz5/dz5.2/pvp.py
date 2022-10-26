from random import randint

def pvp():
	name_one = input('Введите имя первого игрока:')
	name_two = input('Введите имя второго игрока:')
	lot = randint(1, 2)

	if lot == 1:
		print(f"Жребий брошен. {name_one} ходит первым!")
	else:
		print(f"Жребий брошен. {name_two} ходит первым!")

	if lot == 1:
		candy_max = 2021
		while candy_max > 28:
			candy_gamer = int(input(f"{name_one}, введите количество конфет, которые хотите забрать. От 1 до 28: "))

			if candy_gamer > 28:
				print(f'{name_one}, читер!, {name_two}, выиграл!!!!')
				break

			if candy_gamer < 0:
				print(f'{name_one} самый умный?  GAME OVER!')
				break

			candy_max = candy_max - candy_gamer
			print(f"Осталось конфет: {candy_max}")

			if candy_max <= 28:
				print(f'{name_two}, выиграл!')
				break

			candy_gamer = int(input(f"{name_two}, введите количество конфет, которые хотите забрать. От 1 до 28: "))

			if candy_gamer > 28:
				print(f'{name_two}, читер!, {name_one}, выиграл!!!!')
				break

			if candy_gamer < 0:
				print(f'{name_two} самый умный?  GAME OVER!')
				break

			candy_max = candy_max - candy_gamer
			print(f"Осталось конфет: {candy_max}")

			if candy_max <= 28:
				print(f'{name_one}, выиграл!')
				break
	if lot == 2:

		candy_max = 2021
		while candy_max > 28:
			candy_gamer = int(input(f"{name_two}, введите количество конфет, которые хотите забрать. От 1 до 28: "))

			if candy_gamer > 28:
				print(f'{name_two}, читер!, {name_one}, выиграл!!!!')
				break

			if candy_gamer < 0:
				print(f'{name_two} самый умный?  GAME OVER!')
				break

			candy_max = candy_max - candy_gamer
			print(f"Осталось конфет: {candy_max}")

			if candy_max <= 28:
				print(f'{name_one}, выиграл!')
				break

			candy_gamer = int(input(f"{name_one}, введите количество конфет, которые хотите забрать. От 1 до 28: "))

			if candy_gamer > 28:
				print(f'{name_one}, читер!, {name_two}, выиграл!!!!')
				break

			if candy_gamer < 0:
				print(f'{name_one} самый умный?  GAME OVER!')
				break

			candy_max = candy_max - candy_gamer
			print(f"Осталось конфет: {candy_max}")

			if candy_max <= 28:
				print(f'{name_two}, выиграл!')
				break



	



