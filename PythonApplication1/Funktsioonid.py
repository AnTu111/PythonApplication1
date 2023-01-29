from datetime import*


def arithmetic(a1: float, sym: str, a2: float) -> any:
    """Lihtne kalkulaator
    +  liitmine, - lahutamine, * korrutamine,/ jagamine
    :param float a1: Esimene arv
    :param float a2: Teine arv
    :param str sym: Tehe
    :rtype: var Määramata tüüp
    """
    if sym in ["+", "-", "/", "*"]:
        if sym == "/" and a2 == 0:
            vas = "Div/0"
        else:
            vas = eval(str(a1) + sym + str(a2))
    else:
        vas = "Tundmatu tehe!"
    return vas


def is_year_leap(a1: str) -> str:
    """Liigaasta kalkulaator
    Args:
        a1 (int): year
    Returns:
        str:True/Fals
    """
    return a1 % 4 == 0


def season(x: int) -> str:
    """Aasta periood
        Args:
            x (int): numbers (1-12)
        Returns:
            str:[talv, kevad, suvi, sügis]
        """
    if x in range(1, 13):
        if x in range(3, 6):
            vastus = "kevad"
        elif x in range(6, 9):
            vastus = "suvi"
        elif x in range(9, 12):
            vastus = "sugis"
        else:
            vastus = "talv"
    else:
        "Vele number!"
    return vastus


def bank(money: float, years: int) -> float:
    """Panga prosent
    Args:
        money (float): alg summa
        yeras(int): aastad
    Returns:
        lõppsumma (str): lõpsumma
    """
    summa = money * (1 + 0.1) ** years
    return round(summa)


def is_prime(number: int) -> str:
    """Kontroll True or False
    Args:
        number(int): number 1 - 1000
    Returns:
        bool (str): True or False
    """
    while number <= 1000:
        while number >= 0:
            return number % 2 == 0



def date(day:int,month:int,year:int) -> str:
    """Kontrolli kas kuupäev on eksisteerib?
    Args:
        number(int): kuupäev
        number(int): kuu
        number(int): aasta
    Returns:
        bool (str): True or False
    """
    try:
        if datetime(year, month, day):
            answer = True
        else:
            answer = False
    except:
        answer = "Vale!"
    return answer



def XOR_cipher(code:str, psw:int) -> str:
    """XOR kodeerimine
    Args:
        code (str):  sona
        psw (int):  parool
    Returns:
        str: kodeeritud sona
    """
    encrypt_str = ' '
    for i in code:
        encrypt_str += chr(ord(i) ^ int(psw))
    return encrypt_str




def XOR_uncipher(code:str, psw:int) -> str:
    """XOR dekodeerimine
        Args:
            code (str):  sona
            psw (int):  parool
        Returns:
            str: dekodeeritud sona
    """

    uncripted = ''
    for symbol in code:
        uncripted += chr(ord(symbol) ^ psw)
    return uncripted