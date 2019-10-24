import random
rand = random.randint(1, 10)
counter = 0  
while counter != 10:
    inp = int(input("Введите число от 1 до 10 (У вас 10 попыток): "))
    counter += 1
    if inp > rand:
        print("Загаданное число меньше\n")
    elif inp < rand:
        print("Загаданное число больше\n")
    else:
        print("Вы угадали\n")
        break
