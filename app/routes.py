from app import app, db # Importing the app & db variable from the app package directly because they are defined in __init__.py
from flask import render_template, redirect, url_for, flash, request
from app.models import Item, User
from app.forms import RegisterForm, LoginForm, PurchaseForm, SellForm, AddItems
from flask_login import login_user, logout_user, login_required, current_user

# This is a route decorator. It tells Flask that the function below should be called when the user visits the specified route.
# In this case, the user is visiting the home_page in both the cases. (localhost:5000/ and localhost:5000/home)
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market', methods=['GET', 'POST'])
@login_required
def market_page():
    purchase_form = PurchaseForm()
    selling_form = SellForm()
    if request.method == "POST":
        # Purchase Item Logic
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.budget >= p_item_object.price:
                p_item_object.buy(current_user)
                flash(f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$",
                      category='success')
            else:
                flash(f"Insufficient balance! You can't afford {p_item_object.name}", category='danger')
        # Selling Item Logic
        sold_item = request.form.get('sold_item')
        s_item_object = Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            if s_item_object.owner == current_user.id:
                s_item_object.sell(current_user)
                flash(f"Congratulations! You sold {s_item_object.name} back to the app.", category='success')
            else:
                flash(f"Something went wrong with selling {s_item_object.name}", category='danger')
        return redirect(url_for('market_page'))

    if request.method == "GET":
        owned_items = Item.query.filter_by(owner=current_user.id)  # Return a list of all the rows in the table(Item) from the database(app.db) where the owner is the current user.
        items = Item.query.filter_by(owner=None) # Return a list of all the rows in the table(Item) from the database(app.db) where the owner is None.
        return render_template('market.html', items=items, purchase_form=purchase_form, selling_form=selling_form,
                               owned_items=owned_items)


@app.route('/register', methods=['GET', 'POST']) # When the user fills out the form and clicks "Submit," the browser sends a POST request to the same /register endpoint.
def register_page():
    form = RegisterForm() # Creating an instance of the RegisterForm class(forms.py)
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data) # Creating an instance of the User class(models.py) with the data from the form.
        db.session.add(user_to_create) # Adding the user_to_create instance to the database session
        db.session.commit() # Committing the changes to the database
        login_user(user_to_create) # Logging in the user
        flash(f'Account created successfully! You are now logged in as: {user_to_create.username}', category='success')
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user:
            if attempted_user.check_password_correction(attempted_password=form.password.data):
                login_user(attempted_user)
                flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
                return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user() # Logging out the user
    flash("You have been logged out!", category='info')
    return redirect(url_for('home_page'))

@app.route('/admin', methods=['GET', 'POST'])
def admin_page():
    form = AddItems()
    purchase_form = PurchaseForm()
    if request.method == "POST":
        if form.validate_on_submit():
            item_to_create = Item(name=form.name.data,
                                  price=form.price.data,
                                  barcode=form.barcode.data,
                                  description=form.description.data)
            db.session.add(item_to_create)
            db.session.commit()
            flash(f'The item {item_to_create.name} has been added to the app!', category='success')
        return redirect(url_for('admin_page'))
    if request.method == "GET":
        items = Item.query.filter_by(owner=None)
        return render_template('admin.html', items=items, form=form, purchase_form=purchase_form)