import os

os.system('cls' if os.name == 'nt' else 'clear')

# MENGHITUNG LUAS PERSEGI
print(f"==== MENGHITUNG LUAS PERSEGI =====\n")

def luas_persegi(sisi):
    return sisi*sisi

sisi = float(input("Masukan panjang sisi (cm): "))
print(f"Luas persegi: {luas_persegi(sisi)}cm")