# PROGRAM Aritmatika.py

# ALGORITMA
if __name__ == "__main__":

    # input program
    print("Input program")
    bilangan1 = int(input("Masukan bilangan ke-1: "))
    bilangan2 = int(input("Masukan bilangan ke-2: "))
    print("")

    # proses aritmatika
    penjumlahan = bilangan1 + bilangan2
    pengurangan = bilangan1 - bilangan2
    pembagian = bilangan1 * bilangan2
    perkalian = bilangan1 / bilangan2

    # output program
    print("Output program")
    print(str(bilangan1), "+", str(bilangan2), "=", penjumlahan)
    print(str(bilangan1), "-", str(bilangan2), "=", pengurangan)
    print(str(bilangan1), "*", str(bilangan2), "=", pembagian)
    print(str(bilangan1), "/", str(bilangan2), "=", perkalian)