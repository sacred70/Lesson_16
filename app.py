from functions import users_list, orders_list, offers_list
from main import db, app



with app.app_context():
    db.session.add_all(users_list())
    db.session.add_all(orders_list())
    db.session.add_all(offers_list())
    db.session.commit()
print(db)