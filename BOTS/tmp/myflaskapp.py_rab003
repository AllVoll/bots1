from flask import Flask, render_template, request
from binance.client import Client
import json

app = Flask(__name__)

# Ключ API и секретный ключ для подключения к Binance API
api_key = 'your_api_key'
api_secret = 'your_api_secret'

# Инициализация клиента Binance API
client = Client(api_key, api_secret)

# Имя файла для сохранения списка ботов
BOT_FILE = 'bot_list.json'

# Функция для загрузки списка ботов из файла
def load_bots():
    try:
        with open(BOT_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Функция для сохранения списка ботов в файл
def save_bots(bot_list):
    with open(BOT_FILE, 'w') as f:
        json.dump(bot_list, f)

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Страница общих настроек
@app.route('/settings')
def settings():
    return render_template('settings.html')

# Страница списка ботов
@app.route('/bot_list')
def bot_list():
    # Получение списка ботов из базы данных или файла
    bot_list = load_bots()
    return render_template('bot_list.html', bot_list=bot_list)

# Страница создания бота
@app.route('/create_bot')
def create_bot():
    return render_template('create_bot.html')

# Страница статистики ботов
@app.route('/bot_stat')
def bot_stat():
    return render_template('bot_stat.html')

# Страница графиков
@app.route('/charts')
def charts():
    return render_template('charts.html')

if __name__ == '__main__':
    app.run(debug=True)
