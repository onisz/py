s = str("У лукоморья 123 дуб зеленый 456")
print("Индекс буквы","я: " , s.index("я"))
print("Кол-во буквы", "у: ", s.count("у"))
if s.isalpha() == True:
    print(s.upper())
else:
    print("У лукоморья 123 дуб зеленый 456")
if len(s) > 4:
    print(s.lower())
print(s.replace((s[::1]), 'о') + s[1::])
