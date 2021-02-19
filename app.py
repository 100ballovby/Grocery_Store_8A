from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # указываю путь к БД
db = SQLAlchemy(app)  # создаю БД


@app.route('/')
def index():
    return render_template('index.html', title='Main Page')


if __name__ == '__main__':
    app.run(debug=True, port=8910)
