# Warehouse Management System

A Django-based web application for managing warehouse operations, including products, suppliers, buyers, orders, deliveries, and seasonal inventory.

## Features

- User authentication (login/register)
- Dashboard with overview
- Product management (CRUD)
- Supplier management
- Buyer management
- Order processing
- Delivery tracking
- Season-based categorization
- Responsive UI with static assets

## Tech Stack

- **Backend:** Django 5.0.6, Python 3.x
- **Database:** MySQL (mysqlclient)
- **Frontend:** HTML, CSS, JavaScript, Bootstrap (custom assets)
- **Other:** asgiref, sqlparse, tzdata

## Installation

### Prerequisites
- Python 3.10 or higher
- MySQL server
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/adithyanm274/warehouse.git
   cd warehouse

2. Create a virtual environment

   python -m venv venv
3. source venv/bin/activate   # On Windows: venv\Scripts\activate

4. Install dependencies
   pip install -r requirements.txt

5. Configure MySQL database

   Create a database (e.g., warehouse_db)

   Update project22/settings.py with your database credentials:

python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'warehouse_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

6. Run migrations
   python manage.py makemigrations
   python manage.py migrate

7. Create a superuser (admin)

   python manage.py createsuperuser

8. Collect static files

   python manage.py collectstatic

9. Start the development server

   python manage.py runserver

10. Open your browser at http://127.0.0.1:8000

Project Structure
text
warehouse-main/
├── project22/          # Project settings
├── store/              # Main app for warehouse logic
├── users/              # Custom user authentication
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── manage.py
├── requirements.txt
└── README.md
Usage
Admin panel: /admin (use superuser credentials)

Dashboard: /

Manage products: /products/

Manage suppliers: /suppliers/

Manage buyers: /buyers/

Create orders: /orders/create/

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
MIT

Contact
Project maintainer: adithyanm






   
