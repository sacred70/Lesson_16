from flask import jsonify, request
from app_db import db, app
from data import USERS, OFFERS, ORDERS
from utils import users_list, orders_list, offers_list
from ddata_base import User, Offer, Order


# Создаем модели для пользователя, заказа и предложения. Добавляем методы для сериализации

# создаем таблицы и заполняем их данными
with app.app_context():
    db.create_all()


with app.app_context():
    db.session.add_all(users_list(User, USERS))
    db.session.add_all(orders_list(Order, ORDERS))
    db.session.add_all(offers_list(Offer, OFFERS))
    db.session.commit()


# Роуты для метода GET (все пользователи, пользователь по id, все заказы, заказы по id, все предложения,
# предложение по id
@app.get('/users/')
def get_all_users():
    users = User.query.all()
    result = []

    for user in users:
        result.append(user.get_user())

    return jsonify(result)


@app.get('/users/<int:id>/')
def get_user_by_id(id):
    user = User.query.get(id)
    if user is None:
        return 'Пользователь не существует'

    return jsonify(user.get_user())


@app.get('/orders/')
def get_all_orders():
    orders = Order.query.all()
    result = []

    for order in orders:
        result.append(order.get_order())

    return jsonify(result)


@app.get('/orders/<int:id>/')
def get_order_by_id(id):
    order = Order.query.get(id)
    if order is None:
        return 'Ордер не существует'

    return jsonify(order.get_order())


@app.get('/offers/')
def get_all_offers():
    offers = Offer.query.all()
    result = []

    for offer in offers:
        result.append(offer.get_offer())

    return jsonify(result)


@app.get('/offers/<int:id>/')
def get_offer_by_id(id):
    offer = Offer.query.get(id)
    if offer is None:
        return 'Предложение не существует'

    return jsonify(offer.get_offer())


# Роуты для добавления пользователя,
# обновления информации о пользователе,
# удалении пользователя
@app.route("/users/", methods=['POST'])
def add_user():
    data = request.json
    add_user = User(
        id=data.get('id'),
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        ge=data.get('age'),
        email=data.get('email'),
        role=data.get('role'),
        phone=data.get('phone'))
    db.session.add(add_user)
    db.session.commit()





@app.route("/users/<int:id>/", methods=['PUT'])
def update_user_by_id(id):
    data = request.json
    user = User.query.get(id)
    if user is None:
        return 'Пользователь не существует'
    user.id = data.get('id')
    user.first_name = data.get('first_name')
    user.last_name = data.get('last_name')
    user.age = data.get('age')
    user.email = data.get('email')
    user.role = data.get('role')
    user.phone = data.get('phone')
    db.session.add(user)
    db.session.commit()

    return f'Пользователь {id} обновлен'


@app.route("/users/<int:id>/", methods=['DELETE'])
def delete_user_by_id(id):
    user = User.query.get(id)
    if user is None:
        return 'User not found'
    db.session.delete(user)
    db.session.commit()

    return f'Пользователь {id} удален'


# Роуты для добавления заказа,
# обновления информации о заказе,
# удалении заказа
@app.route("/orders/", methods=['POST'])
def add_order():
    data = request.json
    add_order = Order(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        start_date=data.get('start_date'),
        end_date=data.get('end_date'),
        address=data.get('address'),
        price=data.get('price'),
        customer_id=data.get('customer_id'),
        executor_id=data.get('executor_id'))
    db.session.add(add_order)
    db.session.commit()
    return 'Ордер добавлен'




@app.route("/orders/<int:id>/", methods=['PUT'])
def update_order_by_id(id):
    data = request.json
    order = Order.query.get(id)
    if order is None:
        return 'Ордер не существует'

    order.id = data.get('id')
    order.name = data.get('name')
    order.description = data.get('description')
    order.start_date = data.get('start_date')
    order.end_date = data.get('end_date')
    order.address = data.get('address')
    order.price = data.get('price')
    order.customer_id = data.get('customer_id')
    order.executor_id = data.get('executor_id')
    db.session.add(order)
    db.session.commit()

    return f'Ордер {id} обновлен'


@app.route("/orders/<int:id>/", methods=['DELETE'])
def delete_order_by_id(id):
    order = Order.query.get(id)
    if order is None:
        return 'Ордер не существует'
    db.session.delete(order)
    db.session.commit()

    return f'Ордер {id} удален'


# Роуты для добавления предложения,
# обновления информации о предложении,
# удалении предложения
@app.route("/offers/", methods=['POST'])
def add_offer():
    data = request.json
    add_offer = Offer(
        id=data.get('id'),
        order_id=data.get('order_id'),
        executor_id=data.get('executor_id'))

    db.session.add(add_offer)

    db.session.commit()
    return 'Предложение добавлено'



@app.route("/offers/<int:id>/", methods=['PUT'])
def update_offer_by_id(id):
    data = request.json
    offer = Offer.query.get(id)
    if offer is None:
        return 'Предложение не существует'

    offer.id = data.get('id')
    offer.order_id = data.get('order_id')
    offer.executor_id = data.get('executor_id')

    db.session.add(offer)
    db.session.commit()

    return f'Предложение {id} обновлено'


@app.route("/offers/<int:id>/", methods=['DELETE'])
def delete_offer_by_id(id):
    offer = Offer.query.get(id)
    if offer is None:
        return 'Offer not found'
    db.session.delete(offer)
    db.session.commit()

    return f'Предложение {id} удалено'


if __name__ == '__main__':
    app.run()
