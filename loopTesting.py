import pandas as pd
from iteung import reply

# Daftar pertanyaan
listPertanyaan = [
    "Hai",
    "Apa kabar?",
    "Siapa nama kamu?",
    "kamu sehat",
    "kamu suka makan apa?",
    "udah makan?",
    "kamu suka makanan apa?",
    "kamu suka minuman apa?",
]

# Inisialisasi list jawaban dan akurasi
listJawaban = []
listAkurasi = []

# Mendapatkan jawaban dan akurasi untuk setiap pertanyaan
for message in listPertanyaan:
    return_message, status , dec_outputs, akurasi= reply.botReply(message)
    listJawaban.append(return_message)
    listAkurasi.append(akurasi)

# Membuat DataFrame menggunakan pandas
df = pd.DataFrame({
    'Pertanyaan': listPertanyaan,
    'Jawaban': listJawaban,
    'Akurasi': listAkurasi
})

# Menyimpan DataFrame ke dalam file Excel
df.to_excel('hasil_bot.xlsx', index=False)
