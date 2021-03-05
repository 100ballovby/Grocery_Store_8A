from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # указываю путь к БД
db = SQLAlchemy(app)  # создаю БД


class Grocery(db.Model):
    """Класс Базы Данных. Описываем поля"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False, default=0.01)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Grocery {self.name}>'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':  # если я получаю данные из формы
        name = request.form['name']
        price = request.form['price']
        new_stuff = Grocery(name=name, price=price)
        try:  # попробовать сделать это:
            db.session.add(new_stuff)  # добавляю в БД новый продукт
            db.session.commit()  # сохраняю изменения
            return redirect('/')  # перенаправляю пользователя на главную
        except:
            return 'There was a problem adding new item.'
    else:
        groceries = Grocery.query.order_by(Grocery.created_at).all()
        # ^ генерирую все объекты из базы данных
        return render_template('index.html', title='Main Page', items=groceries)


@app.route('/delete/<id>')
def delete(id):
    product = Grocery.query.get_or_404(id)
    # ^ сохраняю продукт в переменную
    try:
        db.session.delete(product)  # удалить из БД
        db.session.commit()  # применить изменения
        return redirect('/')  # вернуться на главную
    # если что-то пошло не так
    except:
        return 'There was a problem deleting data!'


@app.errorhandler(404)
def not_found(error):
    return render_template('not_found.html'), 404


if __name__ == '__main__':
    app.run(debug=True, port=8910)
