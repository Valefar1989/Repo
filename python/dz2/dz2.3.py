n = int(input())
dict = {}

for i in range(1, n + 1): 
    b = 3 * i + 1
    dict.update({i:b})
print(dict)
