# PROGRAM FormLogin.py

# DEKLARASI Library
import os

# main method
if __name__ == "__main__":

  # menu form login os.system('clear')
  print("--------- FORM LOGIN ---------")
  username = input("Masukan username : ")
  password = input("Masukan password : ")
  print("")
  
  # proses cek username dan password
  if username=="kusin" and password=="admin#1234":

    # output program  
    print("--------- Menu Utama ---------")
    print("Selamat Datang di Halaman Dashboard")
  
  # jika username or password salah
  else:

    # Output program
    print("Username atau password salah !!!")