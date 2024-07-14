# PROGRAM GradeNilai.py

# main method
if __name__ == "__main__":

  # input program
  print("-------------------------------")
  mata_kuliah = input("Masukan nama mata kuliah : ")
  nilai_akhir = int(input("Masukan nilai akhir : "))
  print("-------------------------------")

  # proses program
  if nilai_akhir >= 80:
    nilai_huruf = "A"       # output nilai huruf
  elif nilai_akhir >= 70:
    nilai_huruf = "B"       # output nilai huruf
  elif nilai_akhir >= 60:
    nilai_huruf = "C"       # output nilai huruf
  elif nilai_akhir >= 50:
    nilai_huruf = "D"       # output nilai huruf
  else:
    nilai_huruf = "E"       # output nilai huruf

  # Output Program
  print("-------------------------------")
  print("Mata Kuliah : "+str(mata_kuliah))
  print("Nilai Akhir : "+str(nilai_akhir))
  print("Nilai Huruf : "+str(nilai_huruf))
  print("-------------------------------")