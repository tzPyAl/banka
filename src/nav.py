from .settings import korisnici_u_bazi, banka, app_settings
from .korisnici import Korisnici

korisnik_trenutni = 0

izbornik_pretraga = {
    0: "Pretraga po imenu",
    1: "Pretraga po prezimenu",
    2: "Pretraga po tvrtci",
    3: "Povratak na glavni izbornik"
}

izbornik_glavni = {
    0: "Kreiranje novog korisnika",
    1: "Postojeci korisnik",
    2: "Izlaz iz aplikacije"
}

izbornik_korisnik = {
    0: "Otvaranje računa tvrtke",
    1: "Prikaz stanja računa",
    2: "Prikaz prometa po računu",
    3: "Polog novca na račun",
    4: "Podizanje novca s računa",
    5: "Povratak na glavni izbornik"
}


def railroader(value):
    match value:
        case "Otvaranje računa tvrtke":
            kreiranje_novog_korisnika()
        case "Prikaz stanja računa":
            stanje_na_racunu()
        case "Prikaz prometa po računu":
            print("Prikaz prometa po računu")
        case "Polog novca na račun":
            polog_na_racun(vrsta_transakcije="polog")
        case "Podizanje novca s računa":
            polog_na_racun(vrsta_transakcije="podizanje")
        case "Povratak na glavni izbornik":
            print_izbornika(izbornik_glavni)
        case "Kreiranje novog korisnika":
            kreiranje_novog_korisnika()
        case "Postojeci korisnik":
            pretraga_korisnika()
        case "Izlaz iz aplikacije":
            import sys
            sys.exit("Hvala na korištenju.\n")
        case "Pretraga po imenu":
            return "ime"
        case "Pretraga po prezimenu":
            return "prezime"
        case "Pretraga po tvrtci":
            return "tvrtka"


def print_izbornika(izbornik):
    global korisnik_trenutni, korisnici_u_bazi

    if izbornik == izbornik_korisnik:
        print("\n\n************************")
        print(f"Pregled korisnika {korisnici_u_bazi[korisnik_trenutni]['ime']} {korisnici_u_bazi[korisnik_trenutni]['prezime']}, {korisnici_u_bazi[korisnik_trenutni]['tvrtka']}")
        print("************************\n")

    for key,value in izbornik.items():
        print(f"{key}: {value}")
    try:
        izbor = int(input("\nOdaberi radnju: "))
    except:
        print("Potrebno je unijeti broj izbora!\n")
        print_izbornika(izbornik)
    else:
        if izbor > len(izbornik)-1 or izbor < 0:
            print(f"Nepostojeci izbor. Unsesi broj izmedju 0 i {len(izbornik)-1}\n")
            print_izbornika(izbornik)
        else:
            return railroader(izbornik[izbor])


def kreiranje_novog_korisnika():
    global korisnik_trenutni, korisnici_u_bazi

    print("\n\n************************")
    print("Forma za kreiranje novog korisnika\n")
    ime = obavezan_unos(input("Ime korisnika: ")).capitalize()
    prezime = obavezan_unos(input("Prezime korisnika: ")).capitalize()
    tvrtka = input("Naziv tvrtke: ").capitalize()

    pin_potvrdjen = False
    while not pin_potvrdjen:
        pin_1 = obavezan_unos(input("Unesi PIN: "))
        pin_2 = obavezan_unos(input("Potvrdi PIN: "))

        if pin_1 == pin_2:
            pin_potvrdjen = True
        else:
            print("\n????\nPinovi moraju biti identicni. Pokušaj ponovno\n????\n")

    # "baza" koja traje dok se izvrsava app
    novi_id = len(korisnici_u_bazi) # ovo je pozicija za novog korisnika u listi
    korisnik_trenutni = novi_id # spremi poziciju trenutnog korisnika

    tmp = Korisnici(id=novi_id, ime=ime, prezime=prezime, tvrtka=tvrtka, pin=pin_1)
    # spremi u "bazu" korisnika
    korisnici_u_bazi.append(tmp.__dict__)

    # posalji me na izbornik ovog korisnika
    print_izbornika(izbornik_korisnik)

def obavezan_unos(value=""):
    while not value:
        value = input("Unos je obavezan, Ponovi: ")
    return value

def pretraga_korisnika():
    global korisnik_trenutni, korisnici_u_bazi
    izbor_pretrage = print_izbornika(izbornik_pretraga)
    
    keyword = input(f"\nUnesi {izbor_pretrage} za pretragu: ").capitalize()
    keyword_index = next((index for (index, d) in enumerate(korisnici_u_bazi) if d[izbor_pretrage] == keyword), None)
    
    if keyword_index == None:
        print(f"Nazalost, {izbor_pretrage} '{keyword}' ne postoji u bazi")
        pretraga_korisnika()
    else:
        print(f"\nKorisnik {izbor_pretrage}: '{keyword}' pronadjen.")

        # udji u korisnički meni
        korisnik_trenutni = keyword_index
        print_izbornika(izbornik_korisnik)

def stanje_na_racunu():
    print(f"Stanje na racunu: {banka['simbol_valute']}{korisnici_u_bazi[korisnik_trenutni]['stanje']}")
    print_izbornika(izbornik_korisnik)

def polog_na_racun(vrsta_transakcije):
    trenutno = int(korisnici_u_bazi[korisnik_trenutni]['stanje'])
    print(f"Trenutno stanje racuna: {banka['simbol_valute']}{trenutno}")

    ispravan_unos = False
    while not ispravan_unos:
        try:
            iznos_pologa = int(input(f"\nOdaberite iznos {banka['simbol_valute']}"))
        except ValueError:
            print("Unos mora biti brojcani.")
        else:
            ispravan_unos = True
            if vrsta_transakcije == "polog":
                novo_stanje = trenutno - iznos_pologa
            elif vrsta_transakcije == "podizanje":
                novo_stanje = trenutno - iznos_pologa
                if novo_stanje <= app_settings['dozvoljeno_prekoracenje']:
                    print(f"Transakcija odbijena! Stanje na racunu {banka['simbol_valute']}{novo_stanje} prelazi maksimalno dozvoljeno prekoracenje od {banka['simbol_valute']}{app_settings['dozvoljeno_prekoracenje']}")
                    ispravan_unos = False

    korisnici_u_bazi[korisnik_trenutni]['stanje'] = novo_stanje
    print(f"\nUspjesno izvrseno. Novo stanje računa: {banka['simbol_valute']}{novo_stanje}")
    print_izbornika(izbornik_korisnik)
