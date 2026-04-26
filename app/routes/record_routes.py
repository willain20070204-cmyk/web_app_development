from flask import Blueprint, request, render_template, redirect, url_for

record_bp = Blueprint('records', __name__, url_prefix='/records')

@record_bp.route('/')
def index():
    """
    處理借閱紀錄列表請求。
    呼叫 Record.get_all() 並渲染 records/index.html。
    """
    pass

@record_bp.route('/add', methods=['GET', 'POST'])
def add():
    """
    GET: 取得會員與書籍清單，渲染 records/add.html。
    POST: 接收表單資料，建立借閱紀錄，扣除書籍庫存，重導向至 records.index。
    """
    pass

@record_bp.route('/<int:id>/return', methods=['POST'])
def return_book(id):
    """
    POST: 標記指定紀錄為已歸還，並加回該書的庫存數量，最後重導向至 records.index。
    """
    pass
