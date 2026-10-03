print('======SOAL NO 1======')
inputUser=(float(input('Masukkan Angka Komparasi disini')))
a = (inputUser >0)
c = (inputUser <5)
d = (inputUser >8)
e = (inputUser <11)
print ('a bernilai ',a)
print ('c bernilai ',c)
print ('d bernilai',d)
print ('e bernilai ',e)

ac = a and c
de = d and e
gabungan = ac or de

print ('hasilnya adalah',gabungan)


print('======SOAL NO 2======')
inputUser=(float(input('Masukkan Angka Komparasi disini')))
a = (inputUser <0)
c = (inputUser >5)
d = (inputUser <8)
e = (inputUser >11)
print ('a bernilai ',a)
print ('c bernilai ',c)
print ('d bernilai',d)
print ('e bernilai ',e)

ac = a or c
de = d or e
dc = c and d
gabungan = a or e or dc

print ('hasilnya adalah',gabungan)