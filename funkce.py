import random
from datetime import datetime

def privitani ():
    """
    Přivítání uživatele a seznámení s pravidly.
    """
    # přivítání a popsání programu
    return(print("-" * 70, "Vítám tě ve hře:".center(70), "-" * 70, 
"Bulls & Cows".center(70), "-" * 70, 
"""Hra Bulls and Cows je logická hádací hra pro dva hráče. Cílem hry 
je uhodnout tajné číslo, které je náhodně vygenerováno programem, 
pomocí postupného hádání a analýzy odpovědí ve formě "Bulls" a "Cows".""".center(70), "-" * 70, 
sep="\n"))

def cisla_random_cisla () -> list:
    """
    Vytvoření listu, který obsahuje hodnoty, ze kterých se skládá náhodné číslo.
    """
    # vytvoří list čísel od 0 do 9, šlo by zadat i samostatnym listem
    cisla = []
    for ciselny_list in range(0, 10):
        cisla.append(str(ciselny_list))
    
    return cisla

def hodnoty_pro_zadani() -> list:
    """
    Vytvoří list, který obsahuje hodnoty, které je možné zadat pro hádání. 
    """
    # hodnotou ve funkci range mohu udával jak dlouhé může být zadávané číslo
    hodnoty_pro_hadani = []

    for ciselny_list in range(3, 10):
        hodnoty_pro_hadani.append(str(ciselny_list))
        
    return (hodnoty_pro_hadani)

def random_cislo (delka_random_cisla:int) -> str:
    """
    Tato funkce vytvoří náhodné unikátní číslo, které nesmí začínat nulou
    a každé číslo je obsaženo pouze jednou.
    """
    # vytvoří list čísel od 0 do 9, šlo by zadat i samostatnym listem
    
    cisla = cisla_random_cisla ()

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

def trefa (uzivatelske_cislo:str, nahodne_cislo:str) -> list:
    """
    Funkce pro kontrolu zda zadané číslo je stejné jako náhodné číslo. 
    Vypsání bull a cow pro jednotlivé typy.
    """
    #print("uzivatelske cislo je:", uzivatelske_cislo)
    #print("nahodne cislo je", nahodne_cislo) ## KONTROLA RANDOM ČÍSLA PŘI KONTROLE KÓDU, PRO RYCHLEJŠÍ UHÁDNUTÍ ##
    
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

def vyhodnoceni (pocet_pokusu:int) -> str:
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

def cykly_celkem (pocet_cyklu:int) -> str:
    """
    Funkce pro sklonování slova cvyklus.
    """
    if pocet_cyklu == 1:
        pocet = "cyklus"
    elif pocet_cyklu in (2, 3, 4):
        pocet = "cykly"
    else:
        pocet = "cyklů"    
    return(pocet)

def zadani_hodnoty() -> list:
    """
    Funce se zeptá na hodnotu délky čísla a následně délku číslazkontoluje, zda je správně zadaná.
    """
    
    while True: 
        # zadání délky čísla uživatelem
        delka_cisla = input("Jak dlouhé čílo chcete hádat? (Můžeš zadat hodnoty od 3 do 10): ")
        # list s hodnotami, které může zadaná délka obsahovat
        kontrola = hodnoty_pro_zadani()
        # for cyklus pro kontrolu zda je zadaná délka číslo a zároven je délka v listu délek (hodnoty pro zadání)
        if delka_cisla in kontrola and delka_cisla.isdigit():
            nahodne_cislo = random_cislo(int(delka_cisla))
            print("-" * 70)
            break
        else:
            print("Zalal jsi špatnou hodnotu, zkus to znovu:")
            continue

    return(delka_cisla, nahodne_cislo)

def kontrola_zadani(uzivatelske_cislo:str) -> bool:
    """
    Funkce projde uživatelem zadané číslo a zjistí, zda se v čísle neopakují stejné hodnoty.
    """
    vysledek = []

    for cisla in uzivatelske_cislo:
        if uzivatelske_cislo.count(cisla) > 1:
            vysledek.append("Ano")
        else:
            vysledek.append("Ne")

    if "Ano" in vysledek:
        return True
    else:
        return False
    
def hlavni_vypocet() -> list:
    """
    Funkce provede halvní výpočet hry Bull and Cows.
    """
    
    # zadání délky čísla, které budeme hádat - funkce random_cislo
    zadane_hodnoty = zadani_hodnoty()   
    
    #print(nahodne_cislo)
    # spuštění stopek pro získání údaje jak dlouho uživatel hádal
    spusteni_stopek = datetime.now()

    # výpočet počtu pokusů
    pocet_cyklu = 0
    while True:
        # zadání uživatelského čísla         
        uzivatelske_cislo = input("zadejte váš tip: ")  
        
        # hlídání počtu cyků spuštění funkce while
        pocet_cyklu += 1

        # kontrola, zda se uživatel nepřepsal nebo použil dlouhé/krátké číslo, než je hádané číslo.    
        if len(uzivatelske_cislo) != int(zadane_hodnoty[0]) or uzivatelske_cislo.isdigit() == False or kontrola_zadani(uzivatelske_cislo):
            print("Číslo nemá správnou délku, nezadal jsi číslo nebo jsi zadal dvě stejná čísla.", "-" * 70, sep="\n")
            continue

        #kontrola čísla pomocí funkce trefa
        vysledek = trefa(uzivatelske_cislo, zadane_hodnoty[1])

        # vypsání funkce trefa
        print(vysledek[0], vysledek[2], "and", vysledek[1], vysledek[3])
        
        # ukončování hry, pokud počet bull bude stejný jako délka zadaného čísla
        if vysledek[0] == zadane_hodnoty[0]:
            print("-"*70, "Gratuluji, trefil jsi číslo!", "-"*70, sep="\n")
            konec_stopek = datetime.now()
            break
        else:
            print("-" * 70)
            continue

    return(spusteni_stopek, konec_stopek, pocet_cyklu)

def vypsani_vysledku(spusteni_stopek, konec_stopek, pocet_cyklu):
    """
    Funkce vypíše výsledky hry.
    """
    # vypsání výsledků
    print("Zvládl jsi to na", pocet_cyklu, cykly_celkem(pocet_cyklu))

    # vyhodnocení vytvořené pomocí funkce vyhodnocení
    cykly = vyhodnoceni(pocet_cyklu)
    print("Tvé hodnocení:", cykly)

    # zapsání času, který byl potřeba na vyřešení 
    celkovy_cas = konec_stopek - spusteni_stopek
    print("-"*70, f"Čas spuštění programu: {celkovy_cas} sekund".center(70), "-"*70, sep="\n")

def opakovani():
    """
    FFunkce pro zopakování hry.
    """
    # Zopakování programu
    print("-" * 70,"Přejete si Hru hrát znovu?", "A >>> ANO", "Cokoli jiného >>> NE", "-" * 70, sep="\n")
    znovu = input(">>> ")
    print("-" * 70)

    if znovu == "A":
        hlavni_funkce()
    else:
        print("Ukončuji Hru", "-" * 70, sep="\n")
        exit()

def hlavni_funkce():
    """
    Funkce obsahuje všechny potřebné funkce ke spuštění programu.
    """    
    spusteni_stopek, konec_stopek, pocet_cyklu = hlavni_vypocet()
    vypsani_vysledku(spusteni_stopek, konec_stopek, pocet_cyklu)
    opakovani()

if __name__ == "__main__":
    privitani ()
    hlavni_funkce()