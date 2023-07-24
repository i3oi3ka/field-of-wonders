from random import choice


def field(key: str, attempts: int):
    key_user = "*" * len(key)
    print(key_user)
    for i in range(0, attempts):
        user_answer = input("Enter letter or word: ").strip().lower()
        if len(user_answer) > 1:
            if user_answer == key:
                print("Congratulates, you win!")
                return
            else:
                print("Word wrong!")
        elif user_answer in key:
            buf = ""
            for j in range(0, len(key)):
                if key[j] == user_answer:
                    buf += key[j]
                else:
                    buf += key_user[j]
            key_user = buf
        else:
            print(f"Letter '{user_answer}' not in word.")
        if key_user == key:
            print(f"Congratulates, you win! Right word is: {key_user}")
            return
        print(key_user)
    if key_user != key:
        print("I'm sorry, you lose")


word_list = ["apple", "car", "python", "github", "xiaomi"]
key_word = choice(word_list)
# print(key_word)
number_of_attempts = int(input("Enter number of attempts: "))
print(f"You have {number_of_attempts} attempts.")

field(key_word, number_of_attempts)
