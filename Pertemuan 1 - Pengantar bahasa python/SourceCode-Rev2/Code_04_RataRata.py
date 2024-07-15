# PROGRAM RataRata.py

# main method
if __name__ == "__main__":

  # proses menjumlahkan 5 buah bilangan
  jumlah_nilai = 0
  for i in range(5):
    nilai = float(input("Masukkan nilai {}: ".format(i + 1)))
    jumlah_nilai = jumlah_nilai + nilai

  # Menghitung rata-rata
  rata_rata = jumlah_nilai / 5

  # Menampilkan hasil
  print("Rata-rata dari 5 nilai tersebut adalah:", rata_rata)