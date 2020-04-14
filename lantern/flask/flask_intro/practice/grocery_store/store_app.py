from flask import Flask, jsonify, request

import inject


class NoSuchUserError(Exception):
    def __init__(self, user_id):
        self.message = f'No such user_id {user_id}'


class NoSuchStoreError(Exception):
    def __init__(self, store_id):
        self.message = f'No such store_id {store_id}'


class NoSuchManagerError(Exception):
    def __init__(self, manager_id):
        self.message = f'No such manager_id {manager_id}'


app = Flask(__name__)


@app.errorhandler(NoSuchUserError)
def my_error_handler(e):
    return jsonify({'error': e.message}), 404


@app.errorhandler(NoSuchStoreError)
def my_error_handler(e):
    return jsonify({'error': e.message}), 404


@app.errorhandler(NoSuchManagerError)
def my_error_handler(e):
    return jsonify({'error': e.message}), 404


@app.route('/users', methods=['POST'])
def create_user():
    db = inject.instance('DB')
    user_id = db.users.add_user(request.json)
    return jsonify({'user_id': user_id}), 201


@app.route('/users/<int:user_id>')
def get_user(user_id):
    db = inject.instance('DB')
    user = db.users.get_user_by_id(user_id)
    return jsonify(user)


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    db = inject.instance('DB')
    db.users.update_user_by_id(user_id, request.json)
    return jsonify({'status': 'success'}), 200


@app.route('/goods', methods=['POST'])
def create_goods():
    db = inject.instance('DB')
    count_id = db.goods.add_goods(request.json)
    return jsonify({'numbers of items created': count_id}), 200


@app.route('/goods')
def get_goods():
    db = inject.instance('DB')
    list_goods = db.goods.get_goods()
    return jsonify(list_goods)


@app.route('/goods', methods=['PUT'])
def update_goods():
    db = inject.instance('DB')
    successfully_updated, no_such_id_in_goods = db.goods.update_goods(request.json)
    return jsonify({'successfully_updated': successfully_updated,
                    'errors': {'no such id in goods': no_such_id_in_goods}})


@app.route('/store', methods=['POST'])
def create_store():
    db = inject.instance('DB')
    store_id = db.stores.add_store(request.json)
    return jsonify({'store_id': store_id})


@app.route('/store/<int:store_id>')
def get_store(store_id):
    db = inject.instance('DB')
    store = db.stores.get_store_by_id(store_id)
    return jsonify(store)


@app.route('/store/<int:store_id>', methods=['PUT'])
def update_store(store_id):
    db = inject.instance('DB')
    db.stores.update_store_by_id(store_id, request.json)
    return jsonify({'status': 'success'})
