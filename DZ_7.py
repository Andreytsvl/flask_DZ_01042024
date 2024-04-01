# Задание №7
# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def summ():


    if request.method == 'POST':
        number = int(request.form['number'])
        square = number ** 2

        return redirect(url_for('result', number=number, square=square))
    return render_template('form_calculate_DZ.html')

@app.route('/result')
def result():
    number = request.args.get('number')
    square = request.args.get('square')
    return f'Вы ввели число: {number}<br>Квадрат числа: {square}'


if __name__ == '__main__':
    app.run(debug=True)