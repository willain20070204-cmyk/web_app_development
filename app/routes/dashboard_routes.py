from flask import Blueprint, render_template

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def index():
    """
    處理儀表板首頁請求。
    呼叫 Record.get_popular_books() 等統計資料，渲染 dashboard/index.html。
    """
    pass
