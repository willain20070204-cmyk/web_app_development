from flask import Blueprint, render_template
from app.models.record import Record
from app.models.book import Book
from app.models.member import Member

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def index():
    """
    處理儀表板首頁請求。
    呼叫 Record.get_popular_books() 等統計資料，渲染 dashboard/index.html。
    """
    popular_books = Record.get_popular_books(limit=5)
    books_count = len(Book.get_all())
    members_count = len(Member.get_all())
    records = Record.get_all()
    active_records = [r for r in records if r['status'] == 'borrowed']
    
    return render_template('dashboard/index.html', 
                           popular_books=popular_books,
                           books_count=books_count,
                           members_count=members_count,
                           active_borrow_count=len(active_records))
