# Bulls and Cows (Hádání čísel)

## Cíl hry:
Cílem hry je uhodnout tajné číslo, které si zvolil protihráč, pomocí postupného hádání a analýzy odpovědí ve formě "Bulls" a "Cows".

## Pravidla hry:

### Volba tajného čísla: 
- Jeden hráč (počítač) si zvolí tajné číslo, které je náhodně vygenerované. Toto číslo má pevně danou délku (například 4 číslice) a každá číslice musí být unikátní.

- Hádání: Hráč se snaží toto číslo uhodnout tím, že postupně navrhuje různé kombinace čísel.

##Hodnocení pokusů:

### Bull (býk): 
Pokud je hádaná číslice správná a na správné pozici, je to označeno jako "Bull".
### Cow (kráva): 
Pokud je hádaná číslice správná, ale na nesprávné pozici, je to označeno jako "Cow".
### Odpovědi: 
Po každém pokusu Hráče 2 Hráč 1 poskytne zpětnou vazbu v podobě počtu Bulls a Cows. 

## Například:

**Tajné číslo: 4271**
Hádání: 1234
- Odpověď: 1 Bull, 2 Cows (1 Bull za správně umístěnou číslici '2' a 2 Cows za číslice '1' a '4' na nesprávných pozicích)
- Vítězství: Hra pokračuje, dokud Hráč 2 neuhodne celé tajné číslo (tj. nezíská odpověď se 4 Bulls, pokud je délka čísla 4).

## Příklad hry:

**Tajné číslo: 5678**
Hádání 1: _1234_

Odpověď: `0 Bulls, 0 Cows`

Hádání 2: _5671_

Odpověď: `3 Bulls, 0 Cows`

Hádání 3: _5678_

Odpověď: `4 Bulls` (Hráč vyhrává)