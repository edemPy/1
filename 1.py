import telebot
import subprocess

# Укажите токен вашего телеграм-бота
TOKEN = '6707087582:AAGLVhHYEyJiT9hYXbvMm9PuL-FhAnECqqA'
bot = telebot.TeleBot(TOKEN)

# Функция для выполнения команд на удаленной машине и возврата результата
def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        result = str(e.output)
    return result

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Отправьте мне команду для выполнения на удаленной машине.")

# Обработчик всех текстовых сообщений от пользователя
@bot.message_handler(func=lambda message: True)
def execute_command(message):
    # Проверяем, что сообщение пришло от вас или другого доверенного пользователя, чтобы избежать уязвимостей
    if message.from_user.id == 334858015:  # Замените YOUR_USER_ID на ваш ID в Telegram
        command = message.text
        result = run_command(command)
        bot.reply_to(message, result)

# Запускаем телеграм-бот
bot.polling()
