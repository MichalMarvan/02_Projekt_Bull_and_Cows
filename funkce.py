import random
def random_cislo (cislo):

  cisla = []
  for ciselny_list in range(0, 10):
    cisla.append(str(ciselny_list))
  
  n = 0
  vysledek = []
  while n < cislo:
    nahodne_cislo = random.choice(cisla)
    if n == 0 and nahodne_cislo == "0":
      n = 0
      continue
    elif nahodne_cislo in cisla:
      vysledek.append(nahodne_cislo)
      cisla.remove(nahodne_cislo)   
      n += 1
  
  celek = "".join(vysledek)
  return(celek)