from random import randint


def pve():
    candy_max = 2021
    name_player = input(' Введите свое имя: ')
    name_player = name_player.capitalize()
    name_bot = 'СуперБот'
    lot = randint(1, 2)

    if lot == 1:
        print(f" {name_player} ходит первым!")
    else:
        print(f"{name_bot}, ходит первым!")

    if lot == 1:
        while candy_max > 28:
            candy_gamer = int(input(f"{name_player}, введите количество конфет, которые хотите забрать. От 1 до 28: "))

            if candy_gamer > 28:
                print(f"{name_player} читер! {name_bot} выиграл!")
                break
            if candy_gamer < 0:
                print(f'{name_player} самый умный?  GAME OVER!')
                break

            candy_max = candy_max - candy_gamer
            print(f"Осталось конфет: {candy_max}")

            if candy_max <= 28:
                print(f'{name_bot} выиграл!')
                break

            if candy_max > 500:
                candy_gamer = randint(24, 28)
                print(f"{name_bot} забрал: {candy_gamer}")
            else:
                if 100 < candy_max < 500:
                    candy_gamer = randint(15, 28)
                    print(f"{name_bot} забрал: {candy_gamer}")

                else:
                    if 60 < candy_max < 100:
                        candy_gamer = randint(5, 10)
                        print(f"{name_bot} забрал: {candy_gamer}")

                    else:
                        candy_gamer = randint(1, 5)
                        print(f"{name_bot} забрал: {candy_gamer}")

            candy_max = candy_max - candy_gamer
            print(f"Осталось конфет: {candy_max}")

            if candy_max <= 28:
                print(f'{name_player} выиграл!')
                break

    if lot == 2:
        while candy_max > 28:
            if candy_max > 500:
                candy_gamer = randint(24, 28)
                print(f"{name_bot} забрал: {candy_gamer}")
            else:
                if 100 < candy_max < 500:
                    candy_gamer = randint(15, 28)
                    print(f"{name_bot} забрал: {candy_gamer}")

                else:
                    if 60 < candy_max < 100:
                        candy_gamer = randint(5, 10)
                        print(f"{name_bot} забрал: {candy_gamer}")

                    else:
                        candy_gamer = randint(1, 5)
                        print(f"{name_bot} забрал: {candy_gamer}")

            candy_max = candy_max - candy_gamer
            print(f"Осталось конфет: {candy_max}")

            if candy_max <= 28:
                print(f'{name_player} выиграл!')
                break

            candy_gamer = int(input(f"{name_player}, введите количество конфет, которые хотите забрать. От 1 до 28: "))

            if candy_gamer > 28:
                print(f"{name_player} читер! {name_bot} выиграл!")
                break
            if candy_gamer < 0:
                print(f'{name_player} самый умный?  GAME OVER!')
                break

            candy_max = candy_max - candy_gamer
            print(f"Осталось конфет: {candy_max}")

            if candy_max <= 28:
                print(f'{name_bot} выиграл!')
                break





