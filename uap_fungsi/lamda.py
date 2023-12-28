klasifikasi_angka = lambda x: "Positif" if x > 0 else ("Nol" if x == 0 else "Negatif")
pencarian_angka = lambda list_angka, find: "found" if find in list_angka else "not found"

angka = 7
hasil_klasifikasi = klasifikasi_angka(angka)
print(hasil_klasifikasi)

daftar_angka = [1, 2, 3, 4, 5]
angka_cari = 3
hasil_pencarian = pencarian_angka(daftar_angka, angka_cari)
print(hasil_pencarian)
