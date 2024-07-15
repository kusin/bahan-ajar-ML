# PROGRAM Euclidean.py

# main method
if __name__ == "__main__":

  # Deklarasi variabel
  m = 40
  n = 24

  # proses menghitung FPB
  while(n != 0):
    r = m % n
    m = n
    n = r
  
  # output program
  print("Euclidean adalah "+str(m))