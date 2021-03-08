
''''
buatlah sebuah program mencetak hasil nilai perkalian dari inputan user mulai dari awal sampai akhir 
perlihatkan inputan user dari awal sampai akhir setelah itu tunjukkan hasilnya

pertama = angka awal/pertama
terakhir = angka terkhir/batas angka terakhir
perkalianTotal = perkalianTotal * awal  

#input : pertama = angka awal ; terakhir = angka terakhir 

#proses :
memasukkkan angka awal
memasukkan angka akhir
melakukan perulangan (while)
memperlihatkan inputan user dari awal sampai akhir
melakukan perkalian didalam loop
memperliharkan hasil perkaliannya

#output :
menampilkan hasil perkalian dari inputan user pertama sampai terakhir

'''
print("===== selamat datang di program sederhana =====")
pertama = int(input("masukkan angka awal: "))
terakhir = int(input("masukkan angka terakhir: "))
print()
perkalianTotal = 1
while pertama <= terakhir:
    print(pertama,end=" x ")
    perkalianTotal = perkalianTotal * pertama
    pertama = pertama + 1
print("hasil dari perkalian tersebut adalah:",perkalianTotal)
