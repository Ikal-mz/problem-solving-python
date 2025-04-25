import os

os.system('cls' if os.name == 'nt' else 'clear')

# MENGHITUNG LUAS PERSEGI PANJANG
print(f"==== MENGHITUNG LUAS PERSEGI PANJANG =====\n")

def cek_inputan(cek, tipe=float):
    while True:
        try:
            return tipe(input(cek))
        except ValueError:
            print("Inputan harus berupa angka. Ulangi lagi")
            continue

def luas_persegi_panjang(panjang,lebar):
    return panjang*lebar
    
panjang = cek_inputan("Masukan panjang persegi(cm): ")
lebar = cek_inputan("Masukan lebar persegi(cm): ")


print(f"Luas persegi panjang: {luas_persegi_panjang(panjang,lebar)} cm")
