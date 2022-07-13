from app import db
from app.module_messages.models import Message
from flask import request, Blueprint

mod_messages = Blueprint('messages', __name__, url_prefix='/message')

@mod_messages.route('', methods=['POST'])
def send_message():
    content = request.form['content']
    topic = request.form['topic']

    if not content or not topic:
        return {'status': 'fail'}

    entry = Message(content, topic)
    db.session.add(entry)
    db.session.commit()

    return {'status': 'ok'}


@mod_messages.route('/<topic>', methods=['GET'])
def get_messages(topic):
    result = [row.to_json() for row in db.session.query(Message).filter_by(topic=topic)]
    return {'data': result}
