print("Selamat datang di Restoran Takoyaki")
print("Silahkan pesan menu pilihanmu")
print("Menu Takoyaki")
print("1. Varian 1 = Rp. 2000/pcs (45 pcs/hari)")
print("2. Varian 2 = Rp. 2500/pcs (40 pcs/hari")

pesan = int(input("Varian yang di pesan = "))
if pesan == 1:
    print("Jumlah varian 1 = 45 pcs")
    harga = 2000
    banyak = 45
    jumlah = int (input("Jumlah yang di pesan= "))
    if jumlah > banyak:
        print("Jumlah varian yang anda pesan tidak mencukupi di karenakan jumlah varian 1 hanya memiliki 45 pcs, silahkan pesan ulang.")
        
    elif jumlah >= 10:
        total = harga*jumlah
        print("Kamu membeli varian 1 berjumlah 10 atau lebih")
        print("Kamu mendapatkan diskon sebesar 10%")
        print("")
        total_belanja = harga*jumlah
        diskon = total_belanja * (10/100) # Diskon 10%
        bayar = total_belanja - diskon
        sisa = banyak - jumlah
        print("Total harga sebelum diskon Rp.",total)
        print("Total harga setelah diskon Rp.",bayar)
        print("")
        print("Total yang harus dibayar: Rp.",bayar)
        print("Takoyaki tersisa",sisa,"pcs")
        print("Terima kasih sudah memesan, di mohon untuk menunggu sebentar ya")
    else:
        print("Kamu memilih varian: ",pesan)
        print("Dengan jumlah: ",jumlah)
        print("")
        bayar = harga*jumlah
        sisa = banyak - jumlah
        print("Total yang harus dibayar: Rp. ",bayar)
        print("Takoyaki tersisa",sisa,"pcs")
        print("Terima kasih sudah memesan, di mohon untuk menunggu sebentar ya")


elif pesan == 2:
    print("Jumlah varian 2 = 40 pcs")
    harga = 2500
    banyak = 40
    jumlah = int(input("Jumlah yang di pesan = "))
    if jumlah > banyak:
        print("Jumlah varian yang anda pesan tidak mencukupi di karenakan jumlah varian 2 hanya memiliki 40 pcs, silahkan pesan ulang.")
    elif jumlah >= 8:
            total = harga * jumlah
            print("Kamu membeli varian 2 berjumlah 8 atau lebih")
            print("Kamu mendapatkan diskon sebesar 8%")
            print("")
            total_belanja = harga*jumlah
            diskon = total_belanja * (8/100) # Diskon 10%
            bayar = total_belanja - diskon
            sisa = banyak - jumlah
            print("Total harga sebelum diskon Rp.",total)
            print("Total harga setelah diskon Rp.",bayar)
            print("")
            print("Total yang harus dibayar: Rp.",bayar)
            print("Takoyaki tersisa",sisa,"pcs")
            print("Terima kasih sudah memesan, di mohon untuk menunggu sebentar ya")

    
    else:
        print("Kamu memilih varian: ",pesan)
        print("Dengan jumlah: ",jumlah)
        print("")
        bayar = harga*jumlah
        sisa = banyak - jumlah
        print("Total yang harus dibayar: Rp. ",bayar)
        print("Takoyaki tersisa",sisa,"pcs")
        print("Terima kasih sudah memesan, di mohon untuk menunggu sebentar ya")
        
else : 
        print("Tidak ada pilihan tersebut")