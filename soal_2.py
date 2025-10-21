setoran1 = int(input("Masukkan setoran minggu 1: "))
setoran2 = int(input("Masukkan setoran minggu 2: "))
setoran3 = int(input("Masukkan setoran minggu 3: "))

if setoran1 <= 0 or setoran2 <= 0 or setoran3 <= 0:
    print("Input tidak valid, setoran harus lebih dari 0.")
else:
    total = setoran1 + setoran2 + setoran3
    print("Total setoran:", total)

    if total < 300000:
        print("Kategori: rendah")
    elif total <= 600000:
        print("Kategori: sedang")
    else:
        print("Kategori: tinggi")