DROP TABLE IF EXISTS users;
CREATE TABLE users (
  fname        varchar(50) not null,
  lname        varchar(50) not null,
  user        varchar(50) not null PRIMARY KEY,
  password     varchar(50) not null,
  cart         int(3)
  
);
DROP TABLE IF EXISTS products;
CREATE TABLE products (
  id          int(3) not null PRIMARY KEY,
  pname       varchar(50) not null,
  category    varchar(50) not null,
  price       decimal(5,2) not null,
  stock       int(3) not null,
  image       varchar(50) not null,
  status      varchar(50)
  
);


-- users
INSERT INTO users (fname, lname, user, password, cart) VALUES ('John', 'Doe', 'testuser', 'testpass', 0);

-- products, furniture category
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('1', 'Pink Cat Bed', 'Furniture', 30.00, 10, 'pinkcatbed.jpeg', ' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('2', 'Blue Cat Bed', 'Furniture', 30.00, 10, 'bluecatbed.jpeg',' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('3', 'Green Cat Bed', 'Furniture', 30.00, 10, 'greencatbed.jpeg',' ');

INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('4', 'Automatic Litter Box', 'Furniture', 50.00, 2, 'autolitter.jpeg', ' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('5', 'Covered Litter Box', 'Furniture', 35.00, 2, 'coveredlitter.jpeg',' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('6', 'Top-Entry Litter Box', 'Furniture', 50.00, 2, 'toplitter.jpeg',' ');

INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('7', 'Flower Cat Tree', 'Furniture', 100.00, 10, 'flowertower.jpeg', ' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('8', 'Basket Cat Tree', 'Furniture', 120.00, 10, 'baskettower.jpeg', ' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('9', 'Modern Cat Tree', 'Furniture', 130.00, 10, 'moderntower.jpeg', ' ');

-- products, food appliances category

INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('10', 'Stainless Steel Cat Dish', 'Food Applicances', 10.00, 10, 'steeldish.jpeg', ' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('11', 'Non-Skid Ceramic Bowl', 'Food Applicances', 15.00, 10, 'noskidbowl.jpg', ' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('12', 'Elevated Cat Bowl', 'Food Applicances', 20.00, 10, 'elevatedbowl.jpeg', ' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('13', 'Water Fountain', 'Food Applicances', 45.00, 5, 'autowater.jpeg', ' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('14', 'Automatic Feeder', 'Food Applicances', 70.00, 30, 'autofeed.jpeg', ' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('15', 'Silicone Food Mat', 'Food Applicances', 20.00, 10, 'foodmat.jpeg', ' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('16', 'Enrichment Lick Mat', 'Food Applicances', 25.00, 10, 'slowfeedmat.jpeg', ' ');

-- products, toy category

INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('17', 'Wand Toy', 'Toys', 3.00, 40, 'wandtoy.jpeg', ' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('18', 'Catnip Plush', 'Toys', 10.00, 10, 'catniptoy.jpeg', ' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('19', 'Foldable Play Tunnel', 'Toys', 20.00, 10, 'tunnel.jpg', ' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('20', 'Exercise Wheel', 'Toys', 30.00, 5, 'wheel.jpeg', ' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('21', 'Scracth Post', 'Toys', 15.00, 5, 'scratcher.jpeg', ' ');

-- products, travel category

INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('22', 'Hard Carrier', 'Travel', 40.00, 10, 'hcarry.jpeg', ' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('23', 'Soft Carrier', 'Travel', 25.00, 10, 'scarry.jpg', ' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('24', 'Basic Collar', 'Travel', 5.00, 10, 'basic.jpeg', ' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('25', 'Breakaway Collar', 'Travel', 5.00, 10, 'break.jpeg', ' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('26', 'Vest Harness', 'Travel', 10.00, 10, 'vest.jpeg', ' ');
INSERT INTO products (id, pname, category, price, stock, image, status) VALUES ('27', 'Jacket Harness', 'Travel', 10.00, 10, 'harness.jpg', ' ');



