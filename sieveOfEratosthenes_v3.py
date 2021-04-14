while 1:
    try:
        n = int(input("Enter a number: "))
        if n < 2:
            continue
        else:
            break
    except:
        continue

set1 = [i for i in range(2, n+1)]
for j in set1:
    if j == 2:
        #2 is prime
        #remove all multiples of the number
        for l in range(j+j, n+1, j):
            #print(l)
            try:
                set1.remove(l)
            except:
                continue

    for k in range(2, j):
        if j%k == 0:
            break

        #then it's prime
        #remove all multiples of the number
        for l in range(j+j, n+1, j):
            #print(l)
            try:
                set1.remove(l)
            except:
                continue


new_set = set(set1)
print(new_set)