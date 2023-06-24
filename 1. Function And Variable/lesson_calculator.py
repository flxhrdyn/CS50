# Program Kalkulator Sederhana

# Kalkulator Integer
print("Kalkulator Integer")
x = int(input("Masukkan nilai x : ")) # input integer x
y = int(input("Masukkan nilai y : ")) # input integer y 
# klo kita gak pake int sebelum function input maka programnya akan menerima input string, bukan integer
# walapun kita input angka akan tetap dibaca string

# variabel z yang akan menambahkan x dan y
z = x + y

# print out hasil pertambahan
print(f"Hasil Pertambahan Interger Adalah : {z:,}" ) # fungsi {z:,} adalah untuk menambahkan koma di bilangan ribuan 

# Kalkulator Float
print("\nKalkulator Float")
a = float(input("Masukkan nilai a : ")) # input float x
b = float(input("Masukkan nilai b : ")) # input float y 
# variabel diatas dapat menerima input yang bernilai desimal karena menggunakan tipe data float

# print out hasil pertambahan
print("Hasil Pertambahan Float Adalah : ", round(a/b, 3)) # fungsi round adalah untuk membulatkan
# round(a/b, 3) : function disini artinya program akan membulatkan dan menampilkan 3 angka dibelakang koma


