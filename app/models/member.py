from . import get_db_connection

class Member:
    @staticmethod
    def create(name, email=None, phone=None, join_date=None):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO members (name, email, phone, join_date) VALUES (?, ?, ?, ?)',
            (name, email, phone, join_date)
        )
        conn.commit()
        member_id = cursor.lastrowid
        conn.close()
        return member_id

    @staticmethod
    def get_all():
        conn = get_db_connection()
        members = conn.execute('SELECT * FROM members ORDER BY id DESC').fetchall()
        conn.close()
        return [dict(member) for member in members]

    @staticmethod
    def get_by_id(member_id):
        conn = get_db_connection()
        member = conn.execute('SELECT * FROM members WHERE id = ?', (member_id,)).fetchone()
        conn.close()
        return dict(member) if member else None

    @staticmethod
    def update(member_id, name, email, phone, join_date):
        conn = get_db_connection()
        conn.execute('''
            UPDATE members 
            SET name = ?, email = ?, phone = ?, join_date = ?
            WHERE id = ?
        ''', (name, email, phone, join_date, member_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(member_id):
        conn = get_db_connection()
        conn.execute('DELETE FROM members WHERE id = ?', (member_id,))
        conn.commit()
        conn.close()
