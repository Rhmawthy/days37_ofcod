#program menghitung upah karyawan

nama= input("masukkan nama anda:")
golongan = input("masukkan golongan:")
jam = int(input ("masukkan jam kerja anda:"))

print ("nama:", nama, "golongan:", golongan, "jam kerja:",jam)

#tentukan upah golongan per jam

if golongan == " A":
    upah = 10000
elif golongan == " B":
    upah = 7000
elif golongan == " C":
    upah = 6000
elif golongan == " D":
    upah = 5000

    
#cek apakah jam kerja lebih dari 48 jam
if jam > 0:
    upah =  48 - jam
    total_upah = 48* upah + ((48-jam)*4000)

print ("upa anda Rp",total_upah)
    
    





