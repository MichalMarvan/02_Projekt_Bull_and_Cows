import funkce as f

delka_cisla = input("Jak dlouhé čílo chcete hádat? ")
nahoda = f.random_cislo(int(delka_cisla))
print(nahoda)

pocet_cyklu = 0
while True:
  uzivatelske_cislo = input("zadejte váš tip: ")
  vysledek = f.trefa(uzivatelske_cislo, nahoda)
  pocet_cyklu += 1
  print(vysledek[0], vysledek[2], "and", vysledek[1], vysledek[3])
  if vysledek[0] == delka_cisla:
    print("-"*30, "Gratuluji, trefil jsi číslo!", "-"*30, sep="\n")
    break
    #exit()
  else:
    print("-"*35)
    continue

print("Zvládl jsi to na", pocet_cyklu, "cykly")
cykly = f.vyhodnoceni(pocet_cyklu)
print("Tvé hodnocení:", cykly
      )