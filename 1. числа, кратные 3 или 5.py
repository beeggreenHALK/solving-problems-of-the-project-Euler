a = 0
summ = 0
while a <1000:
    if a % 3 == 0 or a % 5 == 0:
       summ += a
       a += 1
    else:
        a +=1
print(summ)
