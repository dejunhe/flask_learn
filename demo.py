# -*- coding:utf-8 -*-

# @Time     : 2020/8/23 20:00
# @Verson   :
# @Author   : jun
# @Site     : 
# @File     : demo.py
# @Software : PyCharm

from flask import Flask, request, abort, g

# from passport import bp

#
# app1 = Flask(__name__)
# app2 = Flask(__name__)
# # app.confit["itcast"] = 'python'
# app1.redis_cli = 'redis client 1'
# app2.redis_cli = 'redis client 2'
#
# # app.register_blueprint(bp)
#
#
# @app1.route('/app1')
# def get_articles():
#
#     return ''

app = Flask(__name__)


def db_query():
    user_id = g.user_id
    user_name = g.user_name
    print('user_id={} user_name={}'.format(user_id, user_name))


@app.route('/')
def get_user_profile():
    g.user_id = 123
    g.user_name = 'itcast'
    db_query()
    return 'hello world'


if __name__ == '__main__':
    app.run()
