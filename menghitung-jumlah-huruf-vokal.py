import os

os.system('cls')
os.system('clear')

# konversi dari detik ke jam-menit-detik
print(f"==== MENGHITUNG JUMLAH HURUF VOKAL =====\n")

teks = input("Masukan teks: ")
vokal = "aiueo"
teks_cek = teks.lower()
jumlah = sum(1 for huruf in teks_cek if huruf in vokal)
print(f"Jumlah huruf vokal: {jumlah}")


