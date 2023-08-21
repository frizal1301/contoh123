import os
import time
import telebot
import threading
import subprocess

# Inisialisasi token bot Telegram
telegram_token = '6056937180:AAER28G6M_ZYXL_QQarxuDONKzl875oExOo'
bot = telebot.TeleBot(telegram_token)

# Variabel untuk menyimpan status terakhir
init_count = 0
logs = '/home/linux/log-tele.txt'
chat_id='1297711079'

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

@bot.message_handler(commands=['block'])
def block(message) :
    global chat_id
    # bot.send_message(chat_id, 'ical')
 
    command = message.text.split()
    if len(command) >= 4 :
        ip_address = command[2]
        port = command[4]

        print("Ip address:", ip_address)
        print("Port:", port)
        block = f"sudo iptables -A INPUT -s {ip_address} -p tcp --dport {port} -j DROP"
        result = subprocess.run(block, shell=True, capture_output=True, text=True, check=True)

        if result.returncode == 0 :
            bot.send_message(chat_id, f"IP Address {ip_address} pada port {port} berhasil diblokir")

# Monitoring Server
def monitor_server() :
    global init_count
    while True:
        last_count = os.path.getsize(logs)
        if last_count > init_count:
            msg = os.popen(f'tail -n 2 {logs}').read()
            caption = f'Halo nTerjadi serangan pada Server!\n\nServer Time: {time.strftime("%d %b %Y %H:%M:%S")}\n\n{msg}'
            with open(msg_caption, 'w') as file:
                file.write(caption)
            send_alert(caption)
            print("Alert Terkirim")
            init_count = last_count
            os.remove(msg_caption)
        time.sleep(2)  # Tunda 2 detik sebelum memeriksa kembali

def run_bot() :
    bot.polling()
# membuat thread monitor_server
server_thread = threading.Thread(target=monitor_server)

# membuat thread run_bot
bot_thread = threading.Thread(target=run_bot)

server_thread.start()

bot_thread.start()