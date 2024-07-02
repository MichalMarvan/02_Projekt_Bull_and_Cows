import random
def random_cislo (cislo:int):

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

def trefa (uzivatelske_cislo:str, nahoda:str): # -> str
  i = 0
  pocet_bull = 0
  pocet_cow = 0
  for cisla in uzivatelske_cislo:
    if cisla == nahoda[i]:
      pocet_bull +=1
    elif cisla in nahoda:
      pocet_cow +=1
    i += 1

  if pocet_bull in (0, 1):
    a = "bull"
  else:
    a = "bulls"

  if pocet_cow in (0, 1):
    b = "cow"
  else:
    b = "cows"
  
  return([str(pocet_bull), str(pocet_cow), a, b])

def vyhodnoceni (vyhodnoceni):
  if vyhodnoceni == 1:
    co = "neuvěřitelné, máš velkou kliku"
  elif vyhodnoceni in (2, 3):
    co = "neskutečný počin"
  elif vyhodnoceni in (4, 5):
    co = "docela dobré"
  elif vyhodnoceni in (5, 6):
    co = "mohlo to být lepší"
  else:
    co = "slabota"
  return(co)