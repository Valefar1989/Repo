my_str = 'aaabbbcccccc'

def encording (data):

    encording = ''
    i = 0
    while i < len(data):
        count = 1

        while i + 1 < len(data) and data[i]  == data[i + 1]:
            count = count + 1
            i = i + 1

        encording += str(count) + data[i]
        i = i + 1

    return encording

print(encording(my_str))
