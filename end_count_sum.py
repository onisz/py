s = 0
while True:
    n = input("Введите число: ")
    n1 = str(n)
    if n1 == "Стоп":
        break
    s += float(n)
print(s)
