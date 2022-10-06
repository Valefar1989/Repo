def FibList(n):
    last = 1
    cur = 0
    li = [0,]
    for i in range(n):
        temp = cur
        cur += last
        last = temp
        li.append(cur)
    
    li2 = []
    for i in range(1, len(li)):
        if i % 2:
            li2.append(li[i])
        else:
            li2.append(-li[i])
    li2.reverse()
    return li2 + li


print(FibList(8))