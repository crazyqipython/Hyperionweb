import app 
from app import db






basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' +os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_DATABASE_ON_TEARDOWN'] = True




class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Interger, primary_key = True)
	name = db.Column(db.String, unique = True)
	users = db.relationship('User', backref = 'role')
	
	def __repr__(self):
		return '<role, %r>' %self.name
	

class User(db.Model):
	__tablename__ = 'users'
	
	id = db.Column(db.Interger, primary_key = True)
	username = db.Column(db.String(40), unique = True)
	role_id = db.Column(db.Interger, db.ForeignKey('roles.id')
	
	# def __repr__(self):
		# return '<user %r>' %self.username