from app import db


class Author(db.Model):
    __tablename__ = 'authors'
    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    bio = db.Column(db.Text)
    def dict(self):
        return {
            'author_id': self.author_id,
            'name': self.name,
            'bio': self.bio
        }