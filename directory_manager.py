from art import text2art
import os, shutil, re
from colorama import init, Fore, Style


init(autoreset=True)

print('')
ascii_art = text2art("DirectoryManager")

def is_valid_name(name):
    invalid_symb = r'[<>:"/\\|?*]'

    if re.search(invalid_symb, name):
        return False
    return True

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_file_or_directory():
    print(f"{Fore.MAGENTA}{Style.BRIGHT}- What you want to create?{Fore.RESET}{Style.RESET_ALL}{Fore.BLUE}\n1.File\n2.Folder")
    file_or_folder = input("[1/2] >>> ")
    if file_or_folder == '1':
        print(f"{Fore.MAGENTA}{Style.BRIGHT}- Enter a name for the file you want to create:")
        name = input(">>> ") 

        if not os.path.exists(name):
            if is_valid_name(name):
                with open(name, 'w'):
                    pass
                print('')
                print(f"{Fore.GREEN}{Style.BRIGHT}- File '{name}' created")
            else:
                print(f"{Fore.RED}{Style.BRIGHT}- Invalid file name. It contains forbidden characters.")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}- File '{name}' already exists")
    elif file_or_folder == '2':
        print(f"{Fore.MAGENTA}{Style.BRIGHT}- Enter a name for the folder you want to create:")
        name = input(">>> ")
        if not os.path.exists(name):
            if is_valid_name(name):
                os.mkdir(name)
                print('')
                print(f"{Fore.GREEN}{Style.BRIGHT}- Folder '{name}' created")
            else:
                print(f"{Fore.RED}{Style.BRIGHT}- Invalid folder name. It contains forbidden characters.")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}- Folder '{name}' already exists")
    else:
        print(f"{Fore.RED}{Style.BRIGHT}Error. Incorrect input.")

def delete_file_or_directory():
    print(f"{Fore.MAGENTA}{Style.BRIGHT}- Enter name of file/directory you want to delete:")
    name = input(">>> ")
    
    try:
        if os.path.exists(name):
            print(f"{Fore.RED}{Style.BRIGHT}- Are you sure you want to delete File/Directory {Fore.MAGENTA}'{name}{Fore.RESET}' ? {Fore.RED}{Style.BRIGHT}(the contents of the folder will also be deleted)")
            choice = input("[y/n] >>> ")
            if choice.lower() == 'y':
                if os.path.isfile(name):
                    print(f'{Fore.MAGENTA}{Style.BRIGHT}Deletion...')
                    os.remove(name)
                    print(f"{Fore.GREEN}{Style.BRIGHT}File '{name}' deleted")
                elif os.path.isdir(name):
                    print(f'{Fore.MAGENTA}{Style.BRIGHT}Deletion...')
                    shutil.rmtree(name)
                    print(f"{Fore.GREEN}{Style.BRIGHT}Directory '{name}' deleted")
            else:
                print('Okay')
        else:
            print(f"{Fore.RED}{Style.BRIGHT}The name does not exist")
    except PermissionError as e:
        print(f"Error! {e}")
    except Exception as e:
        print(f"{Fore.RED}{Style.BRIGHT}An error occurred: {str(e)}")
            
def rename_file_or_folder():
    print(f"{Fore.MAGENTA}{Style.BRIGHT}- Enter name of file/directory you want to rename:")
    name = input(">>> ")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}Enter new name:")
    new_name = input(">>> ")

    if not is_valid_name(new_name):
        print(f"{Fore.RED}{Style.BRIGHT}Invalid name. It contains forbidden characters.")
        return

    try:
        if os.path.exists(name):
            os.rename(name, new_name)
            print(f"{Fore.GREEN}{Style.BRIGHT}Successfully renamed")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}'{name}' does not exist.")
    except PermissionError as e:
        print(f"Error! {e}")

def show_directory_content():
    current_directory = os.getcwd()
    items = os.listdir(current_directory)

    print('')
    for item in items:
        print(f"{Fore.BLUE} - {item}")



def main():
    clear_screen()
    print(Fore.MAGENTA + Style.BRIGHT + ascii_art)
    while True:
        print('')
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Choose action:")
        print(f"{Fore.BLUE}1. Create a new file or folder")
        print(f"{Fore.BLUE}2. Delete an existing file or folder")
        print(f"{Fore.BLUE}3. Rename a file or folder")
        print(f"{Fore.BLUE}4. Show the contents of the directory")
        print(f"{Fore.BLUE}5. Exit")

        action = input(">>> ")
        if action == '1':
            create_file_or_directory()
        elif action == '2':
            delete_file_or_directory()
        elif action == '3':
            rename_file_or_folder()
        elif action == '4':
            show_directory_content()
        elif action == '5':
            print(f"{Fore.MAGENTA}{Style.BRIGHT}Goodbye!")
            break
        else:
            print(f"{Fore.RED}Error. Incorrect input.")


if __name__ == '__main__':
    main()