#PROGRAM KASIR SEDERHANA
#By : Fatma Wani Silitonga
#2021

print("==== Program Kasir Sederhana ====")
print("---------------------------------")

#masukkan jumlah barang
jumlah = int(input("Masukkan Jumlah Barang: "))

#masukkan nama dan harga barang
#menghitung subtotal
subtotal=0
for i in range(jumlah):
    print("---------------------------------")
    print("Barang ke-",i+1)
    nama = str(input("Nama Barang  : "))
    harga = int(input("Harga Barang : Rp. "))
    subtotal += harga
print("---------------------------------")
print("Sub Total    : Rp.",subtotal)

#menghitung diskon
if (subtotal >= 100000) and (subtotal < 499999): #belanja diatas Rp.100.000 diskon 10%
    diskon = subtotal * 0.1 
    print("Diskon       : Rp.",diskon)
elif (subtotal >= 500000) and (subtotal < 999999): #belanja diatas Rp.500.000 diskon 15%
    diskon = subtotal * 0.15
    print("Diskon       : Rp.",diskon)
elif (subtotal >= 1000000): #belanja diatas Rp.1.000.000 diskon 20%
    diskon = subtotal * 0.2
    print("Diskon       : Rp.",diskon)
else:
    diskon = 0
    print("Diskon       : Rp.",diskon)

#menghitung total
total = subtotal - diskon
print("Total        : Rp.",total)
bayar = int(input("Pembayaran   : Rp. "))

#menghitung pengembalian
if total <= bayar:
    kembali = bayar - total
    print("Kembalian    : Rp.",kembali)
    print("---------------------------------")
    print("== Terimakasih Sudah Berbelanja ==")
elif total >= bayar:
    kurang = total - bayar
    print("\nMaaf Uang Anda kurang : ",kurang)







