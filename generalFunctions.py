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

def option_print_iter(option_presenter: str, option_list: tuple, option_number: int):
    print(option_presenter)
    x = 0
    while x < option_number:
        current_option = option_list[x]
        print(f"Press {x + 1}: to {current_option}.")
        x+=1
    min = 0
    max = option_number
    choice_int_checker(min, max)
