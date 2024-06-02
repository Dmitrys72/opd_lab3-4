from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        a = request.form.get('a')
        b = request.form.get('b')
        c = request.form.get('c')
        try:
            a = int(a)
            b = int(b)
            c = int(c)
        except:
            raise TypeError("Параметры должны быть реальным числом")
        if a == 0:
            return render_template('index.html', error="Коэффициент a должен быть не равен 0")
        D = b**2 - 4 * a * c
        if D < 0:
            return render_template('index.html', error="Корней нет")
        if D == 0:
            x1 = -(b)/(2*a)
            result = [x1]
        if D > 0:
            x1 = (-(b) + math.sqrt(D)) / (2 * a)
            x2 = (-(b) - math.sqrt(D)) / (2 * a)
            result = [x1, x2]
        return render_template('index.html', result=result)
    return render_template('index.html')
