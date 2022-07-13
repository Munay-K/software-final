from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://munay:No7854@localhost/postgres'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)

from app.module_messages.controllers import mod_messages
from app.module_users.controllers import mod_users

app.register_blueprint(mod_messages)
app.register_blueprint(mod_users)

if __name__ == '__main__':
    db.create_all()
    app.run()

