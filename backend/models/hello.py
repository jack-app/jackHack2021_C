from db.db import db


class Hello(db.Model):
    message = db.Column(db.String(64), primary_key=True)

    def to_dict(self):
        return {
            'message': self.message,
        }

    def __repr__(self):
        return '<Hello %r>' % self.message

    def getHello():
        hello_list = Hello.query.all()

        if hello_list is None:
            return []
        return hello_list
