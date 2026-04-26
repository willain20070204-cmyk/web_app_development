from . import get_db_connection

class Record:
    @staticmethod
    def create(book_id, member_id, borrow_date, due_date):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO records (book_id, member_id, borrow_date, due_date, status) VALUES (?, ?, ?, ?, ?)',
            (book_id, member_id, borrow_date, due_date, 'borrowed')
        )
        conn.commit()
        record_id = cursor.lastrowid
        conn.close()
        return record_id

    @staticmethod
    def get_all():
        conn = get_db_connection()
        # JOIN books 和 members 以取得名稱
        records = conn.execute('''
            SELECT records.*, books.title as book_title, members.name as member_name 
            FROM records
            JOIN books ON records.book_id = books.id
            JOIN members ON records.member_id = members.id
            ORDER BY records.id DESC
        ''').fetchall()
        conn.close()
        return [dict(record) for record in records]

    @staticmethod
    def get_by_id(record_id):
        conn = get_db_connection()
        record = conn.execute('''
            SELECT records.*, books.title as book_title, members.name as member_name 
            FROM records
            JOIN books ON records.book_id = books.id
            JOIN members ON records.member_id = members.id
            WHERE records.id = ?
        ''', (record_id,)).fetchone()
        conn.close()
        return dict(record) if record else None

    @staticmethod
    def mark_as_returned(record_id, return_date):
        conn = get_db_connection()
        conn.execute('''
            UPDATE records 
            SET status = 'returned', return_date = ?
            WHERE id = ?
        ''', (return_date, record_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_popular_books(limit=5):
        """統計各類書籍的出借次數排行榜"""
        conn = get_db_connection()
        books = conn.execute('''
            SELECT books.id, books.title, books.author, COUNT(records.id) as borrow_count
            FROM books
            LEFT JOIN records ON books.id = records.book_id
            GROUP BY books.id
            ORDER BY borrow_count DESC, books.title ASC
            LIMIT ?
        ''', (limit,)).fetchall()
        conn.close()
        return [dict(book) for book in books]
