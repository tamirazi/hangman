import random
import hangman_pictures

def choose_word(file_path, index):
    f = open(file_path, 'r')
    words = []
    for row in f:
        words.append(row.split('\n')[0])

    mod_index = index % len(words)
    return len(set(words)), words[mod_index - 1]

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
        print(' -> '.join(old_letters_guessed))
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


def main():
    turn = 1
    old_letters_guessed = []
    MAX_TRIES = 6
    hangman_pictures.print_start_screen()
    num_of_words = choose_word('animals.txt', 1)[0]

    random_index = random.randint(0, num_of_words)
    secret_word = choose_word('animals.txt', random_index)[1]
    # print(secret_word)
    while(turn <= MAX_TRIES):
        hangman_pictures.print_hangman(turn)
        print(show_hidden_word(secret_word, old_letters_guessed),'\n')
        print('Turn %s/%s' % (turn, MAX_TRIES))
        letter_guessed = input('Guess a letter :')
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if letter_guessed not in secret_word:
                print(':(')
                turn += 1
        if check_win(secret_word, old_letters_guessed):
            print('YOU WIN!!!')
            exit(1)
        
    hangman_pictures.print_hangman(turn)
    print(show_hidden_word(secret_word, old_letters_guessed),'\n')
    print('YOU LOSE! try next time :)')

if __name__ == "__main__":
    main()