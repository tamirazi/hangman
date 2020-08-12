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


print(check_win("yes", ['d', 'g', 'e', 'i', 's', 'k', 'y']))
