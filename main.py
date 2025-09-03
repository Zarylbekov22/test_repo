import random

lucky_list = [1, 2, 3, 4, 5]

def func_list(player):
    lucky_list_random = random.choice(lucky_list)
    if player == lucky_list_random:
        return f'Вы угадали! Загаданное число - {lucky_list_random}'
    else:
        return f'Неверно! Загаданное число - {lucky_list_random}'



while True:
    print("1. Игра угадай число от 1 до 5")
    print("2. Выйти")
    
    user_nums = input("Выберите пункт: ")
    
    if user_nums == '1':
        print("Угадайте число от 1 до 5")
        try:
            user_answer = int(input("Введите число от 1 до 5: "))
            if user_answer not in lucky_list:
                print("Ошибка! Введите число от 1 до 5")
                continue
            print(func_list(player=user_answer))
        except ValueError:
            print('Ошибка! Введите число а не текст!')
    
    elif user_nums == '2':
        print("Выходи из меню..")
        break
    else: 
        print("Такого пункта в меню нет!")