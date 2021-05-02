from db.db import db


class SituationType(db.Model):
    # TODO: カラムの宣言

    def to_dict(self):
        # TODO: to_dictの実装
        pass

    def __repr__(self):
        return '<SituationType %r>' % self.name

    def get_situation_type():
        # TODO: ここから実装
        pass
