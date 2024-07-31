# PROGRAM GradeNilai.py
import os

# main method
if __name__ == "__main__":

  ulagi = "Y"
  mata_kuliah = ""
  nilai_akhir = ""
  while ulagi == "Y":

    # input program
    os.system("cls")
    print("-------------------------------")
    while mata_kuliah == "":
      mata_kuliah = input("Masukan nama mata kuliah : ")
    while nilai_akhir == "":
      nilai_akhir = input("Masukan nilai akhir : ")
    print("-------------------------------")

    # proses program

    if int(nilai_akhir) >= 80:
      nilai_huruf = "A"       # output nilai huruf
    elif int(nilai_akhir) >= 70:
      nilai_huruf = "B"       # output nilai huruf
    elif int(nilai_akhir) >= 60:
      nilai_huruf = "C"       # output nilai huruf
    elif int(nilai_akhir) >= 50:
      nilai_huruf = "D"       # output nilai huruf
    else:
      nilai_huruf = "E"       # output nilai huruf

    # Output Program
    print("-------------------------------")
    print("Mata Kuliah : "+str(mata_kuliah))
    print("Nilai Akhir : "+str(nilai_akhir))
    print("Nilai Huruf : "+str(nilai_huruf))
    print("-------------------------------")
    print("")

    # reset nilai
    mata_kuliah = ""
    nilai_akhir = ""
    nilai_huruf = ""

    ulagi = input("Apakah ingin ulangi lagi (Y/N): ")