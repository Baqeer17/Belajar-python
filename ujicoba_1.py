nama=input ("siapa nama anda?")
iman_2=int (input("berapa kali anda shalat dalam sehari?"))
iman=int (iman_2)
iman_3=input("apakah anda membaca alquran paling tidak seminggu sekali? (ya/tidak) ")
print (f"halo {nama} mari kita chek keimananmu")
if iman_2 <= 5:
    print("MasyaAllah brother, Keren")
else:
    print("Astaghfirullah Brother, Lebih ditingkatkan lagi keimanannya")
if iman_3.lower () == 'ya' :
    print("MasyaAllah brother, anda hebat")
else:
    print("Lebih rajin lagi ya ibadahnya")

