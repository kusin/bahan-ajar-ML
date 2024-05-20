# PROGRAM Perulangan2.py
# program ini digunakan untuk menghitung faktorial

# ALGORITMA
if __name__ == "__main__":
  
  # input
  bilangan = int(input("Masukan sebuah bilangan: "))
  
  # proses
  faktorial = 1
  for i in range(1, bilangan + 1):
    faktorial = faktorial * i
      
  # output
  print("Faktorial dari", bilangan, "adalah", faktorial)