from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    month = db.Column(db.Integer, nullable=False)
    day = db.Column(db.Integer, nullable=False)
    birthday = db.Column(db.String(100), nullable=True)


    def __repr__(self):
        return f'id:{self.id}-name:{self.name}-month:{self.month}-day:{self.day}'


@app.route('/', methods=["GET"])
def index():
    users = User.query_all()
    return render_template('index.html', users)


@app.route('/', methods=["POST"])
def add_birthday():
    name = request.form.get('name')
    month = request.form.get('month')
    day = request.form.get('day')

    birthday = f'{month}/{day}'

    user = User(name=name, month=month, day=day, birthday=birthday)
    db.session.add(user)
    db.session.commit()

    return redirect("/")
    




