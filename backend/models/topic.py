from db.db import db


class Topic(db.Model):
    message = db.Column(db.String(256), primary_key=True)

    def to_dict(self):
        return{'message': self.message,}

    def __repr__(self):
        return '<Topic %r>' % self.message

    def get_topic():
        topic_list = Topic.query.all()

        if topic_list ia None:
            return []
        return topic_list