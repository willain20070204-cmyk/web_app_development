# 路由設計文件：圖書館理系統

本文件涵蓋所有 Flask 後端路由配置，包含對應的 HTTP 方法、URL 路徑、模板與處理邏輯。

## 1. 路由總覽表格

### 首頁與儀表板 (dashboard_routes)
| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 儀表板 | GET | `/` | `templates/dashboard/index.html` | 顯示系統統計與熱門出借排行 |

### 書籍管理 (book_routes)
| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 書籍列表 | GET | `/books` | `templates/books/index.html` | 顯示與搜尋書籍 |
| 新增書籍頁 | GET | `/books/add` | `templates/books/add.html` | 顯示新增表單 |
| 建立書籍 | POST | `/books/add` | — | 接收表單存入資料庫，完成重導向 `/books` |
| 編輯書籍頁 | GET | `/books/<int:id>/edit` | `templates/books/edit.html` | 顯示編輯表單 |
| 更新書籍 | POST | `/books/<int:id>/edit` | — | 更新資料，完成重導向 `/books` |

### 會員管理 (member_routes)
| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 會員列表 | GET | `/members` | `templates/members/index.html` | 顯示所有會員 |
| 新增會員頁 | GET | `/members/add` | `templates/members/add.html` | 顯示新增表單 |
| 建立會員 | POST | `/members/add` | — | 接收表單存入資料庫，完成重導向 `/members` |
| 編輯會員頁 | GET | `/members/<int:id>/edit` | `templates/members/edit.html` | 顯示編輯表單 |
| 更新會員 | POST | `/members/<int:id>/edit` | — | 更新資料，完成重導向 `/members` |

### 借閱記錄 (record_routes)
| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 借閱列表 | GET | `/records` | `templates/records/index.html` | 顯示所有借閱紀錄 |
| 借出頁面 | GET | `/records/add` | `templates/records/add.html` | 顯示借出表單 (選擇書籍與會員) |
| 建立借出 | POST | `/records/add` | — | 建立紀錄並扣減庫存，重導向 `/records` |
| 歸還書籍 | POST | `/records/<int:id>/return` | — | 標記歸還並增加庫存，重導向 `/records` |

## 2. 每個路由詳細說明

### 2.1 儀表板
- **GET /**
  - 處理邏輯：呼叫 `Record.get_popular_books()` 取得排行，計算書籍、會員與借出總數。
  - 輸出：渲染 `dashboard/index.html`。

### 2.2 書籍管理
- **GET /books**
  - 輸入：Query 參數 `search` (可選)。
  - 處理邏輯：呼叫 `Book.get_all(search)`。
  - 輸出：渲染 `books/index.html`。
- **POST /books/add**
  - 輸入：Form 參數 `title`, `author`, `isbn`, `category`, `stock`。
  - 處理邏輯：呼叫 `Book.create(...)`。
  - 輸出：重導向 `/books`。

### 2.3 會員管理
- **GET /members**
  - 處理邏輯：呼叫 `Member.get_all()`。
  - 輸出：渲染 `members/index.html`。
- **POST /members/add**
  - 輸入：Form 參數 `name`, `email`, `phone`, `join_date`。
  - 處理邏輯：呼叫 `Member.create(...)`。
  - 輸出：重導向 `/members`。

### 2.4 借閱管理
- **GET /records/add**
  - 處理邏輯：呼叫 `Book.get_all()` 與 `Member.get_all()`，將可選清單傳入模板。
  - 輸出：渲染 `records/add.html`。
- **POST /records/add**
  - 輸入：Form 參數 `book_id`, `member_id`, `borrow_date`, `due_date`。
  - 處理邏輯：
    1. 驗證庫存 > 0
    2. 呼叫 `Record.create(...)`
    3. 呼叫 `Book.update_stock(book_id, -1)`
  - 輸出：重導向 `/records`。
- **POST /records/<id>/return**
  - 輸入：URL 參數 `id`。
  - 處理邏輯：
    1. 取得借閱紀錄以獲得 `book_id`
    2. 呼叫 `Record.mark_as_returned(...)`
    3. 呼叫 `Book.update_stock(book_id, 1)`
  - 輸出：重導向 `/records`。

## 3. Jinja2 模板清單

所有模板皆繼承 `base.html`：
- `templates/base.html`
- `templates/dashboard/index.html`
- `templates/books/index.html`
- `templates/books/add.html`
- `templates/books/edit.html`
- `templates/members/index.html`
- `templates/members/add.html`
- `templates/members/edit.html`
- `templates/records/index.html`
- `templates/records/add.html`
