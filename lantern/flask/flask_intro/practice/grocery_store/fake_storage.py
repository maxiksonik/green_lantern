from itertools import count
from store_app import NoSuchUserError, NoSuchStoreError, NoSuchManagerError


class Init:
    def __init__(self):
        self._object = {}
        self._id_counter = count(1)


class FakeStorage:
    def __init__(self):
        self._users = FakeUsers()
        self._goods = FakeGoods()
        self._stores = FakeStores(list_id=self._users.get_list_id())

    @property
    def users(self):
        return self._users

    @property
    def goods(self):
        return self._goods

    @property
    def stores(self):
        return self._stores


class FakeUsers(Init):

    def add_user(self, user):
        user_id = next(self._id_counter)
        self._object[user_id] = user
        return user_id

    def get_user_by_id(self, user_id):
        try:
            return self._object[user_id]
        except KeyError:
            raise NoSuchUserError(user_id)

    def update_user_by_id(self, user_id, user):
        if user_id in self._object:
            self._object[user_id] = user
        else:
            raise NoSuchUserError(user_id)

    def get_list_id(self):
        return self._object.keys()


class FakeGoods(Init):

    def add_goods(self, goods):
        for i in goods:
            goods_id = next(self._id_counter)
            self._object[goods_id] = i
        return len(goods)

    def get_goods(self):
        list_goods = []
        for i in self._object:
            temp = self._object[i]
            temp['id'] = i
            list_goods.append(temp)
        return list_goods

    def update_goods(self, goods):
        successfully_updated = 0
        no_such_id_in_goods = []
        for i in goods:
            if i['id'] in self._object:
                temp_id = i['id']
                del i['id']
                self._object[temp_id] = i
                successfully_updated += 1
            else:
                no_such_id_in_goods.append(i['id'])
        return successfully_updated, no_such_id_in_goods


class FakeStores(Init):
    def __init__(self, list_id):
        super().__init__()
        self.list_id = list_id

    def add_store(self, store):
        if store['manager_id'] in self.list_id:
            store_id = next(self._id_counter)
            self._object[store_id] = store
            return store_id
        else:
            raise NoSuchManagerError(store['manager_id'])

    def get_store_by_id(self, store_id):
        try:
            return self._object[store_id]
        except KeyError:
            raise NoSuchStoreError(store_id)

    def update_store_by_id(self, store_id, store):
        if store['manager_id'] in self.list_id:
            if store_id in self._object:
                self._object[store_id] = store
            else:
                raise NoSuchStoreError(store_id)
        else:
            raise NoSuchManagerError(store['manager_id'])
