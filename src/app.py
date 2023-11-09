from Auth.sign_in import SignIn
from Auth.registry import Regstry
import subprocess
import shlex

"""Cringe"""

def main():
    print(
        "Hi!\nThis is cool chat Slack 😎\n" + 
        "Please, sign in or registry in system.\n"
        )
    k = False
    while k == False:
        ans = input("Choose option S/R: ")
        if ans == "S":
            print("Enter your:")
            mail = input("mail: ")
            password = input("password: ")
            k = SignIn(mail, password).sign_in()
        elif ans == "R":
            print("Enter your:")
            mail = input("mail: ")
            password = input("password: ")
            name = input("name: ")
            age = input("age: ")
            k = Regstry(mail, password, name, age).registry()
            print("Maybe, you should try sign in?\n")
        else:
            print("\nI don't understand that...")
    print("Cool!\n")
    print("Now, do you want chating by yourself?")
    
    ans = input("Y/n: ")
    if ans == "Y":
        # process = subprocess.Popen(shlex.split("""x-terminal-emulator -e 'bash -c "./Comm/chat/server.py"'"""), stdout=subprocess.PIPE)
        # process.wait()
        # process = subprocess.Popen(shlex.split("""x-terminal-emulator -e 'bash -c "./Comm/chat/client.py"'"""), stdout=subprocess.PIPE)
        # process.wait()
        print("Sorry, doesn't work! You can start it manually")
    else:
        print("Ok")


if __name__ == "__main__":
    main()