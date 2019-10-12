def parity(N):
    if N % 2 == 0:
        return "Число четное"
    else:
        return "Число нечетное"

number = int(input("Введите число: "))

print(parity(number))
