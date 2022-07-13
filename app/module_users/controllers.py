from app import db
from app.module_users.models import User
from flask import render_template, request, Blueprint

mod_users = Blueprint('users', __name__, url_prefix='/user')

@mod_users.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = []

        for result in db.engine.execute(f"SELECT * FROM people WHERE pname='{username}'"):
            if (result[2] != password):
                return {'status': 'fail'}
            else:
                return {'status': 'ok'}
        if(len(result) == 0):
            message = 'Invalid user'

    return {'status': 'fail'}


@mod_users.route("/signup", methods=['POST'])
def signup():
    username = request.form["username"]
    password = request.form["password"]
    entry = User(username, password)
    db.session.add(entry)
    db.session.commit()

    return {'status': 'ok'}

