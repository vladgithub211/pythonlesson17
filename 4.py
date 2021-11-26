a =int(input("Ведите число"))
while a!=0:
    if a<0:
        print("Отрицательное число:", a)
        break
    a =int(input("Ведите число"))
else:
    print("отрицательных чисел нет!")
