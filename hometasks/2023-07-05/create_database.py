import datetime
from models.database import create_db, engine
from models.salesmen import Salesman
from models.sales import Sale
from models.customers import Customer


def create_database(session):
    create_db()

    populate_salesmen = [
        {'sname': 'Beckson', 'margin': 2.52, 'city': 'Birmingham'},
        {'sname': 'Rukkunen', 'margin': 1.85, 'city': 'Turku'},
        {'sname': 'Wurz', 'margin': 1.77, 'city': 'Dortmund'},
        {'sname': 'Lopez', 'margin': 2.21, 'city': 'Sevilla'},
        {'sname': 'Boulanger', 'margin': 3.13, 'city': 'Nantes'}
    ]

    populate_customers = [
        {'cname': 'Fedorov', 'rating': 4.2, 'city': 'Moscow', 'sid': 1},
        {'cname': 'Kagawa', 'rating': 3.8, 'city': 'Yokohama', 'sid': 5},
        {'cname': 'Schmidt', 'rating': 4.5, 'city': 'Dortmund', 'sid': 3},
        {'cname': 'Dubois', 'rating': 4.6, 'city': 'Nantes', 'sid': 4},
        {'cname': 'Johnson', 'rating': 3.7, 'city': 'New York', 'sid': 2},
        {'cname': 'Zhukov', 'rating': 4.1, 'city': 'Saint Petersburg', 'sid': 1},
        {'cname': 'Yamamoto', 'rating': 3.9, 'city': 'Tokyo', 'sid': 3}
    ]

    populate_sales = [
        {'sid': 1, 'cid': 1, 'amount': 500, 'date': datetime.datetime(2023, 1, 5)},
        {'sid': 5, 'cid': 2, 'amount': 750, 'date': datetime.datetime(2023, 2, 10)},
        {'sid': 3, 'cid': 3, 'amount': 1200, 'date': datetime.datetime(2023, 3, 15)},
        {'sid': 4, 'cid': 4, 'amount': 900, 'date': datetime.datetime(2023, 4, 20)},
        {'sid': 2, 'cid': 5, 'amount': 600, 'date': datetime.datetime(2023, 5, 25)},
        {'sid': 1, 'cid': 6, 'amount': 1100, 'date': datetime.datetime(2023, 6, 30)},
        {'sid': 3, 'cid': 7, 'amount': 800, 'date': datetime.datetime(2023, 7, 5)},
        {'sid': 3, 'cid': 7, 'amount': 950, 'date': datetime.datetime(2023, 8, 10)},
        {'sid': 4, 'cid': 4, 'amount': 700, 'date': datetime.datetime(2023, 9, 15)},
        {'sid': 5, 'cid': 2, 'amount': 850, 'date': datetime.datetime(2023, 10, 20)}
    ]

    with engine.begin() as conn:
        conn.execute(Salesman.__table__.insert().values(populate_salesmen))
        conn.execute(Customer.__table__.insert().values(populate_customers))
        conn.execute(Sale.__table__.insert().values(populate_sales))

    session.commit()
    session.close()
