# Journal App — Backend

Flask REST API and MySQL database for the Journal App.

## Features
- GET, POST, DELETE endpoints for journal entries
- MySQL database for persistent storage
- CORS enabled for frontend connection
- Environment variables for secure credentials

## Tech Used
- Python
- Flask
- MySQL
- flask-cors
- flask-mysqldb
- python-dotenv

## Setup

### 1. Clone the repository
git clone https://github.com/yourusername/journal-backend.git
cd journal-backend

### 2. Install dependencies
pip install -r requirements.txt

### 3. Set up the database
mysql -u root -p < database.sql

### 4. Create .env file
Create a .env file with:
MYSQL_PASSWORD=your_mysql_password

### 5. Run the server
python app.py

Server runs on http://127.0.0.1:5000

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /entries | Get all journal entries |
| POST | /entries | Add new entry |
| DELETE | /entries/<id> | Delete an entry |

