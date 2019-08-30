# database'i project dizini içerisindeki __init__ dosyasında ayarlayacağız
from project import db


class Ponny(db.Model):
    __tablename__ = 'ponnies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='ponny', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Ponny name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Ponny name is {self.name} and has no owner yet!"


class Owner(db.Model):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    ponny_id = db.Column(db.Integer, db.ForeignKey('ponnies.id'))

    def __init__(self, name, ponny_id):
        self.name = name
        self.ponny_id = ponny_id


if __name__ == "__main__":
    app.run(debug=True)
