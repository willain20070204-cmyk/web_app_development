from flask import Blueprint, request, render_template, redirect, url_for

member_bp = Blueprint('members', __name__, url_prefix='/members')

@member_bp.route('/')
def index():
    """
    處理會員列表請求。
    呼叫 Member.get_all() 並渲染 members/index.html。
    """
    pass

@member_bp.route('/add', methods=['GET', 'POST'])
def add():
    """
    GET: 渲染 members/add.html 以顯示新增會員表單。
    POST: 接收表單資料，呼叫 Member.create()，重導向至 members.index。
    """
    pass

@member_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    """
    GET: 取得指定 id 會員，渲染 members/edit.html。
    POST: 接收更新資料，呼叫 Member.update()，重導向至 members.index。
    """
    pass
