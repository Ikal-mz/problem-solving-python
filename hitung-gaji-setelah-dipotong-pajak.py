import os
os.system('cls')
os.system('clear')

# menghitung gaji di atas 5,5jt setelah dipotong pajak 11%
print(f"HITUNG POTONGAN GAJI DI ATAS 5,5 JUTA DENGAN PAJAK 11%")
gaji = int(input("Masukan gaji : "))

if gaji > 5_500_000:
    gaji_bersih = gaji - (gaji * 0.11)
    potongan_pajak = gaji * 0.11
else:
    gaji_bersih = gaji
    potongan_pajak = 0

print(f"Potongan pajak: Rp{potongan_pajak:,.2f}")
print(f"Gaji bersih: Rp{gaji_bersih:,.2f}")

