

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
        print(letter_guessed.upper())
        old_letters_guessed.sort()
        print(' -> '.join(old_letters_guessed))
        return False


try_update_letter_guessed('a', ['b', 'a', 'c'])
