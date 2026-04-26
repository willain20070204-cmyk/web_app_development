from flask import Blueprint, request, render_template, redirect, url_for

book_bp = Blueprint('books', __name__, url_prefix='/books')

@book_bp.route('/')
def index():
    """
    處理書籍列表請求。
    可接收 search 參數。呼叫 Book.get_all() 並渲染 books/index.html。
    """
    pass

@book_bp.route('/add', methods=['GET', 'POST'])
def add():
    """
    GET: 渲染 books/add.html 以顯示新增書籍表單。
    POST: 接收表單資料，呼叫 Book.create()，重導向至 books.index。
    """
    pass

@book_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    """
    GET: 取得指定 id 書籍，渲染 books/edit.html。
    POST: 接收更新資料，呼叫 Book.update()，重導向至 books.index。
    """
    pass
