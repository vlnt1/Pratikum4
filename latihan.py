print("Akses list")

print ("List sebanyak 5 elemen") 
list = [1,2,3,4,5]
print(list)

print("Tampilkam elemen ke 3")
print(list[-3])

print("Ambil nilai elemen ke 2 sampai elemen ke 4")
print(list[1:4])

print("Ambil elemen terakhir")
print(list[-1])

print("Ubah Elemen List")

print("Ubah elemen ke 4 dengan nilai lainnya")
odd = [1,2,3,4,5]
odd[3] = 10
print(odd)

print("Ubah elemen ke 4 sampai dengan elemen terakhir")
odd[3:5] = [10,11]
print(odd)

print("Tambah Elemen List")

print("Ambil 2 bagian dari list pertama (A) dan jadikan list Ke-2 (B)")
A = [1,2,3,4,5]
B = A[1:3]
print(B)

print("Tambah list B dengan Nilai String")
B.append("joko")
print(B)

print("Tambah List B dengan 3 nilai")
print(B + [7,8])

print("Gabungkan list B dan List A")
print(B + A)