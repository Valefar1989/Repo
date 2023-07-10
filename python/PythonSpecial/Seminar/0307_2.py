from random import randint as rd


def guess(down, up, tries):
    if down > up:
        up, down = down, up
    aim = rd(down, up)
    count = 0
    while count < tries:
        try:
            tmp = int(input('Введите целое число: '))
        except:
            print('Нужно ввести ЦЕЛОЕ число')
            count+=1
            continue
        if tmp < aim:
            print('Число больше')
        elif tmp > aim:
            print('Число меньше')
        else:
            return True
        count += 1
    return False


if __name__=='__main__':
    print(guess(10,100,9))





  
