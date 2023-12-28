barang_harga_tuple = ('Pensil', 1500, 'Buku', 5000, 'Penggaris', 2000)

def pisahkan_data_tuple(data_tuple):
    nama_barang = []
    harga_barang = []
    for i in range(0, len(data_tuple), 2):
        nama_barang.append(data_tuple[i])
        harga_barang.append(data_tuple[i + 1])
    return nama_barang, harga_barang

def buat_dictionary(nama_barang, harga_barang):
    return dict(zip(nama_barang, harga_barang))

nama_barang_list, harga_barang_list = pisahkan_data_tuple(barang_harga_tuple)
dictionary_barang_harga = buat_dictionary(nama_barang_list, harga_barang_list)

print("1. Data tuple:")
print(barang_harga_tuple)
print("2. Hasil pemisahan data tuple:")
print(nama_barang_list, harga_barang_list)
print("3. Hasil pembuatan dictionary:")
print(dictionary_barang_harga)
