# PROGRAM Konversi Suhu
# Program ini digunakan untuk konversi suhu dari celcius ke fahrenheit, reamur, kelvin

# ALGORITMA
if __name__ == "__main__":

  # input program
  celcius = float(input("masukan suhu celcius : "))

  # proses program
  reamur = celcius * 0.8
  fahrenheit = (celcius * 1.8) - 32
  kelvin = celcius + 273

  # output program
  print("Suhu reamur : ",reamur)
  print("Suhu fahrenheit : ",fahrenheit)
  print("Suhu kelvin : ",kelvin)
  
