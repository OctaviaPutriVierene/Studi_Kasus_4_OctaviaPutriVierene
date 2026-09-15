Produk = { 
    "Produk1": {
        "Nama" : "Kue tart",
        "Harga" : "Rp15.000",
        "Stok" : "25"
    }
    }
while True:
    print("\n Toko Bakery R")
    print("Menu pengelolaan data produk: ")
    print("1. Tampilkan data produk")
    print("2. Tambah kategori")
    print("3. Ubah harga")
    print("4. Hapus kategori")
    print("5. Tampilkan data setelah perubahan")
    print("6. keluar")
    pilihan = input("Pilih menu 1-6:")

    if pilihan == "1" :
        print("\n Data produk")
        print("Nama:", Produk["Produk1"]["Nama"])
        print("Harga:", Produk["Produk1"]["Harga"])
        print("Stok:", Produk["Produk1"]["Stok"])
        if "Rasa" in Produk["Produk1"]:
            print("Rasa  :", Produk["Produk1"]["Rasa"])

    elif pilihan == "2":
        Rasa_baru = input("Masukkan kategori terbaru: ")
        Produk["Produk1"]["Rasa"] = Rasa_baru
        print("Kategori berhasil ditambahkan")

    elif pilihan == "3":
        harga_baru =  input("Masukkan harga terbaru:")
        Produk["Produk1"]["Harga"] = harga_baru
        print("Harga berhasil diubah")

    elif pilihan == "4":
        if "Rasa" in Produk["Produk1"]:
            Produk["Produk1"].pop("Rasa")
            print("Kategori berhasil dihapus")
        else:
            print("Kategori tidak ada/sudah dihapus")

    elif pilihan == "5":
        print(Produk)

    elif pilihan == "6" :
        print ("\nselesai")
        break