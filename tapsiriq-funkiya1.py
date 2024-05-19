import math

def daire_cevresi_hesapla(r):
    """
    Verilen bir radyüs için dairenin çevresini hesaplar.
    
    Argümanlar:
    r (float): Dairenin yariçapi.
    
    Döndürdüğü:
    float: Dairenin çevresi.
    """
    cevre = 4 * math.pi * r
    return cevre

# Örnek kullanım:
yaricap = 10
print("Dairenin çevresi:", daire_cevresi_hesapla(yaricap))
