# PROGRAM Faktorial.py

# main method
if __name__ == "__main__":

  # input program
  bilangan = int(input("Masukan sebuah bilangan: "))

  # proses menghitung faktorial
  faktorial = 1
  for i in range(bilangan, 1, -1):
    faktorial = faktorial * i
  
  # output program
  print("faktorial "+str(bilangan)+" adalah :"+str(faktorial))