from app import db


class Holiday(db.Model):
    __tablename__ = 'holidays'

   

    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String())
    date = db.Column(db.String())
    event = db.Column(db.String())

    def __init__(self, month, date, event):
        self.month = month
        self.date = date
        self.event = event

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id, 
            'month': self.month,
            'date': self.date,
            'event':self.event
        }

