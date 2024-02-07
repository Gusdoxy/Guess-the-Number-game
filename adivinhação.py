import random
import time
import os
def clear():
    os.system('cls')

print("---------------------")
print("Guess the Number Game")
print("---------------------")

time.sleep(2)
os.system('cls')


def difficulty():
    while True:
        print("---------------------")
        print("1 - Easy, 2 - Medium, 3 - Hard")
        choicestr = input("Choose your difficulty: ")
        choice = int(choicestr)
        print("---------------------")

        match choice:  # seleciona a dificuldade com base no input do usuario
            case 1:
                secret_number = random.randint(0, 1)
                return secret_number
            case 2:
                secret_number = random.randint(0, 10)
                return secret_number
            case 3:
                secret_number = random.randint(0, 100)
                return secret_number
            case _:
                print("invalid value")




secret_number = difficulty()  # Chama a função de escolha de dificuldade
first_try = ""
while (first_try != secret_number):
    strfirst = input("Type the number: ")
    first_try = int(strfirst)
    print("Your number is:", first_try)
    time.sleep(2)
    clear()

    if first_try == secret_number:
        print("Sucesss")
        print("The number was: ", secret_number)
        time.sleep(1)
        clear()
    elif first_try < secret_number:
        print("oh no! Wrong number")
        print("Tip: The secret number is lower than the one that you chose")
        print(secret_number)
        time.sleep(1)
        clear()
    elif first_try > secret_number:
        print("oh no! Wrong number")
        print("Tip: The secret number is lower than the one that you chose")
        print(secret_number)
        time.sleep(1)
        clear()

