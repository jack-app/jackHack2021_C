from db.db import db


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(128))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }

    def __repr__(self):
        return '<User %r>' % self.name

    def get_users():
        user_list = User.query.all()

        if user_list is None:
            return []
        return user_list

    def post_user(self):
        new_user = self

        db.session.add(new_user)
        db.session.flush()
        db.session.commit()

        return new_user.id
