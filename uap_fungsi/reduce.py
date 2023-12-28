from functools import reduce

# Fungsi filter untuk mendapatkan angka kelipatan 3
kelipatan_3 = filter(lambda x: x % 3 == 0, range(51))

# Menggunakan fungsi reduce untuk menjumlahkan angka-angka kelipatan 3
hasil_jumlah = reduce(lambda x, y: x + y, kelipatan_3)

print(hasil_jumlah)
