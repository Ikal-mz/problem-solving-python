import os

os.system('cls')
os.system('clear')

# konversi dari detik ke jam-menit-detik
print(f"==== KONVERSI DETIK KE JAM-MENIT-DETIK =====\n")

total_detik = int(input("Masukan detik: "))
jam = total_detik // 3600
sisa = total_detik % 3600
menit = sisa // 60
detik = sisa % 60

print(f"""Konversi :
    {jam:02} jam
    {menit:02} menit
    {detik:02} detik
      """)
