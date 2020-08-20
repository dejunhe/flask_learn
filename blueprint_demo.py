# -*- coding:utf-8 -*-

# @Time     : 2020/8/20 23:08
# @Verson   :
# @Author   : jun
# @Site     : 
# @File     : blueprint_demo.py
# @Software : PyCharm

from flask import Blueprint

user_bp = Blueprint("user", __name__)


@user_bp.route('/profile')
def get_profile():
    return "user profile"
