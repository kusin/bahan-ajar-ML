# PROGRAM Percabangan1.py
# Program ini digunakan untuk menghitung luas dan keliling
#   dari tiga buah bangun datar seperti persegi panjang, segitiga, dan lingkaran.

# ALGORITMA
if __name__ == "__main__":
  
  # menu utama
  print("-----------------------------------")
  print("Pilihan menu - Program Bangun Datar")
  print("1. Persegi Panjang")
  print("2. Segitiga")
  print("3. Lingkaran")
  
  # memilih menu
  menu = int(input("Masukan pilihan menu (1/2/3): "))
  print("-----------------------------------")

  # proses pemilihan menu
  match menu:
    
    # jika pengguna memilih menu ke-1
    case 1:
      # input program
      print("\nInput program")
      panjang = int(input("Masukan panjang(cm) : "))
      lebar = int(input("Masukan lebar(cm): "))
      print("")

      # Proses program
      luas = panjang * lebar

      # Output program
      print("Output program")
      print("Luas persegi panjang : "+str(luas))

    # jika pengguna memilih menu ke-2
    case 2:
      # input program
      print("\nInput program")
      alas = int(input("Masukan alas(cm) : "))
      tinggi = int(input("Masukan tinggi(cm): "))
      print("")

      # Proses program
      luas = (alas * tinggi)/2

      # Output program
      print("Output program")
      print("Luas segitiga : "+str(luas))

    # jika pengguna memilih menu ke-3
    case 3:
      # input program
      print("\nInput program")
      jari_jari = int(input("Masukan jari-jari(cm) : "))
      print("")

      # Proses program
      luas = 3.14 * jari_jari * jari_jari

      # Output program
      print("Output program")
      print("Luas lingkaran : "+str(luas))

    # jika pengguna salah memilih menu
    case _:
      print("Anda salah memilih menu !!!")
