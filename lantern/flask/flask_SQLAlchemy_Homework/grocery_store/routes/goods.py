from flask import request
from flask_restful import Resource, marshal

from grocery_store.models import Good
from grocery_store.db import db
from grocery_store.routes.marshal_structure import goods_structure


class Goods(Resource):

    def get(self, good_id=None):
        if good_id:
            good = Good.query.get(good_id)
            if good:
                return marshal(good, goods_structure)
            return f"No such good with id: {good_id}"
        return marshal(Good.query.all(), goods_structure)

    def post(self):
        temp_list_goods = request.json
        for item in temp_list_goods:
            temp = Good(**item)
            db.session.add(temp)
        db.session.commit()
        return f"Numbers of items created {len(temp_list_goods)}"

    def put(self):
        temp_list_goods = request.json
        for temp in temp_list_goods:
            item = Good.query.get(temp['good_id'])
            item.brand = temp['brand']
            item.name = temp['name']
            item.price = temp['price']
        db.session.commit()
        return f"Numbers of items updated {len(temp_list_goods)}"

    def delete(self):
        temp_list_goods = request.json
        for temp in temp_list_goods:
            item = Good.query.get(temp['good_id'])
            db.session.delete(item)
        db.session.commit()
        return f"Numbers of items deleted: {len(temp_list_goods)}"
