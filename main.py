import sqlite3
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask('app')
app.secret_key = "secret"
userCart = []
userPrice = []
orderHistory = []
priceHistory = []
## HOME PAGE
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')
## ----------------------------------------------------------------------------------------

## SIGN IN , SIGN UP, LOG OUT FUNCTIONALITY
@app.route('/back', methods=['GET', 'POST'])
def back():
  if request.method == 'POST':
    return render_template('home.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'GET':
     return render_template('sign_in.html')
     
   if request.method == 'POST':
    connection = sqlite3.connect('myDatabase.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    username = request.form["username"]
    password = request.form["password"]
    print(username)
    print(password)
    cursor.execute("SELECT user, password FROM users WHERE user = ? and password = ?", (username, password))
    user = cursor.fetchone()
    connection.commit()
    if user is None:
      return render_template('sign_in.html', message='Invalid username or password')
    session ['user'] = user['user']
    if 'user' in session:
      return render_template ("home.html")
   return redirect('/home')
      

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'GET':
    return render_template('signup.html')
  if request.method == 'POST':
    fname = request.form['fname']
    lname = request.form['lname']
    user = request.form['username']
    password = request.form['password']
    connection = sqlite3.connect('myDatabase.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (fname, lname, user, password, cart) VALUES (?, ?, ?, ?, 0)", (fname, lname, user, password ))
    connection.commit()
    connection.close()
  return render_template('signup.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
     session.pop('user', default=None)
     return render_template ("home.html")
     return redirect('/home')

## ----------------------------------------------------------------------------------------

## CART FUNCTIONALITY
@app.route('/cart', methods=['GET', 'POST'])
def cart():
  
  if request.method == 'GET':
    session['cart'] = userCart
    session['price'] = userPrice
    sum = 0;
    for i in session['price']:
      sum = sum + i
    return render_template('cart.html', cart=session['cart'], price=session['price'], sum=sum)

  return render_template('cart.html', cart=session['cart'], price=session['price'])

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
  if request.method == 'POST':
    connection = sqlite3.connect('myDatabase.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    user = session['user']
    orderHistory = userCart
    priceHistory = userPrice
    print(orderHistory)
    print(priceHistory)
    for item in userCart:
      cursor.execute("SELECT stock FROM products WHERE pname = ?", [item])
      stock = cursor.fetchone()
      if stock['stock'] == 1:
        cursor.execute("UPDATE products SET status = 'OUT' WHERE pname = ?", [item])
    cursor.execute("UPDATE products SET stock = stock - 1 WHERE pname = ?", [item])
    cursor.execute("UPDATE users SET cart = 0 WHERE user = ?", [user])
    connection.commit()
    connection.close()
  return redirect(url_for('cart', orderHistory=userCart, priceHistory=priceHistory))

@app.route('/history', methods=['GET', 'POST'])
def history():
  if request.method == 'GET':
    session['history']= orderHistory
    print(session['history'])
    session['oldPrice'] = priceHistory
    print(session['oldPrice'])
  return render_template('history.html', cart=session['history'], price=session['oldPrice'])



@app.route('/remove', methods=['GET', 'POST'])
def remove():
  if request.method == 'POST':
    user = session['user']
    print(userCart)
    item = request.form['remove']
    for cart in userCart:
      print("cart:", cart)
      if cart == item:
        userCart.remove(item)
    print(userCart)
    print(userPrice)
    connection = sqlite3.connect('myDatabase.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET cart = cart - 1 WHERE user = ?", [user])
    cursor.execute("SELECT price FROM products WHERE pname = ?", [item])
    print("PRICE:", userPrice)
    price = cursor.fetchone()
    minus = price['price']
    userPrice.remove(minus)
    print(userPrice)
    connection.commit()
    connection.close()
  return redirect(url_for('cart'))

@app.route('/reset', methods=['GET', 'POST'])
def rest():
  if request.method == 'POST':
    user = session['user']
    userCart.clear()
    userPrice.clear()
    connection = sqlite3.connect('myDatabase.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET cart = 0 WHERE user = ?", [user])
    connection.commit()
    connection.close()
  return redirect(url_for('cart'))

## ----------------------------------------------------------------------------------------

## SEARCH FUNCTIONALITY
@app.route('/shopping', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    search = request.form['search']
  connection = sqlite3.connect('myDatabase.db')
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT image, pname, price FROM products WHERE pname LIKE ?", ['%'+search+'%'])
  rows = cursor.fetchall()
  connection.commit()
  connection.close()
  return render_template('index.html', rows=rows)

## ----------------------------------------------------------------------------------------

## PRODUCT CATEGORIES
@app.route('/furniture', methods=['GET', 'POST'])
def furniture():
  if request.method == 'GET':
    connection = sqlite3.connect('myDatabase.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT image, pname, price, status FROM products WHERE category = 'Furniture'")
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    return render_template('furniture.html', rows=rows)
  
  if 'cart' not in session:
    session['cart'] = []
  if 'price' not in session:
    session['price'] = []
  
  if request.method == 'POST':
    user = session['user']
    pick = request.form['pick']
    userCart.append(pick)
    connection = sqlite3.connect('myDatabase.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET cart = cart + 1 WHERE user = ?", [user])
    cursor.execute("SELECT price FROM products WHERE pname = ?", [pick])
    price = cursor.fetchone()
    userPrice.append(price['price'])
    cursor.execute("SELECT image, pname, price, status FROM products WHERE category = 'Furniture'")
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
  return render_template('furniture.html', rows=rows)

@app.route('/toys', methods=['GET', 'POST'])
def toys():
  if request.method == 'GET':
    connection = sqlite3.connect('myDatabase.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT image, pname, price, status FROM products WHERE category = 'Toys'")
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    return render_template('toy.html', rows=rows)
  
  if 'cart' not in session:
    session['cart'] = []
  if 'price' not in session:
    session['price'] = []
  
  if request.method == 'POST':
    user = session['user']
    pick = request.form['pick']
    userCart.append(pick)
    connection = sqlite3.connect('myDatabase.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET cart = cart + 1 WHERE user = ?", [user])
    cursor.execute("SELECT price FROM products WHERE pname = ?", [pick])
    price = cursor.fetchone()
    userPrice.append(price['price'])
    cursor.execute("SELECT image, pname, price, status FROM products WHERE category = 'Toys'")
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
  return render_template('toy.html', rows=rows)
  

@app.route('/travel', methods=['GET', 'POST'])
def travel():
  if request.method == 'GET':
    connection = sqlite3.connect('myDatabase.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT image, pname, price, status FROM products WHERE category = 'Travel'")
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    return render_template('travel.html', rows=rows)

  if 'cart' not in session:
    session['cart'] = []
  if 'price' not in session:
    session['price'] = []

  if request.method == 'POST':
    user = session['user']
    pick = request.form['pick']
    userCart.append(pick)
    connection = sqlite3.connect('myDatabase.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET cart = cart + 1 WHERE user = ?", [user])
    cursor.execute("SELECT price FROM products WHERE pname = ?", [pick])
    price = cursor.fetchone()
    userPrice.append(price['price'])
    cursor.execute("SELECT image, pname, price, status FROM products WHERE category = 'Travel'")
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    return render_template('travel.html', rows=rows)
    

@app.route('/food', methods=['GET', 'POST'])
def food():
  if request.method == 'GET':
    connection = sqlite3.connect('myDatabase.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT image, pname, price, status FROM products WHERE category = 'Food Applicances'")
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    return render_template('food.html', rows=rows)

  if 'cart' not in session:
    session['cart'] = []
  if 'price' not in session:
    session['price'] = []

  if request.method == 'POST':
    user = session['user']
    pick = request.form['pick']
    userCart.append(pick)
    connection = sqlite3.connect('myDatabase.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET cart = cart + 1 WHERE user = ?", [user])
    cursor.execute("SELECT price FROM products WHERE pname = ?", [pick])
    price = cursor.fetchone()
    userPrice.append(price['price'])
    cursor.execute("SELECT image, pname, price, status FROM products WHERE category = 'Food Applicances'")
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    return render_template('food.html', rows=rows)
app.run(host='0.0.0.0', port=8080)


    