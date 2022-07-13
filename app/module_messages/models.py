from app import db

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

