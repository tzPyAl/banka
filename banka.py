from src.settings import app_settings, banka
from src.nav import print_izbornika, izbornik_glavni



# dobrodoslica
print("\n-----------------------------")
print(f"DOBRODOŠLI U {banka['naziv']}!!")
print("-----------------------------\n")

# start with admin login ?
while not app_settings["skip_admin_login"]:
    provided_a_usr = input("admin ime: ")
    provided_a_pass = input("admin pass: ")

    if banka["admin_users"]["username"] == provided_a_usr and banka["admin_users"]["password"] == provided_a_pass:
        print(f"\nPristup dozvoljen. Dobrodošao {provided_a_usr.upper()}!\n\n")
        app_settings["skip_admin_login"] = True
    else:
        print("Neispravni podaci. Pristup nedozvoljen.\n")

# admin access granted
print_izbornika(izbornik_glavni)
