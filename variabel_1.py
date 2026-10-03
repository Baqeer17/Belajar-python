nama =input("siapa Nama Kamu?")
umur_str=input("Berapa Umur Kamu?")
umur=int (umur_str)
tingkat_semester=input("anda menempuh semester ke berapa?")
tingkat=int (tingkat_semester)
print (f"halo,{nama}! Senang bertemu kamu.")
if umur >= 18:
    print("anda telah memenuhi syarat")
else:
    print("anda belum memenuhi syarat")
if tingkat >=4:
    print("anda telah memenenuhi syarat")
else:
    print("anda belum memenuhi syarat")