import time
import random
from colorama import Fore, Back, Style

print(Fore.LIGHTWHITE_EX + "Üdvözöllek a játékban!")
time.sleep(2)
print("\n")
print("A játék során egy véletlenszerű számot fogok generálni 1 és 100 között!")
print("\n")
time.sleep(2)
print("Ezt a számot különböző műveletekkel fogod módosítani!")
print("\n")
time.sleep(2)
print("A műveletek sorrendje: szorzás, összeadás, osztás, kivonás!")
print("\n")
time.sleep(2)
print("A műveleteket végezd el a megadott sorrendben!")
print("\n")
time.sleep(2)
print("A végeredményt 1 tizedesjegyre kerekítsd!")

number = random.randint(1, 100)
szorzas = random.randint(1, 5)
osztas = random.randint(1, 5)
osszeadas = random.randint(1, 20)
kivonas = random.randint(1,  20)

print(f"{number}  <--- Ezzel a számmal végezd el a műveleteket!")
time.sleep(2)
print(Fore.CYAN + f"Szorozd meg: {szorzas}")
time.sleep(2)
print(f"Adjál hozzá: {osszeadas}")
time.sleep(2)
print(f"Oszd el: {osztas}")
time.sleep(2)
print(f"Vonjál ki belőle: {kivonas}")

eredmeny = float(input(Fore.LIGHTRED_EX + "Az eredmény: "))
szamolo = float((number * szorzas + osszeadas) / osztas - kivonas)
szamolo = round(szamolo, 2)

if szamolo == eredmeny:
    print(Fore.RESET + "Gratulálok, helyes!")
else:
    print(Fore.RESET + "Sajnos nem sikerült!")
    print(f"A helyes eredmény: {szamolo}")