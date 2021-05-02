from db.db import db


class Topic(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(256))
    situation_type_id = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "stuation_type_id": self.situation_type_id
        }

    def __repr__(self):
        return '<Topic %r>' % self.name

    def get_topics():
        topic_list = Topic.query.all()

        if topic_list is None:
            return []
        return topic_list

    def post_topic(self):
        new_topic = self

        db.session.add(new_topic)
        db.session.flush()
        db.session.commit()

        return new_topic.id
