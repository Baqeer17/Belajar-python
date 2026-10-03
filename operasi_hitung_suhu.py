print ("\n OPERASI SUHU FAHRENHEIT \n")
fahrenheit= float(input("berapa suhu fahrenheit?"))
print("suhu adalah",fahrenheit,"derajat fahrenheit")

kelvin=(fahrenheit + 459.67)*(5/9)
print("suhu dalam kelvin adalah",kelvin,"derajat kelvin")

print("\n OPERASI HITUNG SUHU KELVIN \n")
kelvin=float(input("berapa suhu kelvin disana?"))
print("suhu kelvin=",kelvin,"derajat kelvin")

fahrenheit=(kelvin-273.15)*9/5+32
print("suhu dalam fahrenheit=",fahrenheit,"derajat fahrenheit")