from colorama import Fore, Back, Style


pic1 = '''
    x-------x
'''
pic2 = '''
    x-------x
    |
    |
    |
    |
    |
'''
pic3 = '''
    x-------x
    |       |
    |       0
    |
    |
    |

'''
pic4 = '''
    x-------x
    |       |
    |       0
    |       |
    |
    |
'''
pic5 = '''
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
'''
pic6 = '''
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
'''
pic7 = '''
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
'''

HANGMAN_ASCII_ART = ''' 
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
'''
HANGMAN_PHOTOS = {
    1: pic1,
    2: pic2,
    3: pic3,
    4: pic4,
    5: pic5,
    6: pic6,
    7: pic7,
}


def print_hangman(num_of_tries):
    print(Fore.MAGENTA +  HANGMAN_PHOTOS[num_of_tries] + Style.RESET_ALL)

def print_start_screen():
    print(Fore.GREEN + HANGMAN_ASCII_ART + Style.RESET_ALL)
