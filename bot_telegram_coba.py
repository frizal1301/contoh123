import os
import time
import telebot

# Inisialisasi token bot Telegram
telegram_token = '6056937180:AAER28G6M_ZYXL_QQarxuDONKzl875oExOo'
bot = telebot.TeleBot(telegram_token)

# Variabel untuk menyimpan status terakhir
init_count = 0
logs = '/home/ghost666/log-tele.txt'

# File sementara untuk menyimpan pesan
msg_caption = '/tmp/telegram_msg_caption.txt'

# Fungsi untuk mengirimkan pesan ke bot Telegram
def send_alert(caption):
    bot.send_message(chat_id, caption)

# Memperoleh chat ID
@bot.message_handler(commands=['start'])
def handle_start(message):
    global chat_id
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Bot is ready to monitor logs.')

# Monitoring Server
while True:
    last_count = os.path.getsize(logs)
    if last_count > init_count:
        msg = os.popen(f'tail -n 2 {logs}').read()
        caption = f'Halo Sayangku Admin Putri ESA I LOVE YOU\nTerjadi serangan pada Server!\n\nServer Time: {time.strftime("%d %b %Y %H:%M:%S")}\n\n{msg}'
        with open(msg_caption, 'w') as file:
            file.write(caption)
        send_alert(caption)
        print("Alert Terkirim")
        init_count = last_count
        os.remove(msg_caption)
    time.sleep(2)  # Tunda 2 detik sebelum memeriksa kembali