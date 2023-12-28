def hitung_pangkat(pangkat):
    def pangkat_dalam_closure(x):
        return x ** pangkat
    return pangkat_dalam_closure

# Contoh penggunaan:
pangkat_kuadrat = hitung_pangkat(2)
pangkat_kubik = hitung_pangkat(3)

# Menggunakan fungsi closure untuk menghitung pangkat
hasil_kuadrat = pangkat_kuadrat(4)
hasil_kubik = pangkat_kubik(4)

print("Hasil Kuadrat:", hasil_kuadrat)
print("Hasil Kubik:", hasil_kubik)
