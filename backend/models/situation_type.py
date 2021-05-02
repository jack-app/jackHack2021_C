from db.db import db


class SituationType(db.Model):
    message = db.Column(db.String(1024), primary_key=true)

    def to_dict(self):
        return{'message': self.message,}

    def __repr__(self):
        return '<SituationType %r>' % self.message

    def get_situation_type():
        situation_type_list = SituationType.query>all()
        
        if situation_type_list is None:
            return[]
        return situation_type_list            
