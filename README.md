# Flask Market

Flask Market is a full-featured e-commerce web application built with Python and the Flask framework. It provides a platform for users to register, log in, buy items, and sell them back to the market. The application also includes an admin panel for managing the products available for sale.

This project is based on the popular "Flask Market" tutorial series and demonstrates key concepts of web development with Flask, including database management, user authentication, and web forms.

## Features

* **User Authentication:** Secure user registration and login functionality.
* **Password Hashing:** Passwords are securely hashed using Bcrypt before being stored in the database.
* **Product Marketplace:** Users can view a list of available items for purchase.
* **Buy and Sell:** Authenticated users can purchase items, which are then added to their owned items list. They can also sell their owned items back to the market.
* **User Budget Management:** Each user has a budget that is updated when they buy or sell items.
* **Admin Panel:** A dedicated page for administrators to add new items to the market.
* **Flash Messages:** Provides feedback to users for actions like successful login, purchases, or errors.

## Technologies Used

* **Backend:** Python, Flask
* **Database:** SQLAlchemy (with SQLite)
* **Forms:** Flask-WTF, WTForms
* **Authentication:** Flask-Login
* **Password Hashing:** Flask-Bcrypt
* **Frontend:** HTML, Bootstrap

## Project Structure

```
├── instance/
│   └── market.db       # Database file
├── market/
│   ├── __init__.py     # Initializes the Flask app and extensions
│   ├── forms.py        # Defines web forms (Register, Login, etc.)
│   ├── models.py       # Defines database models (User, Item)
│   ├── routes.py       # Defines application routes and view logic
│   └── templates/      # Contains all HTML templates
│       ├── base.html
│       ├── home.html
│       ├── market.html
│       └── ...
├── run.py              # Main entry point to run the application
├── database.py         # Script to create and populate the database
└── requirements.txt    # Lists all project dependencies
```

## Setup and Installation

Follow these steps to get the project up and running on your local machine.

### 1. Prerequisites

* Python 3.x

### 2. Clone the Repository

If you have git installed, you can clone the repository. Otherwise, you can download the project files as a ZIP archive.

```bash
git clone <repository-url>
cd <project-directory>
```

### 3. Create a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

Install all the required packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 5. Create the Database

Before running the application for the first time, you need to create the database and populate it with initial data.

First, create a folder named `instance` in the root directory of the project if it doesn't already exist.

Then, run the `database.py` script:

```bash
python database.py
```

You should see a message: `Database created and populated successfully!`

### 6. Run the Application

Now you can start the Flask development server.

```bash
python run.py
```

The application will be available at `http://127.0.0.1:5000` in your web browser.

## How to Use the Application

1.  **Register:** Navigate to the "Register" page and create a new user account.
2.  **Login:** Use your credentials to log in.
3.  **Market Page:** Go to the "Market" page to see the items available for purchase.
4.  **Buy an Item:** Click the "Purchase this Item" button to buy an item. The item will be added to your "Owned Items" list.
5.  **Sell an Item:** In the "Owned Items" section, you can sell items back to the market.
6.  **Admin Panel:** If you are logged in as the admin user (username: "Shaik"), you will see an "Add Products" link in the navigation bar, which takes you to the admin panel where you can add new items.

---

*This README was generated with assistance from an AI model.*
