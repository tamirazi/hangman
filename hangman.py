import random
import hangman_pictures
from colorama import Fore, Back, Style

MAX_TRIES = 6

def choose_word():
    file_path = 'animals.txt'
    f = open(file_path, 'r')
    words = []
    for row in f:
        words.append(row.split('\n')[0])

    random_index = random.randint(0, len(words))
    return words[random_index]

def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) > 1:
        return False
    if not letter_guessed[0].isalpha():
        return False
    if letter_guessed in old_letters_guessed:
        return False
    return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed += letter_guessed
        return True
    else:
        print('X')
        old_letters_guessed.sort()
        print(Back.BLUE + Fore.RED +  ' -> '.join(old_letters_guessed) + Style.RESET_ALL)
        return False

def show_hidden_word(secret_word, old_letters_guessed):
    result = ''
    for letter in secret_word:
        if letter in old_letters_guessed:
            result += letter + ' '
        else:
            result += '_ '
    return result

def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

def print_game_screen(guess_num, secret_word, old_letters_guessed):
    #this function created to shrink the main loop (only prints here)
    hangman_pictures.print_hangman(guess_num)
    print('Animal : ' + show_hidden_word(secret_word, old_letters_guessed),'\n')
    if guess_num > MAX_TRIES:
        print(Back.RED +  'YOU LOSE! try next time :)' + Style.RESET_ALL)
    else:
        print(Fore.BLUE + 'Guess number : %s/%s' % (guess_num, MAX_TRIES) + Style.RESET_ALL)
    
def main():
    guess_num = 1
    old_letters_guessed = []
    hangman_pictures.print_start_screen()
    secret_word = choose_word()
    while(guess_num <= MAX_TRIES):
        print_game_screen(guess_num, secret_word, old_letters_guessed)
        letter_guessed = input(Fore.YELLOW +  'Guess a letter : ' + Style.RESET_ALL)
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if letter_guessed not in secret_word:
                print(Back.WHITE + Fore.BLACK + ':(' + Style.RESET_ALL)
                guess_num += 1
        if check_win(secret_word, old_letters_guessed):
            print(Fore.CYAN +  'YOU WIN!!!' + Style.RESET_ALL)
            exit(1)

    print_game_screen(guess_num, secret_word, old_letters_guessed)

if __name__ == "__main__":
    main()