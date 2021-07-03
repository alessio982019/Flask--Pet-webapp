
from datetime import datetime
from flask.helpers import send_file
from sqlalchemy.orm import relationship, backref
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from main import login_manager,db,app
from sqlalchemy import func
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property


@login_manager.user_loader
def load_user(user_id):
    return  User.query.get(int(user_id))

class Category(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return "Category('{self.id}','{self.name}')"



class Post(db.Model, UserMixin):
    __tablename__ = 'Post'
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    title = db.Column(db.String(60), nullable=False)
    text = db.Column(db.String(200), nullable=False)
    active = db.Column(db.Boolean, default=True,nullable=False)
    picture = db.Column(db.String(60),default='Default.jpeg')
    author_id = db.Column(db.Integer(), db.ForeignKey("User.id"))
    type = db.Column(db.String(60), nullable=False)
    category = db.Column(db.String(60), nullable=False)
    author = relationship('User', foreign_keys=author_id)
    location = db.Column(db.String(60), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 
    likes = db.relationship('Likes', backref='Post', lazy='dynamic')
    def __repr__(self):
        return "Post('ID: ,{},TITLE '{}',TEXT '{}', ACTIVE '{}'')".format(self.id,self.title,self.text,self.active)


class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String(50),  nullable=False)
    lastname = db.Column(db.String(50),  nullable=False)
    email = db .Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(1000),nullable=False)
    address = db.Column(db.String(50),  nullable=False)
    city = db.Column(db.String(50),  nullable=False)
    country = db.Column(db.String(50),  nullable=False)
    zip_code = db.Column(db.String(50),  nullable=False)
    verified = db.Column(db.Boolean,nullable=False,default=False)
    picture = db.Column(db.String(50),nullable=False,default="ProfileDefault.png")
    type = db.Column(db.String(50),  nullable=False)
    post = db.relationship('Post', backref='Post.author_id', passive_deletes=True)
    post_liked = db.relationship('Likes',foreign_keys='Likes.user_id',backref='user', lazy='dynamic')
    def like_post(self, post):
        if not self.has_liked_post(post):
            like = Likes(user_id=self.id, post_id=post.id)
            db.session.add(like)
    def unlike_post(self, post):
        if self.has_liked_post(post):
            Likes.query.filter_by(
                user_id=self.id,
                post_id=post.id).delete()

    def has_liked_post(self, post):
        return Likes.query.filter(
            Likes.user_id == self.id,
            Likes.post_id == post.id).count() > 0

    def get_reset_token(self,expires_sec = 1800):
        s = Serializer(app.config['SECRET_KEY'],expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
    def __repr__(self):
        return "User('{}','{}','{}','{}','{}')".format(self.id,self.firstname,self.email,self.verified,self.picture)

class Likes(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('Post.id'))


    def __repr__(self):
        return "Like('ID: ,{},USER ID '{}',POST ID '{}'')".format(self.id,self.user_id,self.post_id)


class Product(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    productname = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    category = db.Column(db.String(500), nullable=False)
    quantity = db.Column(db.Numeric(10,2), nullable=False)
    details = db.Column(db.String(500), nullable=False)
    active = db.Column(db.Boolean, default=True,nullable=False)
    image1 = db.Column(db.String(60),nullable=False,default='ProductDefault.jpeg')
    image2 = db.Column(db.String(60),nullable=True)
    image3 = db.Column(db.String(60),nullable=True)
    image4 = db.Column(db.String(60),nullable=True)
    image5 = db.Column(db.String(60),nullable=True)
    premium = db.Column(db.Boolean, default=True,nullable=False)
    product_price_key = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return "Post('ID: ,{},NAME '{}',TEXT '{}',PRICE '{}', AVAILABILITY '{}', ACTIVE '{}', PREMIUM '{}')".format(self.id,self.productname,self.description,self.price,self.quantity,self.active,self.premium)



class Orders(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    customerID = db.Column(db.Integer,nullable=False)
    productID = db.Column(db.Integer,nullable=False)
    quantity = db.Column(db.Numeric(10,2), nullable=False)
    total_price = db.Column(db.Numeric(10,2), nullable=False)
    stripe_session_id = db.Column(db.String(200),nullable=True)
