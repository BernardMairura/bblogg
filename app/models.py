from .import db,admin
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer
from flask_login import UserMixin
from datetime import datetime   
from .import login_manager
from flask_admin.contrib.sqla import ModelView



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    __tablename__ ='users'

    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    bio = db.Column(db.String(255))
    password_secure = db.Column(db.String(255))



    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)




class Blog(db.Model):

    __tablename__ ='blogs'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    body=db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


admin.add_view(ModelView(Blog, db.session))
admin.add_view(ModelView(User, db.session))