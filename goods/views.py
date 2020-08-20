# -*- coding:utf-8 -*-

# @Time     : 2020/8/20 23:16
# @Verson   :
# @Author   : jun
# @Site     : 
# @File     : views.py
# @Software : PyCharm

from . import goods_bp


@goods_bp.route('/goods')
def get_goods():
    return 'get goods'
