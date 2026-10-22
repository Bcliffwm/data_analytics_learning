from pathlib import Path
import getpass

# Resolve paths relative to this script, not the current working directory,
# so the program behaves the same no matter where it is launched from.
BASE_DIR = Path(__file__).parent
INPUT_FILE = BASE_DIR / 'inputs' / 'test_file.txt'
OUTPUT_FILE = BASE_DIR / 'outputs' / 'users.txt'

def get_user_name():
    # getpass() reads from the terminal with echo turned off, so nothing the
    # user types is displayed.
    try:
        return getpass.getpass("Enter your name: ")
    except:
        print('No name entered or name entering failed')
        return None

def save_user_name(users_name: str):
    # 'a' (append) mode adds to the end of the file instead of replacing it,
    # and still creates the file if it does not exist yet. Compare to 'w',
    # which truncates the file to empty before writing.
    # The parent directory has to exist first, so make sure of it.
    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    # write() adds no newline of its own, so add one after the name. Putting
    # it at the end (rather than before) keeps the file ending in a newline,
    # which is what lets the next run start on its own line.
    with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
        f.write(users_name + '\n')

    print(f"Appended to {OUTPUT_FILE}")
    return True

def list_users():
    user_list = []
    with open(OUTPUT_FILE, 'r') as f:
        lines = f.readlines()

    return lines
def greet_user():
    print(f"Reading from {INPUT_FILE}")

    # The `with` statement closes the file automatically, even if an error
    # is raised while reading it.
    with open(INPUT_FILE, encoding='utf-8') as f:
        lines = f.readlines()

    # readlines() keeps the trailing newline on each line, so strip it before
    # printing to avoid blank lines between them.
    for line in lines:
        print(line.rstrip())

def menu():
    user_choice = ''
    while user_choice not in ['1', 'q', 'Q']:
        user_choice = getpass.getpass(prompt='Please enter an option:\n1) Enter name in log\n2) List users\nq) Quit program\n')
        if user_choice == 'q':
            break
    return user_choice


def main():

    keep_on = True # Flag for controlling execution of program
    greet_user() # keeping this call outside loop as it is only needed once

    while keep_on: # using while loop to continue running program until exited by user
        user_choice = '' # resetting user_choice for handling logic options
        
        user_choice = menu()
        if user_choice == '1':
            users_name = get_user_name()
            print(f"Hello, {users_name}! Welcome!")
            
            save_user_name(users_name)
        
        elif user_choice == '2':
            user_list = ''
            user_list = list_users()
            print(user_list)

        elif user_choice == 'q' or user_choice == 'Q':
            print('Exiting program')
            keep_on = False
        else:
            print('Error with program. Exiting with errors...')
            keep_on = False

    return True


if __name__ == '__main__':
    main()
