# PROGRAM Bilangan Terbesar

# main method
if __name__ == "__main__":

  # masukan program
  num1 = 3
  num2 = 4
  num3 = 5

  # proses program
  if num1 >= num2 and num1 >= num3:
    largest = num1
  elif num2 >= num1 and num2 >= num3:
    largest = num2
  else:
    largest = num3
  
  # keluaran program
  print("Bilangan terbesar adalah:", largest)
    