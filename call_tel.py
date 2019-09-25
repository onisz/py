code = int(input("Введите код города: "))
minuts = int(input("Введите минуты разговора: "))
if code == 343:
    print(minuts * 15)
elif code == 381:
    print(minuts * 18)
elif code == 473:
    print(minuts * 13)
elif code == 485:
    print(minuts * 11)
else:
    print("По данному коду нет города")
