# -*- coding:utf-8 -*-

# @Time     : 2020/8/20 23:15
# @Verson   :
# @Author   : jun
# @Site     : 
# @File     : __init__.py.py
# @Software : PyCharm

from flask import Blueprint

goods_bp = Blueprint('goods', __name__)
from . import views