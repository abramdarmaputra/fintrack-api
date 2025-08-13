# FinTrackAPI

## 🌟 Deskripsi Proyek

FinTrackAPI adalah RESTful API sederhana untuk membantu pengguna mencatat pemasukan, pengeluaran, dan memantau saldo bulanan. API ini cocok digunakan sebagai backend aplikasi mobile/web untuk manajemen keuangan pribadi.

---

## 🎯 Tujuan

* Mencatat transaksi pemasukan dan pengeluaran.
* Mengelompokkan transaksi berdasarkan kategori.
* Menyediakan ringkasan laporan bulanan dan pengeluaran per kategori.
* Menyediakan API CRUD untuk User, Kategori, dan Transaksi.

---

## 🛠️ Teknologi yang Digunakan

* **Python** (FastAPI)
* **PostgreSQL** (Database)
* **SQLAlchemy** (ORM)
* **Alembic** (Migrasi Database)
* **Docker** & **docker-compose** (Containerization)
* **Postman** (Pengujian API)
* **GitHub** (Version Control)

---

## 🛠️ Panduan Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/abramdarmaputra/fintrack-api.git
cd fintrack-api
```

### 2. Buat Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Environment

Buat file `.env` berdasarkan `.env.example`:

```env
DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/fintrack_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Setup Database

```bash
alembic revision --autogenerate -m "init"
alembic upgrade head
```

### 6. Jalankan Server

```bash
uvicorn app.main:app --reload
```

---

## 📂 Struktur Folder

```
fintrackapi/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── deps.py
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── category.py
│   │   ├── transaction.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── category.py
│   │   ├── transaction.py
│   ├── utils/
│   |   ├── __init__.py
│   |   ├── calc.py
│   |   ├── security.py
│   |   ├── summary.py
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
├── tests/                 # Unit & integration tests
│   ├── __init__.py
│   ├── test_calc.py
│   ├── test_categories.py
│   └── test_transactions.py
├── alembic.ini
├── .env.example
├── requirements.txt
├── README.md
```

---

## 📊 Endpoint Utama

### **Kategori**

* `GET /kategori/` - List semua kategori
* `POST /kategori/` - Tambah kategori baru
* `PUT /kategori/{id}` - Update kategori
* `DELETE /kategori/{id}` - Hapus kategori

### **Transaksi**

* `GET /transaksi/` - List semua transaksi
* `POST /transaksi/` - Tambah transaksi baru
* `PUT /transaksi/{id}` - Update transaksi
* `DELETE /transaksi/{id}` - Hapus transaksi

---

## 📊 Testing API di Postman

1. Import file koleksi Postman (`FinTrackAPI.postman_collection.json`).
2. Pastikan server berjalan.
3. Uji semua endpoint CRUD.

---

## 📝 Lisensi

```
Proyek ini menggunakan lisensi MIT.
```
