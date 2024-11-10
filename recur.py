def recurs(i):
    if i == 1:
        return 0
    elif i == 2:
        return 1
    else:
        return recurs(i-1)+recurs(i-2)
    
print(recurs(10))
    
for i in range(1, 10):
    print(recurs(i))