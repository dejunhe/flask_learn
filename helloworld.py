# -*- coding:utf-8 -*-

# @Time     : 2020/8/19 22:20
# @Verson   :
# @Author   : jun
# @Site     : 
# @File     : helloworld.py
# @Software : PyCharm
from flask import Flask
from blueprint_demo import user_bp
from goods import goods_bp

#
# class DefaultConfig(object):
#     SECRET_KEY = 'heljlljaljaf'


app = Flask(__name__)

# app.config.from_object(DefaultConfig)
app.config.from_pyfile('config.py')
app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(goods_bp, url_prefix='/goods')


@app.route('/')
def index():
    print(app.config['SECRET_KEY'])
    return 'hello,world'


# app.config.get(name)
# app.config[name]

if __name__ == '__main__':
    # print(app.config)
    print(app.url_map)
    app.run(debug=True)
