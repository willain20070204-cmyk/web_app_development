from . import get_db_connection

class Book:
    @staticmethod
    def create(title, author, isbn=None, category=None, stock=0):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO books (title, author, isbn, category, stock) VALUES (?, ?, ?, ?, ?)',
            (title, author, isbn, category, stock)
        )
        conn.commit()
        book_id = cursor.lastrowid
        conn.close()
        return book_id

    @staticmethod
    def get_all(search_query=None):
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
        conn.close()
        return [dict(book) for book in books]

    @staticmethod
    def get_by_id(book_id):
        conn = get_db_connection()
        book = conn.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
        conn.close()
        return dict(book) if book else None

    @staticmethod
    def update(book_id, title, author, isbn, category, stock):
        conn = get_db_connection()
        conn.execute('''
            UPDATE books 
            SET title = ?, author = ?, isbn = ?, category = ?, stock = ?
            WHERE id = ?
        ''', (title, author, isbn, category, stock, book_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(book_id):
        conn = get_db_connection()
        conn.execute('DELETE FROM books WHERE id = ?', (book_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def update_stock(book_id, amount):
        """amount 可為正或負"""
        conn = get_db_connection()
        conn.execute('UPDATE books SET stock = stock + ? WHERE id = ?', (amount, book_id))
        conn.commit()
        conn.close()
