import random

def random_cislo (delka_random_cisla:int): # -> str
    """
    Tato funkce vytvoří náhodné unikátní číslo, které nesmí začínat nulou
    a každé číslo je obsaženo pouze jednou.
    """
    # vytvoří list čísel od 0 do 9, šlo by zadat i samostatnym listem
    cisla = []
    for ciselny_list in range(0, 10):
        cisla.append(str(ciselny_list))
    # vytvoření listu náhodných čísel, počet je dán zadanou délkou čísla
    n = 0
    vysledek = []

    while n < delka_random_cisla:
        nahodne_cislo = random.choice(cisla)
        # podmínka k odstranění 0 z prvního místa
        if n == 0 and nahodne_cislo == "0":
            n = 0
            continue
        # vytvoření listu s náíhodnými čísly
        elif nahodne_cislo in cisla:
            vysledek.append(nahodne_cislo)
            cisla.remove(nahodne_cislo)   
            n += 1
    # předělání listu s jednotlivými čísly na jedno číslo
    celek = "".join(vysledek)
    return(celek)

def trefa (uzivatelske_cislo:str, nahodne_cislo:str): # -> list
    """
    Funkce pro kontrolu zda zadané číslo je stejné jako náhodné číslo. 
    Vypsání bull a cow pro jednotlivé typy.
    """
    print(uzivatelske_cislo)
    print(nahodne_cislo)
    # potřebné zadání pro for cyklus   
    i = 0
    pocet_bull = 0
    pocet_cow = 0
    # počty bull/cow
    for cisla in uzivatelske_cislo:
        if cisla == nahodne_cislo[i]:
            pocet_bull +=1
        elif cisla in nahodne_cislo:
            pocet_cow +=1
        i += 1
    # rozdělení jednotného a množného čísla pro bull
    if pocet_bull in (0, 1):
        bull = "bull"
    else:
        bull = "bulls"
    # rozdělení jednotného a množného čísla pro cow    
    if pocet_cow in (0, 1):
        cow = "cow"
    else:
        cow = "cows"
    
    return([str(pocet_bull), str(pocet_cow), bull, cow])

def vyhodnoceni (pocet_pokusu:int): # -> str
    """
    Funkce pro vypsání vyhodnocení výsledků podle počtu pokusů.
    """
    # vyhodnocení dle počtu pokusů a vypsání stringu jako hodnocení pokusu
    if pocet_pokusu == 1:
        vyhodnoceni_vysledku = "Neuvěřitelné, máš velké štěsté!"
    elif pocet_pokusu in (2, 3):
        vyhodnoceni_vysledku = "Neskutečný počin."
    elif pocet_pokusu in (4, 5):
        vyhodnoceni_vysledku = "Docela dobré."
    elif pocet_pokusu in (5, 6):
        vyhodnoceni_vysledku = "Mohlo to být lepší."
    else:
        vyhodnoceni_vysledku = "Slabota, máš na víc!"

    return(vyhodnoceni_vysledku)

def pocet_cyklu (pocet_cyklu:int): #-> str
    if pocet_cyklu == 1:
        pocet = "cyklus"
    elif pocet_cyklu in (2, 3, 4):
        pocet = "cykly"
    else:
        pocet = "cyklů"
    
    return(pocet)
