from json import dumps
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .utils import timestamp


class User(db.Model):
    """The User model"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), nullable=False, unique=True)
    created_at = db.Column(db.Integer, default=timestamp)
    password_hash = db.Column(db.String(256), nullable=False)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Export user to a dictionary."""
        return {
            'id': self.id,
            'email': self.email,
            'created_at': self.created_at
        }

    @staticmethod
    def create(email, password):
        user = User()
        user.password_hash = generate_password_hash(password)
        user.email = email
        return user

    @staticmethod
    def get_user(email, password):
        for user in User.query.all():
            if user.email == email and user.verify_password(password):
                return user

    def __repr__(self):
        return dumps(self.to_dict())

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
