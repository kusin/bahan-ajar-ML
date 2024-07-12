# PROGRAM Zakat.py

# main method
if __name__ == "__main__":

  # Algoritma
  # - input program
  penghasilan = input("Masukan penghasilan anda : Rp. ")

  # - proses program
  zakat = float(penghasilan) * 0.025

  # - proses program
  print(f"Jumlah zakat sebesar Rp. "+"{:0,.2f}".format(zakat))