n = int(input("Masukkan nilai N = "))
for x in range(n):
    if(10 ** x > n):
        break
    else:
        print("Nilai yang terkecil dari 10^x terkecil dari N adalah",10 ** x)