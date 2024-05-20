# PROGRAM Percabangan2.py
# Program ini digunakan untuk menghitung nilai akhir mahasiswa berdasarkan
#   nilai formatif (40%), nilai UTS (30%), nilai UAS (30%).
#   Kemudian program ini dapat menentukan nilai huruf berdasarkan nilai akhir
#   	jika nilai lebih besar dari 80 maka mendapat nilai A
#     jika nilai lebih besar dari 70 maka mendapat nilai B
#     jika nilai lebih besar dari 60 maka mendapat nilai C
#     jika nilai lebih besar dari 50 maka mendapat nilai D
#     jika nilai kurang dari 50 maka mendapat nilai E


# ALGORITMA
if __name__ == "__main__":
	
	# ------------- -- #
	# Input program -- #
	# ------------- -- #
	print("Input program")
	nama = input("Masukan nama anda : ")
	nim = input("Masukan nim anda : ")
	formatif = input("Berapa nilai formatif : ")
	uts = input("Berapa nilai uts : ")
	uas = input("Berapa nilai uas : ")
	print("")

	# Proses program
	# - menghitung nilai akhir
	nilai_akhir = float(formatif)*0.4 + float(uts)*0.3 + float(uas)*0.3

	# PROSES program
	# - menentukan nilai huruf
	if(nilai_akhir >= 80):
		nilai_huruf = 'A'
	elif(nilai_akhir >=70):
		nilai_huruf = 'B'
	elif(nilai_akhir >=60):
		nilai_huruf = 'C'
	elif(nilai_akhir >=50):
		nilai_huruf = 'D'
	else:
		nilai_huruf = 'E'

	# -------------- -- #
	# Output program -- #
	# -------------- -- #
	print("Output program")
	print(str(nama),"-",str(nim))
	print("Nilai akhir anda : "+ str(nilai_akhir))
	print("Nilai huruf anda : "+ str(nilai_huruf))