input_user = input("Masukan angka acak : ")

hasil = 0

for i in range(len(input_user)):
    input_to_int = int( input_user[i])

    if input_to_int % 2 == 0:
        hasil +=1

print (hasil)