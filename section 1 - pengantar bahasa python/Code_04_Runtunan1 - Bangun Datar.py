# PROGRAM Runtunan1.py
# Program ini digunakan untuk menghitung luas dan keliling persegi panjang

# ALGORITMA
if __name__ == "__main__":

    # Input program
    print("Input program")
    panjang = int(input("Masukan panjang(cm) : "))
    lebar = int(input("Masukan lebar(cm): "))
    print("")

    # Proses program
    luas = panjang * lebar
    keliling = (panjang*2) + (lebar*2)

    # Output program
    print("Output program")
    print("Luas : "+str(luas))
    print("Keliling : "+str(keliling))