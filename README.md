# Purrfect Shop

A full-stack e-commerce web app for cat supplies, built with Python Flask and SQLite.

---

## Overview

Purrfect Shop is a web store where users can browse cat products across multiple categories, search by name, manage a shopping cart, and place orders. It was built to practice full-stack web development with a relational database backend.

## Features

- Browse 20+ products across 4 categories: Furniture, Food Appliances, Toys, and Travel
- Search for products by name
- User registration and login
- Session-based shopping cart — add, remove, or clear items
- Checkout flow that updates inventory in the database
- Order history for logged-in users
- Out-of-stock indicators; prevents buying more than available inventory

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML, CSS (Jinja2 templating)

## Getting Started

### Prerequisites

- Python 3.x
- Flask (`pip install flask`)

### Setup

1. Clone the repo
2. Initialize the database:
   ```bash
   sqlite3 myDatabase.db < store_schema.sql
   ```
3. Run the app:
   ```bash
   python main.py
   ```
4. Visit `http://localhost:8080`

## Project Structure

```
shopping-cart/
├── main.py              # Flask routes and app logic
├── store_schema.sql     # Database schema and seed data
├── myDatabase.db        # SQLite database
├── templates/           # Jinja2 HTML templates
└── static/
    └── assets/          # Product images and stylesheets
```

## What I Want to Fix / Add

### Bugs (yes I know)
- [ ] The cart is a global list right now which means it's technically shared across all users... will fix that
- [ ] There's an indentation bug in checkout so only the last item in the cart actually gets its stock updated
- [ ] Order history disappears on server restart because it's stored in a variable instead of the database
- [ ] Signup just stays on the form after you submit, it doesn't tell you anything went through
- [ ] Search crashes if you try to visit the search page directly without submitting the form

### Security Stuff
- [ ] Passwords are stored as plain text rn — need to hash them with something like `werkzeug.security`
- [ ] `app.secret_key` is literally just `"secret"` — should pull that from an environment variable
- [ ] Cart, checkout, and history pages are accessible even if you're not logged in

### Things I Want to Add
- [ ] Let users pick a quantity when adding to cart instead of always adding 1
- [ ] Actually save order history to the database with a timestamp
- [ ] Let users sort and search through their past orders
- [ ] Add some JS form validation so you can't type in a negative number or something
- [ ] Give each product a description
- [ ] Add a logo / make it look more like a real store

### Cleanup
- [ ] The DB connection code is copy-pasted in like every single route — should make a helper function
- [ ] Add a `.gitignore` (accidentally committed `.DS_Store` files)
- [ ] Add a `requirements.txt`
