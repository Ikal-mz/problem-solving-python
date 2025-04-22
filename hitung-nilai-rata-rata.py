import os
os.system('cls')
os.system('clear')

# menghitung nilai rata-rata siswa dengan inputan
nilai_siswa = []
while True:
    try:
        nilai = int(input("Masukan nilai siswa : "))
        nilai_siswa.append(nilai)
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        continue  # Kembali ke awal loop jika input tidak valid

    validasi = input("Masukan nilai lagi (y/n)? ")
    if validasi.lower() == "n":
        break

if nilai_siswa:  # Memastikan list tidak kosong sebelum menghitung rata-rata
    rata_rata = sum(nilai_siswa) / len(nilai_siswa)
    jumlah_diatas_rata = sum(1 for n in nilai_siswa if n > rata_rata)

    print(f"Nilai siswa yang anda masukan : {nilai_siswa}")
    print(f"Nilai rata-rata siswa : {rata_rata:.2f}")
    print(f"Banyak siswa di atas nilai rata-rata: {jumlah_diatas_rata}")
else:
    print("Tidak ada nilai siswa yang dimasukkan.")


"""
    jumlah_diatas_rata = 0
    for n in nilai_siswa:
        if n > rata_rata:
            jumlah_diatas_rata += 1
    ---------------------------------------------------------------------
    untuk bentuk simpel dari mencari jumlah di atas rata-rata gunakan ini
    ---------------------------------------------------------------------
    jumlah_diatas_rata = sum(1 for n in nilai_siswa if n > rata_rata)
"""