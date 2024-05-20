# PROGRAM Runtunan2.py
# Program ini digunakan untuk menghitung nilai mahasiswa berdasarkan nilai formatif (40%), nilai UTS (30%), nilai UAS (30%).

# ALGORITMA
if __name__ == "__main__":
    
    # Input program
    # -------------
    print("Input program")
    nama = input("Masukan nama anda : ")
    nim = input("Masukan nim anda : ")
    formatif = input("Berapa nilai formatif : ")
    uts = input("Berapa nilai uts : ")
    uas = input("Berapa nilai uas : ")
    print("")

    # Proses program
    nilai_akhir = float(formatif)*0.4 + float(uts)*0.3 + float(uas)*0.3

    # Output program
    # --------------
    print("Output program")
    print(str(nama),"-",str(nim))
    print("Nilai akhir sebesar : ", str(nilai_akhir))