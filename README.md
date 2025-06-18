# Bank API (Flask + PostgreSQL)

## 專案簡介
模擬銀行帳戶管理 API，支援帳戶總攬、交易明細、利息自動計算等功能。後端採用 Flask，資料庫為 PostgreSQL，適合部署於 Render。

## 啟動方式
1. 安裝依賴：
   ```
   pip install -r requirements.txt
   ```
2. 設定環境變數（可用 .env 檔）：
   - `DATABASE_URL`：PostgreSQL 連線字串
   - `SECRET_KEY`：Flask 密鑰
3. 初始化資料庫：
   ```
   flask shell
   >>> from app import db, create_app
   >>> app = create_app()
   >>> with app.app_context():
   ...     db.create_all()
   ```
4. 啟動伺服器：
   ```
   python app.py
   ```

## Render 部署注意事項
- 在 Render 上建立 PostgreSQL 資料庫，並將 `DATABASE_URL` 設為環境變數。
- 部署 Web Service 時，啟動指令設為：
  ```
  gunicorn app:create_app()
  ``` 