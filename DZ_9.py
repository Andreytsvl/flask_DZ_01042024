# Задание №9
# Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# При отправке которой будет создан cookie файл с данными
# пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.
from flask import Flask, request, redirect, url_for, render_template, make_response

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        response = make_response(redirect(url_for('Привет')))
        response.set_cookie('user_data', f'{name}/{email}')

        return response

    return render_template('DZ_9.html')


@app.route('/Привет')
def Привет():
    user_data = request.cookies.get('user_data')
    if user_data:
        name, email = user_data.split('/')
        return f'Привет, {name}! Ваш адрес электронной почты: {email}. <br><a href="/logout">Выйти</a>'
    else:
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('user_data', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)