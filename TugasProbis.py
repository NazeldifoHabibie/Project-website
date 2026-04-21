JumlahDuit = float(input("Jumlah Duit"))
Diskon = float(input("Diskon"))
Harga = float(input("Harga Barang"))
JumlahBarang = float(input("Jumlah Barang"))

JumlahDiskon = Diskon / 100
TotalHarga = JumlahBarang * JumlahDuit * JumlahDiskon - Harga
if(TotalHarga > 250000):
  print("Total bayar berlebih")
  print("Total Harga", TotalHarga)
  print("Total diskon", JumlahDiskon * Harga)
else:
  print("Total bayar tidak berlebih")
  print("Total Harga", TotalHarga)
  print("Total diskon", JumlahDiskon * Harga)