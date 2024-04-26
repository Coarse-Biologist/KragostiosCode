from itemClass import*
def choice_int_checker(min, max):
    choice = input("Choose!")
    while True:
            if isinstance(choice, int):
                if min < choice <= max:
                        return choice
                choice = input("Error! Select a viable option!")
            else: 
                try:
                    choice = int(choice)
                except ValueError:
                    choice = input("Error! Select a viable option!")


def is_vowel(char):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return (char.lower() in vowels)


