from app import db
from app import bcrypt
from app import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id): # This function is used to load the user by the user_id
    return User.query.get(int(user_id))

# SQLAlchemy’s underlying Model class supports keyword arguments matching column names.
class User(db.Model, UserMixin): # Creating a User class which inherits from db.Model, where Model is a class in SQLAlchemy which is a base class for all models in SQLAlchemy. Here Model class is being accessed through db object.
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=10000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    # Transforming the password into a hashed password using the bcrypt library and storing it in the password_hash column.
    # Getters and setters are essential when you need to control access or add logic for attribute management.
    @property # This decorator allows you to access the method (password) as if it were an attribute. It allows you to use @password.setter or @password.deleter
    def password(self):
        raise AttributeError("Password cannot be accessed directly.")

    @password.setter # When you assign a value to the password attribute (e.g., user_to_create.password = form.password1.data), the setter is called.
    def password(self, plain_text_password): # Function name should be the same as the property name.
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    # Alternatively, you can create a method to set the password. 1st block should be in routes.py and 2nd block should be in models.py.

    # user_to_create = User(username=form.username.data,
    #                       email_address=form.email_address.data)
    # user_to_create.set_password(form.password1.data)

    # def set_password(self, plain_text_password):
    #     self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password): # This function is used to check if the password entered by the user is correct or not.
        return bcrypt.check_password_hash(self.password_hash, attempted_password) # Returns True & False.

    @property # This decorator allows you to access the method (prettier_budget) as if it were an attribute. 
    def prettier_budget(self): # This function is used to display the budget in a prettier format.
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f"{self.budget}$"

    def __repr__(self): # __repr__ is a built-in function used to compute the “official” string reputation of an object.
        return f"{self.username}"

    @property
    def is_admin(self):
        return self.username == "Shaik"


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f"{self.name}"

    def buy(self, user):
        self.owner = user.id
        user.budget -= self.price
        db.session.commit()

    def sell(self, user):
        self.owner = None
        user.budget += self.price
        db.session.commit()