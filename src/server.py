from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://munay:No7854@localhost/postgres'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),  nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500),  nullable=False)
    topic = db.Column(db.String(200), nullable=False)

    def __init__(self, content, topic):
        self.content = content
        self.topic = topic

    def to_json(self):
        return {
            'content': self.content,
            'topics': self.topic
        }


@app.route('/')
def home():
    return '<a href="/index"><button> Click here </button></a>'


@app.route("/signup")
def signup():
    return render_template("create_user.html")


@app.route('/message', methods=['POST'])
def send_message():
    content = request.form['content']
    topic = request.form['topic']

    if not content or not topic:
        return {'status': 'fail'}

    entry = Message(content, topic)
    db.session.add(entry)
    db.session.commit()

    return {'status': 'ok'}


@app.route('/message/<topic>', methods=['GET'])
def get_messages(topic):
    result = [row.to_json() for row in db.session.query(Message).filter_by(topic=topic)]
    return {'data': result}


@app.route('/index', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = []

        for result in db.engine.execute(f"SELECT * FROM people WHERE pname='{username}'"):
            print(result)
            print(result[0])
            print(result[1])
            if (result[2] != password):
                message = 'Error: Invalid password. Please try again.'
            else:
                message = 'Success: Login Sucessful.'
        if(len(result) == 0):
            message = 'Invalid user'
    return render_template('login.html', message=message)


@app.route("/adduser", methods=['POST'])
def adduser():
    username = request.form["username"]
    password = request.form["password"]
    entry = User(username, password)
    db.session.add(entry)
    db.session.commit()

    return render_template("index.html")


if __name__ == '__main__':
    db.create_all()
    app.run()

