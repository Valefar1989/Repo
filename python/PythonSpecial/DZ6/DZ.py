import numpy as num
 
 
def can_stand(row, pos, field):
    test_field = field.copy()
    test_field[row][pos] = True
    for i in range(len(test_field)):
        if num.sum(num.diagonal(test_field, i)) > 1:
            return False
        if num.sum(num.diagonal(test_field, -i)) > 1:
            return False
        if num.sum(num.diagonal(num.rot90(test_field), i)) > 1:
            return False
        if num.sum(num.diagonal(num.rot90(test_field), -i)) > 1:
            return False
    return True
 
 
def queens(size):
    CASES = []
    s = []
    s1 = []
    if size == 3:
        return
    number_of_cases = {4: 2, 5: 10, 6: 4, 7: 40, 8: 92, 9: 352, 10: 724, 11: 2680, 12: 14200}
    field = num.zeros((size, size), dtype='bool_')
    while len(CASES) < number_of_cases.get(size):
        for i in range(size):
            s.clear()
            s1.clear()            
            pos = num.random.randint(0, size)
            while pos in s:
                pos = num.random.randint(0, size)
            s.append(pos)
            count = 1
            while num.any(field[:, pos]) or not can_stand(i, pos, field):
                pos = num.random.randint(0, size)
                while pos in s1:
                    pos = num.random.randint(0, size)
                s1.append(pos)                
                count += 1
                if count == size:
                    count = False
                    break
            if not count:
                break
            field[i][pos] = True
        text = ''.join([str(j + 1) for i in field for j in range(len(i)) if i[j]])
        if text not in CASES and len(text) == size:
            CASES.append(text)
        field = num.zeros((size, size), dtype='int8')
    for i in sorted(CASES):
        print(i)