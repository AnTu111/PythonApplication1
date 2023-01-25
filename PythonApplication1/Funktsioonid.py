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


