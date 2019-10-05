def _max(Num1, Num2):
    if Num1 < Num2:
        return Num2
    elif Num1 > Num2:
        return Num1
    elif Num1 == Num2:
        return "Числа равны"
    else:
        ("Что то пошло не так")

num = input("Введи первое чиcло: ")
num2 = input("Введи второе число: ")

print(_max(num,  num2))
