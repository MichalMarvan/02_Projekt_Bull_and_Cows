import funkce as f
from datetime import datetime

"""
main.py: druhý projekt do Engeto Online Python Akademie
author: Michal Marvan
email: marvan.michal@gmail.com
discord: Michal_M
"""

# přivítání a popsání programu
print("-" * 50, "Vítám tě ve hře:".center(50), "-" * 50, 
"Bulls & Cows".center(50), "-" * 50, 
"""Hra Bulls and Cows je logická hádací hra pro dva 
hráče. Cílem hry je uhodnout tajné číslo, které je 
náhodně vygenerováno programem, pomocí postupného 
hádání a analýzy odpovědí ve formě "Bulls" a "Cows".""".center(50), "-" * 50, 
sep="\n")

# zadání délky čísla, které budeme hádat - funkce random_cislo
delka_cisla = input("Jak dlouhé čílo chcete hádat? ")
nahodne_cislo = f.random_cislo(int(delka_cisla))
print("-" * 50)

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
    if len(uzivatelske_cislo) != int(delka_cisla) or uzivatelske_cislo.isdigit() == False :
        print("Číslo nemá správnou délku nebo jsi nezadal číslo.", "-" * 50, sep="\n")
        continue

    #kontrola čísla pomocí funkce trefa
    vysledek = f.trefa(uzivatelske_cislo, nahodne_cislo)

    # vypsání funkce trefa
    print(vysledek[0], vysledek[2], "and", vysledek[1], vysledek[3])
    
    # ukončování hry, pokud počet bull bude stejný jako délka zadaného čísla
    if vysledek[0] == delka_cisla:
        print("-"*50, "Gratuluji, trefil jsi číslo!", "-"*50, sep="\n")
        konec_stopek = datetime.now()
        break
    else:
        print("-" * 50)
        continue

# vypsání výsledků
print("Zvládl jsi to na", pocet_cyklu, f.pocet_cyklu(pocet_cyklu))

# vyhodnocení vytvořené pomocí funkce vyhodnocení
cykly = f.vyhodnoceni(pocet_cyklu)
print("Tvé hodnocení:", cykly)

# zapsání času, který byl potřeba na vyřešení 
celkovy_cas = konec_stopek - spusteni_stopek
print("-"*50, f"Čas spuštění programu: {celkovy_cas} sekund".center(50), "-"*50, sep="\n")