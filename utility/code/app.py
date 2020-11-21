from flask import Flask , request
from flask_restful import Resource, Api
import configparser
config = configparser.ConfigParser()
config.read('../config.ini')

app=Flask(__name__)
api=Api(app)


items=[]

print(config.sections())
class Datasource(Resource):
    def get(self, data):
        for item in items:
            if item["key"] == data:
                return item, 200
        return {"key" : None}, 404


    def post(self, data):
        data = request.get_json(force=True)
        item = {"key":data["key"],"value":data["value"]}
        items.append(item)
        return item , 201


    def delete(self, data):
        for i in range(len(items)):
            if items[i]['key'] == data:
                del items[i]
                break
        return {"status":"success"}, 200


class Alllist(Resource):
    def get(self):
        return {"items":items}

api.add_resource(Datasource,"/key/<string:data>")
api.add_resource(Alllist,"/alllist")

app.run(host='0.0.0.0',port=5000)
