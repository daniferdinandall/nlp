from iteung import reply
import pandas as pd


""" data = reply.get_val_data()
val_q = []
val_a = []
bot_a = []
for i, v in data.iterrows():
    val_question = v['0']
    val_answer = v['1'].replace('<START>', '').replace('<END>', '').strip()
    val_q.append(val_question)
    val_a.append(val_answer)
    bot_a.append(reply.botReply(val_question)[0])

bot_test_dataframe = pd.DataFrame(
    {
        'question': val_q,
        'answer': val_a,
        'bot': bot_a
    }
)

reply.bot_test_dataframe.to_csv('output_dir/test_result.csv', index=False) """
listJawaban = []
listAkurasi = []
listPertanyaan = []
while True:
    message = input("Kamu: ")
    if message == "exit":

        break
    return_message, status , dec_outputs, akurasi= reply.botReply(message)
    listJawaban.append(return_message)
    listAkurasi.append(akurasi)
    listPertanyaan.append(message)

    print(f"ITeung: {return_message}")

# Membuat DataFrame menggunakan pandas
df = pd.DataFrame({
    'Pertanyaan': listPertanyaan,
    'Jawaban': listJawaban,
    'Akurasi': listAkurasi
})

# Menyimpan DataFrame ke dalam file Excel
df.to_excel('hasil2_bot.xlsx', index=False)

