import random
words = ["самовар", "весна", "лето"]
rand_word = random.choice(words)
rand_letter = random.choice(rand_word)
ind = rand_word.index(rand_letter)
secret_word = rand_word[:ind] + "?" + rand_word[ind + 1:]
print(secret_word)
secret_letter = str(input("Введите загаданную букву: "))
if secret_letter == rand_letter:
    print("Вы угадали!")
else:
    print("Вы не угадали!")

