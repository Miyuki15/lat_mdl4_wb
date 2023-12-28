def tambah_angka(angka, total=0):
    return total + angka

# Contoh penggunaan:
angka1 = 5
angka2 = 3

total_setelah_tambah = tambah_angka(angka1)
total_setelah_tambah_lagi = tambah_angka(angka2, total_setelah_tambah)

print(total_setelah_tambah)
print(total_setelah_tambah_lagi)
