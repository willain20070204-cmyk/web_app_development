from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.models.record import Record
from app.models.book import Book
from app.models.member import Member
from datetime import datetime

record_bp = Blueprint('records', __name__, url_prefix='/records')

@record_bp.route('/')
def index():
    records = Record.get_all()
    return render_template('records/index.html', records=records)

@record_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book_id = request.form.get('book_id', type=int)
        member_id = request.form.get('member_id', type=int)
        borrow_date = request.form.get('borrow_date')
        due_date = request.form.get('due_date')

        if not book_id or not member_id or not borrow_date or not due_date:
            flash('所有欄位皆為必填', 'danger')
            return redirect(url_for('records.add'))

        book = Book.get_by_id(book_id)
        if not book or book['stock'] <= 0:
            flash('書籍不存在或庫存不足', 'danger')
            return redirect(url_for('records.add'))

        if Record.create(book_id, member_id, borrow_date, due_date):
            Book.update_stock(book_id, -1)
            flash('成功登記借出', 'success')
            return redirect(url_for('records.index'))
        else:
            flash('登記借出失敗', 'danger')

    books = [b for b in Book.get_all() if b['stock'] > 0]
    members = Member.get_all()
    return render_template('records/add.html', books=books, members=members)

@record_bp.route('/<int:id>/return', methods=['POST'])
def return_book(id):
    record = Record.get_by_id(id)
    if not record or record['status'] == 'returned':
        flash('無效的操作', 'danger')
        return redirect(url_for('records.index'))
    
    return_date = datetime.now().strftime('%Y-%m-%d')
    if Record.mark_as_returned(id, return_date):
        Book.update_stock(record['book_id'], 1)
        flash('成功登記歸還', 'success')
    else:
        flash('歸還登記失敗', 'danger')
        
    return redirect(url_for('records.index'))
