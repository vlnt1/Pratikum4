a = []
yatidak = True
while yatidak:
    nama = input("Nama: ")
    nim = input("NIM: ")
    tugas = int(input("Nilai Tugas: "))
    uts = int(input("Nilai UTS: "))
    uas = int(input("Nilai UAS: "))
    akhir =(tugas * 30/100) + (uts * 35/100) + (uas * 35/100)

    a.append([nama,nim,tugas,uts,uas,int(akhir)])
    if(input("Tambah Data (y/t)? ") =='t'):
        yatidak=False
print("------------------------------------------------------------------")
print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
print("------------------------------------------------------------------")
i = 0                                                                         
for nomor in a:                                                             
    i += 1
    print("| {no:2d} | {nama:12s} | {nim:9s} | {tugas:5d} | {uts:5d} | {uas:5d} | {akhir:6.2f} |"
         .format(no=i, nama=nomor[0], nim=nomor[1], tugas=nomor[2], uts=nomor[3], uas=nomor[4], akhir=nomor[5]))
print("------------------------------------------------------------------")