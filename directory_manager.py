from art import text2art
import os, shutil, re
from colorama import init, Fore


init(autoreset=True)

print('')
ascii_art = text2art("DirectoryManager")

def create_file_or_directory():
    print(f"{Fore.CYAN}What you want to create?\n1.File\n2.Folder")
    file_or_folder = input(f"{Fore.YELLOW}[1/2] >>> ")
    if file_or_folder == '1':
        print(f"{Fore.CYAN}Enter a name for the file you want to create:")
        name = input(f"{Fore.YELLOW}>>> ") 

        if not os.path.exists(name):
            with open(name, 'w'):
                pass
            print(f"{Fore.YELLOW} File '{name}' created")
        else:
            print(f"{Fore.YELLOW}File '{name}' already exists")
    elif file_or_folder == '2':
        print(f"{Fore.CYAN}Enter a name for the folder you want to create:")
        name = input(f"{Fore.YELLOW}>>> ")
        if not os.path.exists(name):
            os.mkdir(name)
            print(f"{Fore.YELLOW}Folder '{name}' created")
        else:
            print(f"{Fore.YELLOW}Folder '{name}' already exists")
    else:
        print(f"{Fore.RED}Error. Icorrect input.")

def delete_file_or_directory():
    print(f"{Fore.CYAN}Enter name of file/directory you want to delete:")
    name = input(f"{Fore.YELLOW}>>> ")
    
    try:
        if os.path.exists(name):
            print(f"{Fore.RED}Are you sure you want to delete File/Directory {Fore.YELLOW}'{name}{Fore.RESET}' ? (this operation is irreversible)")
            choice = input(f"{Fore.YELLOW}[y/n] >>> ")
            if choice.lower() == 'y':
                if os.path.isfile(name):
                    print('Deletion...')
                    os.remove(name)
                    print(f"{Fore.YELLOW}File '{name}' deleted")
                elif os.path.isdir(name):
                    print('Deletion...')
                    shutil.rmtree(name)
                    print(f"{Fore.YELLOW}Directory '{name}' deleted")
            else:
                print('Okay')
        else:
            print(f"{Fore.RED}The name does not exists")
    except PermissionError as e:
        print(f"Error! {e}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {str(e)}")
            
def rename_file_or_folder():
    print(f"{Fore.CYAN}Enter name of file/directory you want to rename:")
    name = input(f"{Fore.YELLOW}>>> ")
    print(f"{Fore.CYAN}Enter new name:")
    new_name = input(f"{Fore.CYAN}>>> ")
    try:
        if os.path.exists(name):
            os.rename(name, new_name)
            print(f"{Fore.YELLOW} Successfully renamed")
        else:
            print(f"{Fore.RED}'{name}' does not exists.")
    except PermissionError as e:
        print(f"Error! {e}")

def main():
    print(Fore.CYAN + ascii_art)
    while True:
        print(f"""{Fore.CYAN}Choose action:
1. Create a new file or folder (you will be asked for a name)
2. Delete an existing file or folder (be careful, this action is irreversible)
3. Rename a file or folder (you will need to provide the current name and new name)
4. Exit""")
        action = input(f"{Fore.YELLOW}>>> ")
        if action == '1':
            create_file_or_directory()
        elif action == '2':
            delete_file_or_directory()
        elif action == '3':
            rename_file_or_folder()
        elif action == '4':
            break
        else:
            print(f"{Fore.RED}Error. Incorrect input.")


if __name__ == '__main__':
    main()