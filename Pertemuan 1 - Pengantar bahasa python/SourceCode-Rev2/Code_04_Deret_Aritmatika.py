# PROGRAM Perulangan1.py
# Program ini digunakan untuk menampilkan bilangan 1 sampai 5
#   menggunakan perulangan for, while, dan do-while.

# ALGORITMA
if __name__== "__main__":

  print("Perulangan - FOR")
  for x in range(1,15,3):
    print("Bilangan ke-"+str(x))
  # ---------------------------------

  print("Perulangan - WHILE")
  y = 1
  while y <= 15:
    print("Bilangan ke-"+str(y))
    y = y + 3
  # ---------------------------------
  