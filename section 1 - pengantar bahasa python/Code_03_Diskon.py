# PROGRAM Diskon

# DEKLARASI
diskon = 0.05    # const diskon 5%

# ALGORITMA
if __name__ == "__main__":

  # input program
  nama_barang = input("Masukan nama barang : ")
  harga_barang = float(input("Masukan harga barang : "))

  # proses program
  total_diskon = harga_barang * diskon
  total_harga = harga_barang - total_diskon

  # output program
  print(f"Harga barang setelah diskon adalah "+"{:0,.0f}".format(total_harga))
