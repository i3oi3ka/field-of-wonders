# Зареєструватись на github, та створити окремий репозиторій для цього завдання
# 1. Програма буде брати зі списку слів одне рандомне слово.
# 2. Програма буде отримувати від користувача число - кількість спроб вгадати
# 3. Далі програма буде чекати від користувача або букву, або ціле слово.
# 4. Якщо користувач пише слово, програма повинна перевіряти чи це не те саме число, якщо так то говорити що користувач вгадав слово, або писати що слово не правильне.
# 5. Якщо користувач ввів літеру, програма повинна перевірити чи є ця літера у нашому слові, та якщо є, виводити наше слово, де зірочками будуть закриті всі літери, які користувач ще не вгадав, або "Такої літери немає"
# 6. Якщо кількість спроб закінчиться, потрібно сказати користувачю, що він програв та закінчити роботу програми.
#
# Приклад:
# Програмою обрано слово "apple"
# Вхід: 10 (10 спроб вгадати слово)
# Вхід: "a"
# Вихід: "a****"
# Вхід: "d"
# Вихід: "Такої літери немає"
# Вхід: "l"
# Вихід: "a**l*"
# Вхід: "e"
# Вихід: "a**le"
# Вхід: "apple"
# Вихід: "Вітаю, ви вгадали слово"
#
# Код програми залейте до вашого репозиторію та надішліть посилання у відповідь.
from random import choice

word_list = ["apple", "car", "python", "github", "xiaomi"]
key_word = choice(word_list)
print(key_word)
number_of_attempts = int(input("Enter number of attempts: "))
key_user = "*" * len(key_word)
print(key_user)

for i in range(0, number_of_attempts):
    user_answer = input("Enter letter or word: ")
    buf = ""
    if len(user_answer) > 1:
        if user_answer == key_word:
            print("Congratulate, you win!")
            key_user = key_word
            break
        else:
            print("Word wrong!")
    elif user_answer in key_word:
        for i in range(0, len(key_word)):
            if key_word[i] == user_answer:
                buf += key_word[i]
            else:
                buf += key_user[i]
    else:
        print(f"Leter '{user_answer}' not in word.")
        buf = key_user
    key_user = buf
    if key_user == key_word:
        print("Congratulate, you win!")
        break
    print(key_user)

if key_user != key_word:
    print("I'm sorry, you lose")
