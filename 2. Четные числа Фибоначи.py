a, b = 1, 2
summ = 0
while a <= 4000000:
    if a % 2 == 0:
        summ += a
        a, b = b, a+b
    else:
        a, b = b, a+b
print(summ)

