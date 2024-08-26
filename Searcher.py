import os
from marshal import dumps
from binascii import hexlify
from random import randint, shuffle
import time

from pystyle import *
 
os.system('cls')
System.Size(150, 40)



Box = r'''
 ________________________________________
|                                        |
| Bienvenue dans le Searcher DB by NVME  |
|________________________________________|
'''

banner1 = r'''
  ██████ ▓█████ ▄▄▄       ██▀███   ▄████▄   ██░ ██ ▓█████  ██▀███     ▓█████▄  ▄▄▄▄   
▒██    ▒ ▓█   ▀▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒   ▒██▀ ██▌▓█████▄ 
░ ▓██▄   ▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒██▀▀██░▒███   ▓██ ░▄█ ▒   ░██   █▌▒██▒ ▄██
  ▒   ██▒▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄     ░▓█▄   ▌▒██░█▀  
▒██████▒▒░▒████▒▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▓█▒░██▓░▒████▒░██▓ ▒██▒   ░▒████▓ ░▓█  ▀█▓
▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░    ▒▒▓  ▒ ░▒▓███▀▒
░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░    ░ ▒  ▒ ▒░▒   ░ 
░  ░  ░     ░    ░   ▒     ░░   ░ ░         ░  ░░ ░   ░     ░░   ░     ░ ░  ░  ░    ░ 
      ░     ░  ░     ░  ░   ░     ░ ░       ░  ░  ░   ░  ░   ░           ░     ░      
                                  ░                                    ░            ░ '''

banner2 = r'''
'''

banner = Add.Add(banner1, banner2, center=True)


purple = Col.StaticMIX([Col.blue, Col.purple])

def search_files(search_term, database_folder, max_results=10):
    results = []
    results_found = 0
    for root, _, files in os.walk(database_folder):
        if results_found >= max_results:
            break
        for file in files:
            if file.endswith(('.txt', '.csv', '.sql', '.json')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', errors='ignore') as f:
                    lines = f.readlines()
                    for index, line in enumerate(lines):
                        if results_found >= max_results:
                            break
                        if search_term in line:
                            result_str = f'{line.strip()}'
                            results.append(result_str)
                            results_found += 1
    return results

def main():
    database_folder = r""



    
    print(Colorate.Vertical(Colors.black_to_white,"      "))
    print(Colorate.Vertical(Colors.black_to_white,"          "))
    print(Colorate.Vertical(Colors.black_to_white,"           "))
from pystyle import Colorate, Colors

os.system('cls')

def search_files(search_term, database_folder, max_results=10):
    results = []
    results_found = 0
    for root, _, files in os.walk(database_folder):
        if results_found >= max_results:
            break
        for file in files:
            if file.endswith(('.txt', '.csv', '.sql')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', errors='ignore') as f:
                    lines = f.readlines()
                    for index, line in enumerate(lines):
                        if results_found >= max_results:
                            break
                        if search_term in line:
                            result_str = f'{line.strip()}'
                            results.append(result_str)
                            results_found += 1
    return results

def main():









    System.Size(150, 40)
System.Title("Searcher DB")
Cursor.ShowCursor()
print()
print(Colorate.Vertical(Colors.green_to_blue, Center.XCenter(banner + '\n\n')))
print(Colorate.Diagonal(Colors.green_to_blue, Center.XCenter(Box + '\n\n')))

term = input(Colorate.Horizontal(Colors.green_to_blue, "[?] Mettez ici l'email ou le pseudo de la personne recherchée -> "))
print('\n')
Write.Print(f"[...] Searcher DB est en train de rechercher dans vos db veuillez patienter.\n\n", Colors.blue_to_green, interval=0.05)

database_folder = r""
while term.lower() != 'q':
        results = search_files(term, database_folder)

        if results:
            Write.Print(f"[+] Searcher DB à trouver des résultats dans vos db.\n\n", Colors.green, interval=0.05)
            for result in results:
                print(Colors.purple ,'[ + | Result ] ' + result)
                
                # Spécifiez le chemin du dossier
            dossier = r""

            # Vérifiez si le dossier existe, sinon créez-le
            if not os.path.exists(dossier):
                os.makedirs(dossier)

            # Maintenant vous pouvez enregistrer le fichier dans ce dossier
            chemin_fichier = os.path.join(dossier, "resultats.txt")
            dossier1 = ('resultats.txt')
            # Exemple pour enregistrer un texte
            with open(chemin_fichier, 'w') as fichier:
                fichier.write("\n".join(results))

            Write.Print(f"\n\n[-] Fichier enregistré dans {chemin_fichier}\n", Colors.dark_green, interval=0.05)
            Write.Print(f"[!] Le Searcher DB redémarre dans 1 minute, regardez le dossier {dossier1} il y a les résultats.\n", Colors.red, interval=0.05)
            time.sleep(60)
            os.system('cls')
            System.Size(150, 40)
            System.Title("Searcher DB")
            Cursor.ShowCursor()
            print()
            print(Colorate.Vertical(Colors.green_to_blue, Center.XCenter(banner + '\n\n')))
            print(Colorate.Diagonal(Colors.green_to_blue, Center.XCenter(Box + '\n\n')))


        else:
            Write.Print(f"[!] Searcher DB n'a pas pu trouver les informations dans les DB.\n", Colors.red, interval=0.05)
            Write.Print(f"[!] Le Searcher DB redémarre dans 5 secondes.\n", Colors.red, interval=0.05)
            time.sleep(5)
            os.system('cls')
            System.Size(150, 40)
            System.Title("Searcher DB")
            Cursor.ShowCursor()
            print()
            print(Colorate.Vertical(Colors.green_to_blue, Center.XCenter(banner + '\n\n')))
            print(Colorate.Diagonal(Colors.green_to_blue, Center.XCenter(Box + '\n\n')))
            
        term = input(Colorate.Horizontal(Colors.green_to_blue, "[?] Mettez ici l'email ou le pseudo de la personne recherchée -> "))
        Write.Print(f"[...] Searcher DB est en train de rechercher dans vos db veuillez patienter.\n\n", Colors.blue_to_green, interval=0.05)


if __name__ == "__main__":
    (main)