import inject

from store_app import app
from fake_storage import FakeStorage


def configure_test(binder):
    db = FakeStorage()
    binder.bind('DB', db)


class Initializer:
    def setup(self):
        inject.clear_and_configure(configure_test)

        app.config['TESTING'] = True
        with app.test_client() as client:
            self.client = client


class TestUsers(Initializer):
    def test_create_new(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        assert resp.status_code == 201
        assert resp.json == {'user_id': 1}

        resp = self.client.post(
            '/users',
            json={'name': 'Andrew Derkach'}
        )
        assert resp.json == {'user_id': 2}

    def test_successful_get_user(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.get(f'/users/{user_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'John Doe'}

    def test_unsuccessful_get_user(self):
        resp = self.client.get(f'/users/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}

    def test_successful_update_user(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.put(
            f'/users/{user_id}',
            json={'name': 'Johnna Doe'}
        )
        assert resp.status_code == 200
        assert resp.json == {'status': 'success'}

    def test_unsuccessful_update_user(self):
        resp = self.client.put(
            '/users/1',
            json={'name': 'Johnna Doe'}
        )
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}


class TestGoods(Initializer):
    def test_create_new_goods(self):
        resp = self.client.post(
            '/goods',
            json=[{'name': 'Chocolate bar', 'price': 10},
                  {'name': 'Pepsi', 'price': 30},
                  {'name': 'Coca Cola', 'price': 32},
                  {'name': 'Fanta', 'price': 31},
                  {'name': 'Sprite', 'price': 30},
                  {'name': 'Coffee', 'price': 75},
                  {'name': 'Juice', 'price': 45},
                  {'name': 'Buckwheat', 'price': 29},
                  {'name': 'Bread', 'price': 16},
                  {'name': 'Dr Pepper', 'price': 35}
                  ]
        )
        assert resp.status_code == 200
        assert resp.json == {'numbers of items created': 10}

    def test_get_goods(self):
        self.client.post(
            '/goods',
            json=[{'name': 'Chocolate bar', 'price': 10},
                  {'name': 'Pepsi', 'price': 30},
                  {'name': 'Coca Cola', 'price': 32},
                  {'name': 'Fanta', 'price': 31},
                  {'name': 'Sprite', 'price': 30},
                  ]
        )
        resp = self.client.get('/goods')
        assert resp.status_code == 200
        assert resp.json == [{'name': 'Chocolate bar', 'price': 10, 'id': 1},
                             {'name': 'Pepsi', 'price': 30, 'id': 2},
                             {'name': 'Coca Cola', 'price': 32, 'id': 3},
                             {'name': 'Fanta', 'price': 31, 'id': 4},
                             {'name': 'Sprite', 'price': 30, 'id': 5}]

    def test_update_goods(self):
        self.client.post(
            '/goods',
            json=[{'name': 'Chocolate bar', 'price': 10},
                  {'name': 'Pepsi', 'price': 30},
                  {'name': 'Coca Cola', 'price': 32},
                  {'name': 'Fanta', 'price': 31},
                  {'name': 'Sprite', 'price': 30},
                  ]
        )
        resp = self.client.put(
            '/goods',
            json=[{'name': 'Chocolate candy', 'price': 5, 'id': 1},
                  {'name': 'Pepsi', 'price': 32, 'id': 2},
                  {'name': 'Coca Cola', 'price': 25, 'id': 3},
                  {'name': 'Bread', 'price': 16, 'id': 9},
                  {'name': 'Dr Pepper', 'price': 35, 'id': 7},
                  {'name': 'Buckwheat', 'price': 29, 'id': 6},
                  ]
        )
        assert resp.status_code == 200
        assert resp.json == {'successfully_updated': 3, 'errors': {'no such id in goods': [9, 7, 6]}}


class TestStores(Initializer):
    def test_create_store(self):
        self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 1})
        assert resp.json == {'store_id': 1}
        assert resp.status_code == 200

    def test_unsuccessful_create_store(self):
        self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2})
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such manager_id 2'}

    def test_successful_get_store(self):
        self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 1})
        resp = self.client.get('/store/1')
        assert resp.status_code == 200
        assert resp.json == {'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 1}

    def test_unsuccessful_get_store(self):
        self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 1})
        resp = self.client.get('/store/2')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such store_id 2'}

    def test_successful_update_store(self):
        self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 1})
        resp = self.client.put('/store/1',
                               json={'name': 'Local Taste', 'location': 'Lviv', 'manager_id': 1})
        assert resp.status_code == 200
        assert resp.json == {'status': 'success'}

    def test_unsuccessful_update_store_with_store_id(self):
        self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 1})
        resp = self.client.put('/store/2',
                               json={'name': 'Local Taste', 'location': 'Lviv', 'manager_id': 1})
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such store_id 2'}

    def test_unsuccessful_update_store_with_manager_id(self):
        self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 1})
        resp = self.client.put('/store/1',
                               json={'name': 'Local Taste', 'location': 'Lviv', 'manager_id': 2})
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such manager_id 2'}