# # -*- coding:utf-8 -*-
#
# # @Time     : 2020/8/20 23:50
# # @Verson   :
# # @Author   : jun
# # @Site     :
# # @File     : 01_url_param.py
# # @Software : PyCharm
#
# from flask import Flask
#
# from werkzeug.routing import BaseConverter
#
# app = Flask(__name__)
#
#
# @app.route('/users/<int:user_id>')
# def get_users_data(user_id):
#     print(type(user_id))
#     return 'get users {}'.format(user_id)
#
#
# class MobileConverter(BaseConverter):
#     regex = r'1[3-9]\d{9}'
#
#
# app.url_map.converters['mobile'] = MobileConverter
#
#
# @app.route('/sms_codes/<mobile:mob_num>')
# def send_sms_code(mob_num):
#     print(type(mob_num))
#     return 'send sms code to {}'.format(mob_num)
#
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
