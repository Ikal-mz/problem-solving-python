# menghitung jumlah kata dalam teks
def count_words(text):
    words = text.strip().split()
    return len(words)

hitung_kata = count_words("Hello world saya ikal mz")
print(hitung_kata)

"""
Penjelasan: String dibersihkan dari spasi berlebih dengan strip(), 
lalu dipecah menjadi list kata menggunakan split(). Panjang list adalah jumlah kata.
"""