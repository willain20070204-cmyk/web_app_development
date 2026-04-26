import sqlite3
from . import get_db_connection

class Book:
    @staticmethod
    def create(title, author, isbn=None, category=None, stock=0):
        """新增一筆書籍紀錄"""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO books (title, author, isbn, category, stock) VALUES (?, ?, ?, ?, ?)',
                (title, author, isbn, category, stock)
            )
            conn.commit()
            book_id = cursor.lastrowid
            return book_id
        except sqlite3.Error as e:
            print(f"Database error in Book.create: {e}")
            return None
        finally:
            if 'conn' in locals() and conn:
                conn.close()

    @staticmethod
    def get_all(search_query=None):
        """取得所有書籍，支援模糊搜尋"""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            if search_query:
                query = f"%{search_query}%"
                cursor.execute('''
                    SELECT * FROM books 
                    WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ? OR category LIKE ?
                    ORDER BY id DESC
                ''', (query, query, query, query))
            else:
                cursor.execute('SELECT * FROM books ORDER BY id DESC')
            books = cursor.fetchall()
            return [dict(book) for book in books]
        except sqlite3.Error as e:
            print(f"Database error in Book.get_all: {e}")
            return []
        finally:
            if 'conn' in locals() and conn:
                conn.close()

    @staticmethod
    def get_by_id(book_id):
        """根據 ID 取得單筆書籍"""
        try:
            conn = get_db_connection()
            book = conn.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
            return dict(book) if book else None
        except sqlite3.Error as e:
            print(f"Database error in Book.get_by_id: {e}")
            return None
        finally:
            if 'conn' in locals() and conn:
                conn.close()

    @staticmethod
    def update(book_id, title, author, isbn, category, stock):
        """更新書籍資料"""
        try:
            conn = get_db_connection()
            conn.execute('''
                UPDATE books 
                SET title = ?, author = ?, isbn = ?, category = ?, stock = ?
                WHERE id = ?
            ''', (title, author, isbn, category, stock, book_id))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error in Book.update: {e}")
            return False
        finally:
            if 'conn' in locals() and conn:
                conn.close()

    @staticmethod
    def delete(book_id):
        """刪除指定書籍"""
        try:
            conn = get_db_connection()
            conn.execute('DELETE FROM books WHERE id = ?', (book_id,))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error in Book.delete: {e}")
            return False
        finally:
            if 'conn' in locals() and conn:
                conn.close()

    @staticmethod
    def update_stock(book_id, amount):
        """更新書籍庫存數量 (amount 可正可負)"""
        try:
            conn = get_db_connection()
            conn.execute('UPDATE books SET stock = stock + ? WHERE id = ?', (amount, book_id))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error in Book.update_stock: {e}")
            return False
        finally:
            if 'conn' in locals() and conn:
                conn.close()
