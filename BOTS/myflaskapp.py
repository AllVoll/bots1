from flask import request
from flask import Flask, render_template

app = Flask(__name__)

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Страница настроек
@app.route('/settings')
def settings():
    return render_template('settings.html')

# Страница управления API
# @app.route('/api_manager')
# def api_manager():
#     return render_template('api_manager.html')

# Страница управления списком монет
@app.route('/coinlist_manager')
def coinlist_manager():
    return render_template('coinlist_manager.html')

# Страница управления депозитами
@app.route('/depo_manager')
def depo_manager():
    return render_template('depo_manager.html')

# Страница управления стратегиями
@app.route('/strategy_manager')
def strategy_manager():
    return render_template('strategy_manager.html')

# Страница создания бота
@app.route('/create_bot')
def create_bot():
    return render_template('create_bot.html')

# Страница со списком ботов
@app.route('/bot_list')
def bot_list():
    return render_template('bot_list.html')

# Страница со статистикой бота
@app.route('/bot_stat')
def bot_stat():
    return render_template('bot_stat.html')

# Страница с графиками
@app.route('/charts')
def charts():
    return render_template('charts.html')

# Страница с графиком монеты
@app.route('/coin_chart')
def coin_chart():
    return render_template('coin_chart.html')

@app.route('/sidebar')
def sidebar():
    return render_template('sidebar.html')

@app.route('/api-manager', methods=['GET', 'POST'])
def api_manager():
    if request.method == 'POST':
        api_name = request.form['api-name']
        api_key = request.form['api-key']
        secret_key = request.form['secret-key']
        api_type = request.form['api-type']
        data = {
            'api_key': api_key,
            'secret_key': secret_key,
            'api_type': api_type
        }
        with open('api_data.json', 'w') as f:
            json.dump(data, f)
    return render_template('api_manager.html')

if __name__ == '__main__':
    app.run()