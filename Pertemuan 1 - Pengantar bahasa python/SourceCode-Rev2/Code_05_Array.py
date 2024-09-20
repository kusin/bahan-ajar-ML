# PROGRAM Array1.py
# Program ini digunakan untuk menjumlahkan dua buah matriks berukuran 3x3

# DEKLARASI Pustaka
import numpy as np

# ALGORITMA
if __name__ == "__main__":

  # Input Program
  Arr1 = np.array([
    [1, 2, 3], [4, 5, 6], [7, 8, 9],
  ])
  Arr2 = np.array([
    [1, 0, 0], [0, 1, 0], [0, 0, 1],
  ])

  # proses penjumlahan array
  Arr3 = Arr1 + Arr2
  
  # Output program
  print("Hasil penjumlahan array")
  print(Arr3)
  