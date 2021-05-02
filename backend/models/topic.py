from db.db import db


class Topic(db.Model):
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    name = db.Column(db.String(256))

    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,}

    def __repr__(self):
        return '<Topic %r>' % self.message

    def get_topic():
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