from db.db import db


class Diary(db.Model):
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    title = db.Column(db.String(128))
    content = db.Column(db.String(4096))
    user_id = db.Column(db.Integer)
    timestamp =db.Column(db.Timestamp)

def to_dict(self):
    return{"id": self.id,
    "name":self.name,}

def __repr__(self):
    return '<Diary %r>' % self.name

def get_diarys():
    diarys_list = Diarys.query.all()    

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