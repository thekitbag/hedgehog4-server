from webapp import db

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(32))
    name = db.Column(db.String(128))

    def __repr__(self):
        return f'<Project {self.id}  {self.title}>'