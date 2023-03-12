from random import randint
from .settings import banka

class Korisnici:
    def __init__(self, id, ime, prezime, pin, tvrtka=None):
        self.id = id
        self.ime = ime.capitalize()
        self.prezime = prezime.capitalize()
        self.tvrtka = tvrtka
        self.pin = pin
        self.stanje = 0
        self.iban = self.generiraj_iban()

        print("\nKorisnik upjesno kreiran!\n")
        self.print_korisnika()

    def generiraj_iban(self):
        iban = banka["iban_hardcoded"]
        iban_user_numbers = randint(10**(banka["iban_user_lenght"]-1), (10**banka["iban_user_lenght"])-1)
        return (iban + str(iban_user_numbers))
    
    def print_korisnika(self):
        print("************************")
        print(f"ID korisnika: {self.id}\nIme: {self.ime}\nTvrtka: {self.tvrtka}\nIBAN: {self.iban}\nStanje na racunu: {self.stanje}\nPIN: {self.skriveni_pin()}")
        print("************************")

    def skriveni_pin(self):
        # # mora bit bolji nacin
        # hidden = ""
        # for i in range(len(self.pin)):
        #     hidden = hidden + "*"
        # return hidden
        return '*'*len(self.pin)
    