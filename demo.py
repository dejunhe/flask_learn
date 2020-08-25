# -*- coding:utf-8 -*-

# @Time     : 2020/8/23 20:00
# @Verson   :
# @Author   : jun
# @Site     : 
# @File     : demo.py
# @Software : PyCharm

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorldResource(Resource):
    def get(self):
        return {"hello": "world"}

    def post(self):
        return {'msg': 'post hello world'}


api.add_resource(HelloWorldResource, '/')

if __name__ == '__main__':
    app.run(debug=True)
