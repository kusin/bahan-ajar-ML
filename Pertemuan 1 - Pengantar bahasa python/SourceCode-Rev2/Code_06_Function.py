# PROGRAM Function.py

# DEKLARASI Func
def diskon(harga_barang):
  # proses - menghitung diskon
  if harga_barang >= 100000:
    total_diskon = harga_barang * 0.05
  else:
    total_diskon = 0
  # proses - menghitung total harga
  total_harga = harga_barang - total_diskon

  # return values
  return total_diskon, total_harga

# ALGORITMA
if __name__ == "__main__":
 
  # input program
  nama_barang = input("Masukan nama barang : ")
  harga_barang = float(input("Masukan harga barang : "))
 
  total_diskon, total_harga = diskon(harga_barang)
 
  # output program
  print(f"Total diskon sebesar : Rp. "+"{:0,.0f}".format(total_diskon))
  print(f"Total harga sebesar : Rp. "+"{:0,.0f}".format(total_harga))
  
  