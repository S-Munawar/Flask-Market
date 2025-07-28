from app import app, db
from app.models import Item

with app.app_context():
    # This will create all the tables defined in your models
    db.create_all()

    # Now, you can add your initial data
    item1 = Item(name="Phone", price=500, barcode="893212299897", description="New iPhone 10")
    item2 = Item(name="Laptop", price=900, barcode="123985473165", description="New MacBook Air")
    item3 = Item(name="Keyboard", price=150, barcode="231985128446", description="Wired keyboard")

    # Check if the items already exist before adding them
    if not Item.query.filter_by(name="Phone").first():
        db.session.add(item1)
    if not Item.query.filter_by(name="Laptop").first():
        db.session.add(item2)
    if not Item.query.filter_by(name="Keyboard").first():
        db.session.add(item3)

    db.session.commit()

print("Database created and populated successfully!")