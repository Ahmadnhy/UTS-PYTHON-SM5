import csv     
import json    
import os      
import logging

# set up menampilkan pesan INFO dan ERROR
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

os.makedirs("data", exist_ok=True)

# menulis file CSV
data_csv = [
    ["nim", "nama", "hadir_uts"],
    ["23001", "april", 6],
    ["23002", "rozi", 3],
    ["23003", "gibran", 0],
    ["23004", "mamad", 1],
]

try:
    logging.info("Membuat dan menulis file CSV...")
    
    with open("data/presensi.csv", "w", newline="") as f:
        writer = csv.writer(f)    # Gunakan writer untuk menulis baris ke CSV
        writer.writerows(data_csv)
        
    logging.info("Berhasil membuat dan menulis file CSV")
    logging.info("File CSV berhasil dibuat didalam folder 'data/presensi.csv'")

except Exception as e:
    logging.error(f"Gagal menulis CSV: {e}")
    logging.error("Terjadi kesalahan saat menulis file CSV:", e)

# membaca file CSV
try:
    print("====================================")
    logging.info("Membaca file CSV...")
    logging.info("Membaca data presensi...")
    
    with open("data/presensi.csv") as f:
        reader = csv.DictReader(f)
        data = list(reader)

    total = len(data)
    hadir = sum(int(row["hadir_uts"]) for row in data)
    persentase = hadir / total * 100

    # ringkasan disimpan ke JSON
    ringkasan = {
        "total": total,
        "hadir": hadir,
        "persentase": persentase
    }

    # Simpan hasil ringkasan ke file JSON
    with open("data/ringkasan.json", "w") as f:
        json.dump(ringkasan, f, indent=4)

    print("====================================")
    logging.info("Ringkasan berhasil disimpan ke JSON.")
    logging.info("Ringkasan disimpan pada 'data/ringkasan.json'")

except Exception as e:
    logging.error(f"Gagal membaca/menulis file: {e}")
    logging.error("Terjadi kesalahan saat membaca atau menulis data:", e)