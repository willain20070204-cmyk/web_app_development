import os
import sqlite3
from flask import Flask

# 引入註冊函式
from app.routes import register_blueprints

def create_app():
    app = Flask(__name__)
    
    # 載入環境變數設定
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    
    # 設定資料庫與 instance 目錄路徑
    os.makedirs(app.instance_path, exist_ok=True)
    app.config['DATABASE'] = os.path.join(app.instance_path, 'database.db')

    # 註冊所有的 Blueprint
    register_blueprints(app)

    return app

def init_db():
    """初始化資料庫表結構"""
    app = create_app()
    with app.app_context():
        db_path = app.config['DATABASE']
        schema_path = os.path.join(os.path.dirname(__file__), 'database', 'schema.sql')
        
        conn = sqlite3.connect(db_path)
        with open(schema_path, 'r', encoding='utf-8') as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()
        print(f"Initialized the database at {db_path}")

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
