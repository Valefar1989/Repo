with open('test.txt', 'r') as file:
    a = list(map(int, file.read().split()))
    for i in range(len(a)-1):
        if a[i]+1 != a[i+1]:
            print(int(a[i])+1)
