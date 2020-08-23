# -*- coding:utf-8 -*-

# @Time     : 2020/8/23 19:59
# @Verson   :
# @Author   : jun
# @Site     : 
# @File     : passport.py
# @Software : PyCharm

from flask import Blueprint, current_app

bp = Blueprint('passport', __name__)


@bp.route('/bp')
def viewfunc():
    print('bp的', current_app.redis_cli)
    return 'ok'
