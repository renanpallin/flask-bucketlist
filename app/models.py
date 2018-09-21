from app import db
from flask_bcrypt import Bcrypt

# class User(db.Model):
# 	"""This class defines the users table"""

# 	__table__ = 'users'

# 	id = db.Column(db.Integer, primary_key=True)
# 	email = db.Column(db.String(256), nullable=False, unique=True)
# 	password = db.Column(db.String(256), nullable=False)
# 	bucketlists = db.relationship('Bucketlist', order_by='Bucketlist.id', cascade="all, delete-orphan")

# 	def __init__(self, email, password):
# 		self.email = email
# 		self.password = password

# 	def password_is_valid(self, password):
# 		return Bcrypt().check_password_hash(self.password, password)

# 	def save(self):
# 		db.session.add(self)
# 		db.session.commit()


class SerializableModel(db.Model):

	def __call__(self):
		return {'a': 666}
	# def as_dict(self):
 #       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Bucketlist(SerializableModel):
	"""This class represents the bucketlist table."""

	__tablename__ = 'bucketlists'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(
		db.DateTime, default=db.func.current_timestamp(),
		onupdate=db.func.current_timestamp())
	# created_by = db.Column(db.Integer, db.ForeignKey(User.id))

	def __init__(self, name):
		"""Initialize with name."""
		self.name = name

	def save(self):
		db.session.add(self)
		db.session.commit()

	@staticmethod
	def get_all():
		return Bucketlist.query.all()

	def delete(self):
		db.session.delete(self)
		db.session.commit()

	def __repr__(self):
		return f"<Bucketlist: {self.name}>"