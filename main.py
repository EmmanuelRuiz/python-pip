import random


def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('Elige: ').lower()

    if not user_option in options:
        print('Esa no es una opción valida')
        return None, None
    
    computer_option = random.choice(options)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("EMPATE")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("User +1, Piedra gana a tijera")
            user_wins += 1
        else:
            print("Comp +1, Papel gana a piedra")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("User +1, Papel gana a piedra")
            user_wins += 1
        else:
            print("Comp +1, Tijera corta papel")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("User +1, Tijera corta papel")
            user_wins += 1
        else:
            print("Comp +1, Piedra aplasta tijera")
            computer_wins += 1
    
    return user_wins, computer_wins
        

def main():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print("*" * 20)
        print("ROUND", rounds)
        print("computer_wins", computer_wins)
        print("user_wins", user_wins)
        print("*" * 20)

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        rounds += 1

        if user_wins == 2:
            print('GANÓ USER')
            break
        if computer_wins == 2:
            print('GANO PC')
            break


if __name__ == '__main__':
    main()