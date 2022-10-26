from pve import pve
from pvp import pvp

s_game = int(input('Для игры с игрок против игрока введите 1. Для игры с ботом введите 2: '))

if s_game == 1:
    pvp()
else:
    pve()
