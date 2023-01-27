from data import USERS, OFFERS, ORDERS
import classes_model


def users_list():
    """
    Получает данные в формате списка словарей,
    возвращает список экземпляров класса User
    """

    users_base = []
    for user in USERS:
        add_user = classes_model.User(
            id=user['id'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            age=user['age'],
            email=user['email'],
            role=user['role'],
            phone=user['phone'])
        users_base.append(add_user)

    return users_base


def orders_list():
    """
    Получает данные в формате списка словарей,
    возвращает список экземпляров класса Order
    """

    orders_base = []

    for order in ORDERS:
        add_order = classes_model.Order(
            id=order['id'],
            name=order['name'],
            description=order['description'],
            start_date=order['start_date'],
            end_date=order['end_date'],
            address=order['address'],
            price=order['price'],
            customer_id=order['customer_id'],
            executor_id=order['executor_id'])

        orders_base.append(add_order)

    return orders_base


def offers_list():
    """
    Получает данные в формате списка словарей,
    возвращает список экземпляров класса Offer
    """

    offers_base = []

    for offer in OFFERS:
        add_offer = classes_model.Offer(
            id=offer['id'],
            order_id=offer['order_id'],
            executor_id=offer['executor_id'])
        offers_base.append(add_offer)
    return(offers_base)


