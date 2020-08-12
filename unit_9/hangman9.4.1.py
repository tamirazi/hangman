

def choose_word(file_path, index):
    f = open(file_path, 'r')
    words = []
    for row in f:
        words = row.split(' ')

    mod_index = index % len(words)
    return len(set(words)), words[mod_index - 1]


print(choose_word(r"words.txt", -1))
print(choose_word(r"words.txt", 15))
