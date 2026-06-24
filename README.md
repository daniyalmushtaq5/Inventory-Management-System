# Inventory Management System

## Overview

Inventory Management System is a full-stack web application designed to help businesses efficiently manage products, inventory records, and customer orders.

The system provides a simple and intuitive interface for managing product catalogs, tracking inventory items, creating customer orders, and maintaining unit-of-measure (UOM) information through a centralized dashboard.

Built with Flask, PostgreSQL, JavaScript, and Bootstrap, the application demonstrates the implementation of a complete CRUD-based inventory management solution.

---

## Features

### Product Management

* Add new products.
* View all available products.
* Delete products from inventory.
* Store product pricing information.
* Associate products with units of measurement.

### Order Management

* Create customer orders.
* Add multiple products to a single order.
* Calculate order totals automatically.
* Store complete order history.
* View previously created orders.

### Unit of Measurement (UOM) Management

Supports inventory units such as:

* Kilograms (Kg)
* Grams (g)
* Liters (L)
* Pieces (pcs)

Additional units can be added through the database.

### Dashboard Interface

* Product Management Page
* Order Management Page
* Interactive forms
* Dynamic table views
* Responsive design

---

## Technology Stack

### Backend

* Python
* Flask
* PostgreSQL
* Psycopg2

### Frontend

* HTML5
* CSS3
* JavaScript
* jQuery
* Bootstrap

### Database

* PostgreSQL

---

## System Architecture

```text
Frontend (HTML/CSS/JS)
           │
           ▼
      Flask API
           │
           ▼
     PostgreSQL
           │
           ▼
 Products | Orders | UOM
```

---

## Project Structure

```text
Inventory-Management-System/
│
├── backend/
│   ├── server.py
│   ├── sql_connection.py
│   ├── products_dao.py
│   ├── orders_dao.py
│   └── uom_dao.py
│
├── ui/
│   ├── index.html
│   ├── manage-product.html
│   ├── order.html
│   │
│   ├── css/
│   └── js/
│
├── homepage.JPG
└── README.md
```

---

## Database Schema

The application uses the following core tables:

### Products

| Column         | Description         |
| -------------- | ------------------- |
| product_id     | Product identifier  |
| name           | Product name        |
| uom_id         | Unit of measurement |
| price_per_unit | Product price       |

### UOM (Unit of Measurement)

| Column   | Description    |
| -------- | -------------- |
| uom_id   | UOM identifier |
| uom_name | Unit name      |

### Orders

| Column        | Description      |
| ------------- | ---------------- |
| order_id      | Order identifier |
| customer_name | Customer name    |
| total         | Order total      |
| date_time     | Order timestamp  |

### Order Details

| Column      | Description       |
| ----------- | ----------------- |
| order_id    | Related order     |
| product_id  | Product reference |
| quantity    | Ordered quantity  |
| total_price | Total line amount |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Inventory-Management-System.git
cd Inventory-Management-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install flask psycopg2
```

---

## PostgreSQL Configuration

Update database settings in:

```python
backend/sql_connection.py
```

Example:

```python
host = "127.0.0.1"
port = "5432"
dbname = "Inventory_system"
user = "postgres"
password = "your_password"
```

Create the PostgreSQL database:

```sql
CREATE DATABASE Inventory_system;
```

Then create the required tables:

* products
* uom
* orders
* order_details

---

## Running the Application

### Start Backend Server

Navigate to the backend directory:

```bash
cd backend
```

Run the Flask application:

```bash
python server.py
```

Server will start on:

```text
http://localhost:5000
```

---

## API Endpoints

### Get Units of Measurement

```http
GET /getUOM
```

Returns all available units of measurement.

---

### Get Products

```http
GET /getProducts
```

Returns all products stored in inventory.

---

### Add Product

```http
POST /insertProduct
```

Request Example:

```json
{
  "product_name": "Rice",
  "uom_id": 1,
  "price_per_unit": 120
}
```

---

### Delete Product

```http
POST /deleteProduct
```

Request Example:

```json
{
  "product_id": 1
}
```

---

### Create Order

```http
POST /insertOrder
```

Request Example:

```json
{
  "customer_name": "John Doe",
  "grand_total": 500,
  "order_details": [
    {
      "product_id": 1,
      "quantity": 2,
      "total_price": 240
    }
  ]
}
```

---

### Get All Orders

```http
GET /getAllOrders
```

Returns all customer orders.

---

## User Interface

### Dashboard

Provides quick navigation between:

* Product Management
* Order Management

### Product Management

Features:

* Add products
* View products
* Delete products

### Order Management

Features:

* Create customer orders
* Select multiple products
* Calculate totals automatically
* Store order information

---

## Learning Objectives

This project demonstrates:

* Full-Stack Web Development
* REST API Development with Flask
* PostgreSQL Database Integration
* CRUD Operations
* Data Access Layer (DAO Pattern)
* Frontend-Backend Communication
* Inventory Management Concepts

---

## Future Enhancements

Potential improvements include:

* User Authentication
* Role-Based Access Control
* Inventory Stock Tracking
* Product Categories
* Supplier Management
* Purchase Orders
* Sales Reports
* Dashboard Analytics
* Docker Deployment
* Cloud Hosting Support

---

## Screenshot

### Home Page

Add the following screenshot to showcase the application:

```text
homepage.JPG
```

---

## Author

**Daniyal Mushtaq**

Computer Science Graduate | Python Developer | Automation Engineer

GitHub: https://github.com/daniyalmushtaq5

---

## License

MIT License

Feel free to use, modify, and distribute this project under the terms of the MIT License.

