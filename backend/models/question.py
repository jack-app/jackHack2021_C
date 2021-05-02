from db.db import db


class Question(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    topic_id = db.Column(db.Integer)
    situation_type_id = db.Column(db.Integer)
    content = db.Column(db.String(4096))

    def to_dict(self):
        return {
            "id": self.id,
            "topic_id": self.topic_id,
            "situation_type_id": self.situation_type_id,
            "content": self.content
        }

    def get_questions(topic_id):
        question_list = Question.query.filter(Question.topic_id == topic_id)

        return question_list
