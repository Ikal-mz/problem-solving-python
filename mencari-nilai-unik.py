import os

os.system('cls' if os.name == 'nt' else 'clear')


# MENCARI NILAI UNIK
print(f"==== MENCARI NILAI UNIK =====\n")
jumlah_angka = int(input("Berapa banyak angka yang ingin Anda masukkan: "))
daftar_angka = []

for i in range(jumlah_angka):
    while True:
        try:
            angka = int(input(f"Masukkan angka ke-{i+1}: "))
            daftar_angka.append(angka)
            break
        except ValueError:
            print("Input yang Anda masukkan bukan angka. Silakan coba lagi.")
            # Anda bisa menambahkan logika di sini jika ingin pengguna mengulang input angka yang salah
    

print("Angka-angka yang telah Anda masukkan:", daftar_angka)


unik = {x for x in daftar_angka if daftar_angka.count(x) == 1}
print(f"Angka yang unik: {unik}")

