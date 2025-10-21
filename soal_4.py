def jadwal_hari(hari):
    jadwal = [{"hari": "Senin", "matkul": "Algoritma"}, {"hari": "Selasa", "matkul": "Basis Data"}, {"hari": "Rabu", "matkul": "Jaringan Komputer"}]

    for item in jadwal:
        if item["hari"] == hari:
            # Jika ketemu, kembalikan nama mata kuliah
            return f"Jadwal hari {hari}: {item['matkul']}"
    
    return "Jadwal tidak ditemukan."

# mengecek satu per satu hari
print(jadwal_hari("Rabu"))
print(jadwal_hari("Jumat"))