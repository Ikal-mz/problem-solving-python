import os

os.system('cls' if os.name == 'nt' else 'clear')

print(f"\n==== KONVERSI SUHU =====\n")
print("=== Pilih Suhu Yang Ingin Di Masukan ===")
print("1. Celcius")
print("2. Fahrenheit")
print("3. Kelvin")
print("4. Reamur")

while True:
    inputanAwal = input("Pilih suhu awal (1/2/3/4): ")
    if inputanAwal.isdigit() and 0 < int(inputanAwal) < 5:
        inputanAwal = int(inputanAwal)
        break
    else:
        print("Inputan salah !")

if inputanAwal == 1:
    print("\n=== Mau Konversi Ke ===")
    print("1. Fahrenheit")
    print("2. Kelvin")
    print("3. Reamur")
elif inputanAwal == 2:
    print("\n=== Mau Konversi Ke ===")
    print("1. Celcius")
    print("2. Kelvin")
    print("3. Reamur")
elif inputanAwal == 3:
    print("\n=== Mau Konversi Ke ===")
    print("1. Celcius")
    print("2. Fahrenheit")
    print("3. Reamur")
elif inputanAwal == 4:
    print("\n=== Mau Konversi Ke ===")
    print("1. Celcius")
    print("2. Fahrenheit")
    print("3. Kelvin")


while True:
    inputanAkhir = input("Pilih konversi (1/2/3): ")
    if inputanAkhir.isdigit() and 0 < int(inputanAkhir) < 4:
        inputanAkhir = int(inputanAkhir)
        break
    else:
        print("Konversi salah !")

nilai = float(input("Masukan nilai: "))

def celcius(nilai):
    if inputanAwal == 1:
        if inputanAkhir == 1:
            farh = nilai * (9/5) + 32
            print(f"Konversi celcius ke fahrenheit : {farh:.2f}")
        elif inputanAkhir == 2:
            kelv = nilai + 273.15
            print(f"Konversi celcius ke kelvin : {kelv:.2f}")
        elif inputanAkhir == 3:
            rea = nilai * (4/5)
            print(f"Konversi celcius ke reamur : {rea:.2f}")


def fahrenheit(nilai):
    if inputanAwal == 2:
        if inputanAkhir == 1:
            celc = (nilai - 32) * (5/9)
            print(f"Konversi fahrenheit ke celcius : {celc:.2f}")
        elif inputanAkhir == 2:
            kelv = (nilai - 32) * (5/9) + 273.15
            print(f"Konversi fahrenheit ke kelvin : {kelv:.2f}")
        elif inputanAkhir == 3:
            rea = (nilai - 32) * (4/9)
            print(f"Konversi fahrenheit ke reamur : {rea:.2f}")

def kelvin(nilai):
    if inputanAwal == 3:
        if inputanAkhir == 1:
            celc = nilai - 273.15
            print(f"Konversi kelvin ke celcius : {celc:.2f}")
        elif inputanAkhir == 2:
            farh = (nilai - 273.15) * (9/5) + 32
            print(f"Konversi kelvin ke fahrenheit : {farh:.2f}")
        elif inputanAkhir == 3:
            rea = (nilai - 273.15) * (4/5)
            print(f"Konversi kelvin ke reamur : {rea:.2f}")

def reamur(nilai):
    if inputanAwal == 4:
        if inputanAkhir == 1:
            celc = nilai * (5/4)
            print(f"Konversi reamur ke celcius : {celc:.2f}")
        elif inputanAkhir == 2:
            farh = nilai * (9/4) + 32
            print(f"Konversi reamur ke fahrenheit : {farh:.2f}")
        elif inputanAkhir == 3:
            kelv = nilai * (5/4) + 273.15
            print(f"Konversi fahrenheit ke kelvin : {kelv:.2f}")

celcius(nilai)
fahrenheit(nilai)
kelvin(nilai)
reamur(nilai)