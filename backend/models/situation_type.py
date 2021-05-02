from db.db import db


class SituationType(db.Model):
    
    id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    name = db.Column(db.String(1024))

    def to_dict(self):
    
        return{"id": self.id,
            "name": self.name,}

    def __repr__(self):
        return '<SituationType %r>' % self.name

    def get_situation_type():
        situation_type_list = SituationType.query>all()
        
        if situation_type_list is None:
            return[]
        return situation_type_list            
    
    def post_situation_type(self):
        new_situation_type = self

        db.session.add(new_situation_type)
        db.session.flush()
        db.session.commit()

        return new_situation_type.id