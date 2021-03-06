import csv
import os

from grocery_store import app, db
from grocery_store.models import User, Good, Store
from grocery_store.config import FIXTURES_DIR
from sqlalchemy_utils import create_database, drop_database, database_exists

USERS_DIR = os.path.join(FIXTURES_DIR, 'users.csv')
GOODS_DIR = os.path.join(FIXTURES_DIR, 'goods.csv')
STORE_DIR = os.path.join(FIXTURES_DIR, 'stores.csv')


def get_users():
    with open(USERS_DIR, 'r') as f:
        reader = csv.DictReader(f)
        users = [i for i in reader]
    return users


def get_goods():
    with open(GOODS_DIR, 'r') as f:
        reader = csv.DictReader(f)
        goods = [i for i in reader]
    return goods


def get_store():
    with open(STORE_DIR, 'r') as f:
        reader = csv.DictReader(f)
        items = [i for i in reader]
    return items


with app.app_context():
    if database_exists(db.engine.url):
        db.create_all()
        print('Database exists')
    else:
        print(f"Database does not exists {db.engine.url}")
        create_database(db.engine.url)
        print('Data base created')

with app.app_context():
    users = get_users()
    goods = get_goods()
    stores = get_store()
    for user in users:
        db.session.add(User(**user))
    for good in goods:
        db.session.add(Good(**good))
    for item in stores:
        db.session.add(Store(**item))
    db.session.commit()
    print('Data written in data_base succesfuly')