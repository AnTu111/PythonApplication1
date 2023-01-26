def arithmetic(a1:float,sym:str,a2:float)->any:
    """Lihtne kalkulaator
    +  liitmine, - lahutamine, * korrutamine,/ jagamine
    :param float a1: Esimene arv
    :param float a2: Teine arv
    :param str sym: Tehe
    :rtype: var Määramata tüüp
    """
    if sym in ["+","-","/","*"]:
        if sym=="/" and a2==0:
            vas="Div/0"
        else:
            vas=eval(str(a1)+sym+str(a2))
    else:
        vas="Tundmatu tehe!"
    return vas


def is_year_leap(a1:str)->str:
    """Liigaasta kalkulaator
    Args:
        a1 (int): year
    Returns:
        str:True/Fals
    """
    return a1 % 4 ==0



def season(x:int)->str:
    """Aasta periood
        Args:
            x (int): numbers (1-12)
        Returns:
            str:[talv, kevad, suvi, sügis]
        """
    if x in range(1,13):
        if x in range(3,6):
            vastus = "kevad"
        elif x in range(6,9):
            vastus = "suvi"
        elif x in range(9,12):
            vastus = "sugis"
        else:
            vastus = "talv"
    else:
        "Vele number!"
    return vastus



def bank(money:float,years:int)->float:
    """Panga prosent
    Args:
        money (float): alg summa
        yeras(int): aastad
    Returns:
        lõppsumma (str): lõpsumma
    """
    summa = money*(1+0.1*years)
    return summa