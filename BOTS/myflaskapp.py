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

# Страница создания бота
@app.route('/create_bot', methods=['GET', 'POST'])
def create_bot():
    if request.method == 'POST':
        bot_name = request.form['bot_name']
        bot_symbol = request.form['bot_symbol']
        bot_budget = request.form['bot_budget']
        bot_quantity = request.form['bot_quantity']

        # Создание нового бота
        bot = {
            'name': bot_name,
            'symbol': bot_symbol,
            'budget': bot_budget,
            'quantity': bot_quantity
        }

        # Получение текущей цены символа бота из Binance API
        symbol_price = client.get_symbol_ticker(symbol=bot_symbol)['price']
        bot['price'] = symbol_price

        # Сохранение бота в базу данных или файл
        bot_list = load_bots()
        bot_list.append(bot)
        save_bots(bot_list)

        return render_template('bot_created.html', bot=bot)
    else:
        return render_template('create_bot.html')

# Страница списка ботов
@app.route('/bot_list')
def bot_list():
    # Получение списка ботов из базы данных или файла
    bot_list = load_bots()

    return render_template('bot_list.html', bot_list=bot_list)

# Страница управления ботом
@app.route('/bot/<bot_name>')
def bot_control(bot_name):
    # Получение данных бота из базы данных или файла по его имени
    bot_list = load_bots()
    bot = next((b for b in bot_list if b['name'] == bot_name), None)

    if bot is None:
        return render_template('bot_not_found.html', bot_name=bot_name)

    # Получение баланса и цены для символа бота из Binance API
    symbol_balance = client.get_asset_balance(asset=bot['symbol'].replace('USDT', ''))
    symbol_price = client.get_symbol_ticker(symbol=bot['symbol'])['price']

    return render_template('bot_control.html', bot=bot, symbol_balance=symbol_balance, symbol_price=symbol_price)

if __name__ == '__main__':
    app.run(debug=True)
