berjalan= True
while berjalan:
    nilai_str = input("input nilai disini (atau ketik 'selesai'untuk keluar):")
    if nilai_str.lower() == 'selesai':
        berjalan = False
        continue
    nilai=int(nilai_str)
    print (f"Jika nilai anda adalah {nilai} Maka Predikat anda adalah:" )
    if nilai >= 90:
        print("predikat A")
    elif nilai >= 85:
        print("predikat -A")
    elif nilai >= 80:
        print("predikat B")
    elif nilai >= 75:
        print("predikat -B")
    else :
        print("predikat C") 

    print ("-" *20) 

print ("terimakasih")