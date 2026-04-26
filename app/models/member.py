import sqlite3
from . import get_db_connection

class Member:
    @staticmethod
    def create(name, email=None, phone=None, join_date=None):
        """建立新會員"""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO members (name, email, phone, join_date) VALUES (?, ?, ?, ?)',
                (name, email, phone, join_date)
            )
            conn.commit()
            member_id = cursor.lastrowid
            return member_id
        except sqlite3.Error as e:
            print(f"Database error in Member.create: {e}")
            return None
        finally:
            if 'conn' in locals() and conn:
                conn.close()

    @staticmethod
    def get_all():
        """取得所有會員列表"""
        try:
            conn = get_db_connection()
            members = conn.execute('SELECT * FROM members ORDER BY id DESC').fetchall()
            return [dict(member) for member in members]
        except sqlite3.Error as e:
            print(f"Database error in Member.get_all: {e}")
            return []
        finally:
            if 'conn' in locals() and conn:
                conn.close()

    @staticmethod
    def get_by_id(member_id):
        """根據 ID 取得會員資料"""
        try:
            conn = get_db_connection()
            member = conn.execute('SELECT * FROM members WHERE id = ?', (member_id,)).fetchone()
            return dict(member) if member else None
        except sqlite3.Error as e:
            print(f"Database error in Member.get_by_id: {e}")
            return None
        finally:
            if 'conn' in locals() and conn:
                conn.close()

    @staticmethod
    def update(member_id, name, email, phone, join_date):
        """更新會員資料"""
        try:
            conn = get_db_connection()
            conn.execute('''
                UPDATE members 
                SET name = ?, email = ?, phone = ?, join_date = ?
                WHERE id = ?
            ''', (name, email, phone, join_date, member_id))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error in Member.update: {e}")
            return False
        finally:
            if 'conn' in locals() and conn:
                conn.close()

    @staticmethod
    def delete(member_id):
        """刪除指定會員"""
        try:
            conn = get_db_connection()
            conn.execute('DELETE FROM members WHERE id = ?', (member_id,))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error in Member.delete: {e}")
            return False
        finally:
            if 'conn' in locals() and conn:
                conn.close()
