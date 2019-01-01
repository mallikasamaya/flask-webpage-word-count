from app import db

class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100))
    result_words = db.Column(db.Integer)
    status_code = db.Column(db.Integer)

    def __init__(self, url, result_words, status_code):
        self.url = url
        self.result_words = result_words
	self.status_code = status_code	

    def __repr__(self):
        return '<id {}>'.format(self.id)
