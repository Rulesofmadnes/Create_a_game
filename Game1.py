import random
import time


def get_user_choice():
    user_choice = input("Выберите Камень, Ножницы или Бумагу: ").strip().lower()
    while user_choice not in ["камень", "ножницы", "бумага"]:
        print("Неверный выбор. Попробуйте снова.")
        user_choice = input("Выберите Камень, Ножницы или Бумагу: ").strip().lower()
    return user_choice


def get_computer_choice():
    return random.choice(["камень", "ножницы", "бумага"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        return "Вы победили!"
    else:
        return "Вы проиграли!"


def play_game():
    print("Добро пожаловать в игру Камень-Ножницы-Бумага!")
    score = {"Победы": 0, "Поражения": 0, "Ничьи": 0}
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("Компьютер выбрал:", computer_choice)
        time.sleep(1)  # Задержка для имитации "думающего" компьютера
        print("Результат:", determine_winner(user_choice, computer_choice))
        if determine_winner(user_choice, computer_choice) == "Вы победили!":
            score["Победы"] += 1
        elif determine_winner(user_choice, computer_choice) == "Вы проиграли!":
            score["Поражения"] += 1
        else:
            score["Ничьи"] += 1
        print("Счет:", score)
        play_again = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
        if play_again != "да":
            print("Спасибо за игру!")
            break


play_game()
