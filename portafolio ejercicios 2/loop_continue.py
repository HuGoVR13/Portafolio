j = 0 
for i in range (10):
    j += 2
    print('i:', i, 'j', j)
    if j >= 2 and j <=6:
        continue
    print("el valor de j: ", j)
