from random import *
from sys import *


username_list = ["user1", "user2", "user3"]
psw_list = ["psw1", "psw2", "psw3"]


def password_generation(number_of_initials: int) -> float:
    """Parooli isegenereerimine
    Args:
        number_of_initials (int): _sümbolite arv_
    Returns:
        _type_(int): _tagastab uus parrol_
    """

    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0 + str1 + str2 + str3
    ls = list(str4)
    shuffle(ls)
    psword = ''.join([choice(ls) for x in range(number_of_initials)])
    print("Yours generated password is: ", psword)
    return psword



def choises():
    """Funktsioon annab  valik:  sisseloogida voi registreeruda
    Args:

    Returns:
    """
    print("Hello! Palun sisselogida või registreeru")
    while True:
        try:
            choose = str(input("\nUue konto registreerumine   - 1,\nSisseloogimine  -  2,"
                              "Välja -   -  3\n "))
        except:
            print("Sistage numbri")
        if str(choose) == "2":
            user_login()
        elif str(choose) == "1":
            user_registration()
            user_login()
        elif str(choose) == "3":
            exit()



def user_registration() -> any:
    """Kasutaja loob endale uus konto.
    Args:

    Returns:
        _type_(any): tagastab password
    """
    username = input("Please, enter a new username \n")
    while username in username_list:
        print("This username in used! Please, choose the other one!")
        username = input("Please, enter a new username\n")
    else:
        username_list.append(username)
    salasona = input("If you want to generate password - enter number 1,\nif you want to use your password - enter "
                     "number" "2.\n")
    if salasona == "1":
        try:
            num = int(input("Enter the initials amount --> "))
        except:
            print("You must enter a number!")
        psw_list.append(password_generation(num))
    elif salasona == "2":
        password = input("Enter new password \n")
        while password_control(password) == False:
            password = input("Enter new password \n")
        if password_control(password) == True:
            psw_list.append(str(password))
            print("\nYours new password is: ", str(password))
    return psw_list



def user_login():
    """Funktsioon teeb sisselogimis protsessi
     Args:

    Returns:
    """
    username = input("Hello!Sisesta username")
    try:
        if username in username_list:
            a = username_list.index(username)
            for i in range(2):
                password = input(f"Dear,{username}!\nEnter the password\n")
                if password == psw_list[a]:

                    print("\nLog in succesfully!")
                    break
                else:
                    print("\nWrong password!", (1 + i))
        else:
            for i in range(3):
                print("\nVale username!")
                username = input("Enter the correct username\n")
                if username in username_list:
                    a = username_list.index(username)
                    break
                else:
                    print("\nIncorrect! Append:", i + 1)
                    if i == 3:
                        break
    except:
        print("Viga!")


def password_control(password: str):
    """Kontrollib salasona.
    Args:
        password (str): _salasona mis paneb ise kasutaja_
    Returns:
        _type_: return True or False.
    """



    num = len(password)
    a = 0

    for i in range(num):
        if password[i].isdigit() or password[i].isupper() or password[i].isalpha():
            a += 1
        else:
            print("Parool on vale reeglid ei järgi")
            return False
    if a > 0:
        return True
    else:
        print("Parool on vale reeglid ei järgi")
        return False
