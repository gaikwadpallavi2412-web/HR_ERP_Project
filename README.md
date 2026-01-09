# HR ERP Project (Flask + MySQL)

This is a simple Human Resource ERP web application built using Flask and MySQL. It allows an admin to manage employee records including adding, updating, deleting, and viewing employee details.

## 🔧 Features

- Admin login with session management
- Add new employees
- View all or specific employees
- Update employee details
- Delete employee records
- Search employee by ID

## Demo Documentation

A detailed demo is available here:

📄 [Download Demo Document](Demo.docx)

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Database**: MySQL (via PyMySQL)
- **Frontend**: HTML templates (Jinja2)

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/flask-hr-erp.git
cd flask-hr-erp


### 2. Install dependencies

```bash
pip install -r requirements.txt

### 3. Set up the MySQL database
Create a database named hr_erp_db and a table named employee:
CREATE TABLE employee (
  empid INT PRIMARY KEY,
  full_name VARCHAR(100),
  email VARCHAR(100),
  phone VARCHAR(20),
  department VARCHAR(50),
  joining_date DATE,
  salary FLOAT
);

### 4. Run the application
python main.py
Visit http://127.0.0.1:5000/ in your browser.

Project Structure
flask-hr-erp/
│── main.py
│── templates/
│   ├── index.html
│   ├── about.html
│   ├── admin.html
│   ├── adminhome.html
│   ├── addemp.html
│   ├── showemp.html
│   ├── profile.html
│   ├── searchemp.html
│   ├── adminlogout.html
│── static/ (optional for CSS/JS)
│── requirements.txt
│── README.md



