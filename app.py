from flask import Flask, render_template
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


@app.route('/')
def index():
    return render_template('index.html', title='Main Page')


if __name__ == '__main__':
    app.run(debug=True, port=8910)
