def hitung_ongkir(berat_kg, kota, asuransi=False):
    tarif_dasar = {"Jakarta": 10000, "Bandung": 12000, "Surabaya": 15000
    }

    ongkir = berat_kg * 2000 + tarif_dasar.get(kota)

    # Jika pengguna memilih asuransi
    if asuransi:
        ongkir += 3000

    return ongkir

print(hitung_ongkir(2, "Jakarta"))
print(hitung_ongkir(3, "Surabaya", asuransi=True))