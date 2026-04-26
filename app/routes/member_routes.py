from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.models.member import Member

member_bp = Blueprint('members', __name__, url_prefix='/members')

@member_bp.route('/')
def index():
    members = Member.get_all()
    return render_template('members/index.html', members=members)

@member_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        join_date = request.form.get('join_date')

        if not name:
            flash('會員姓名為必填', 'danger')
            return redirect(url_for('members.add'))

        if Member.create(name, email, phone, join_date):
            flash('成功新增會員', 'success')
            return redirect(url_for('members.index'))
        else:
            flash('新增會員失敗', 'danger')

    return render_template('members/add.html')

@member_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    member = Member.get_by_id(id)
    if not member:
        flash('找不到該會員', 'danger')
        return redirect(url_for('members.index'))

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        join_date = request.form.get('join_date')

        if not name:
            flash('會員姓名為必填', 'danger')
            return redirect(url_for('members.edit', id=id))

        if Member.update(id, name, email, phone, join_date):
            flash('成功更新會員資料', 'success')
            return redirect(url_for('members.index'))
        else:
            flash('更新會員資料失敗', 'danger')

    return render_template('members/edit.html', member=member)
