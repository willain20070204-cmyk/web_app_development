from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.models.book import Book

book_bp = Blueprint('books', __name__, url_prefix='/books')

@book_bp.route('/')
def index():
    search = request.args.get('search', '')
    books = Book.get_all(search) if search else Book.get_all()
    return render_template('books/index.html', books=books, search=search)

@book_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        isbn = request.form.get('isbn')
        category = request.form.get('category')
        stock = request.form.get('stock', type=int)

        if not title or not author or stock is None:
            flash('書名、作者與庫存數量為必填', 'danger')
            return redirect(url_for('books.add'))

        if Book.create(title, author, isbn, category, stock):
            flash('成功新增書籍', 'success')
            return redirect(url_for('books.index'))
        else:
            flash('新增書籍失敗', 'danger')

    return render_template('books/add.html')

@book_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    book = Book.get_by_id(id)
    if not book:
        flash('找不到該書籍', 'danger')
        return redirect(url_for('books.index'))

    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        isbn = request.form.get('isbn')
        category = request.form.get('category')
        stock = request.form.get('stock', type=int)

        if not title or not author or stock is None:
            flash('書名、作者與庫存數量為必填', 'danger')
            return redirect(url_for('books.edit', id=id))

        if Book.update(id, title, author, isbn, category, stock):
            flash('成功更新書籍', 'success')
            return redirect(url_for('books.index'))
        else:
            flash('更新書籍失敗', 'danger')

    return render_template('books/edit.html', book=book)
