from db.db import db


class Topic(db.Model):
    # TODO: カラムの宣言

    def to_dict(self):
        # TODO: to_dictの実装
        pass

    def __repr__(self):
        return '<Topic %r>' % self.name

    def get_topic():
        # TODO: ここから実装
        pass
