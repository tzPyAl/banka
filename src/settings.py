## START_UP
# capitalize ime, prezime & tvrtka
korisnici_u_bazi = [{'id': 0, 'ime': 'Pero', 'prezime': 'Peric', 'tvrtka': '', 'pin': '1111', 'stanje': 8821, 'iban': 'PY4419110031001550276520'}, {'id': 1, 'ime': 'Marko', 'prezime': 'Marko', 'tvrtka': 'Mirko', 'pin': '2222', 'stanje': 535, 'iban': 'PY4419110031002392572352'}]

## SETTINGS
banka = {
    "naziv": "Python Bank",
    "valuta": "euro",
    "simbol_valute": "€",
    "iban_hardcoded": "PY441911003100",
    "iban_user_lenght": 10,
    "admin_users": {
        "username": "admin",
        "password": "test1234"
    }
}

app_settings = {
    "skip_admin_login": False,
    "dozvoljeno_prekoracenje": -1000,
    "kamata_na_stednju": 0.0000001
}

transaction_history = []