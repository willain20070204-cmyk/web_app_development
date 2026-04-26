import sqlite3
from . import get_db_connection

class Record:
    @staticmethod
    def create(book_id, member_id, borrow_date, due_date):
        """新增借閱紀錄"""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO records (book_id, member_id, borrow_date, due_date, status) VALUES (?, ?, ?, ?, ?)',
                (book_id, member_id, borrow_date, due_date, 'borrowed')
            )
            conn.commit()
            record_id = cursor.lastrowid
            return record_id
        except sqlite3.Error as e:
            print(f"Database error in Record.create: {e}")
            return None
        finally:
            if 'conn' in locals() and conn:
                conn.close()

    @staticmethod
    def get_all():
        """取得所有借閱紀錄 (包含關聯的書名與會員名)"""
        try:
            conn = get_db_connection()
            records = conn.execute('''
                SELECT records.*, books.title as book_title, members.name as member_name 
                FROM records
                JOIN books ON records.book_id = books.id
                JOIN members ON records.member_id = members.id
                ORDER BY records.id DESC
            ''').fetchall()
            return [dict(record) for record in records]
        except sqlite3.Error as e:
            print(f"Database error in Record.get_all: {e}")
            return []
        finally:
            if 'conn' in locals() and conn:
                conn.close()

    @staticmethod
    def get_by_id(record_id):
        """根據 ID 取得單一紀錄"""
        try:
            conn = get_db_connection()
            record = conn.execute('''
                SELECT records.*, books.title as book_title, members.name as member_name 
                FROM records
                JOIN books ON records.book_id = books.id
                JOIN members ON records.member_id = members.id
                WHERE records.id = ?
            ''', (record_id,)).fetchone()
            return dict(record) if record else None
        except sqlite3.Error as e:
            print(f"Database error in Record.get_by_id: {e}")
            return None
        finally:
            if 'conn' in locals() and conn:
                conn.close()

    @staticmethod
    def mark_as_returned(record_id, return_date):
        """標記紀錄為已歸還"""
        try:
            conn = get_db_connection()
            conn.execute('''
                UPDATE records 
                SET status = 'returned', return_date = ?
                WHERE id = ?
            ''', (return_date, record_id))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error in Record.mark_as_returned: {e}")
            return False
        finally:
            if 'conn' in locals() and conn:
                conn.close()

    @staticmethod
    def get_popular_books(limit=5):
        """統計各類書籍的出借次數排行榜"""
        try:
            conn = get_db_connection()
            books = conn.execute('''
                SELECT books.id, books.title, books.author, COUNT(records.id) as borrow_count
                FROM books
                LEFT JOIN records ON books.id = records.book_id
                GROUP BY books.id
                ORDER BY borrow_count DESC, books.title ASC
                LIMIT ?
            ''', (limit,)).fetchall()
            return [dict(book) for book in books]
        except sqlite3.Error as e:
            print(f"Database error in Record.get_popular_books: {e}")
            return []
        finally:
            if 'conn' in locals() and conn:
                conn.close()
