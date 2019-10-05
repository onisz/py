import random

number_1 = int(input("Введите число от 1 до 4: "))

number_2 = random.randint(1, 4)

if number_1 == number_2:
    print("Вы угадали число", ", загаданное число:", number_2)
else:
    print("Вы не угадали")


