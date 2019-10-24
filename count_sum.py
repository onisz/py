number = input("Введите число: ")
c = 0
for i in number:
    if int(i) % 2 != 0:
        c += int(i) ** 2
print(c)
