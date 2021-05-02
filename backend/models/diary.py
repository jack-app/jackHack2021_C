from db.db import db
from sqlalchemy.sql.expression import text


class Diary(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(128))
    content = db.Column(db.String(4096))
    user_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=text("NOW()"))

    def to_dict(self):
        return{"id": self.id,
               "title": self.title, "content": self.content, "user_id": self.user_id, "created_at": self.created_at}

    def __repr__(self):
        return '<Diary %r>' % self.name

    def get_diarys():
        diarys_list = Diary.query.all()

        if diarys_list is None:
            return []
        return diarys_list

    def get_diary(id):
        diary = Diary.query.filter(Diary.id == id).one()

        return diary

    def post_diary(self):
        new_diary = self

        db.session.add(new_diary)
        db.session.flush()
        db.session.commit()

        return new_diary.id
