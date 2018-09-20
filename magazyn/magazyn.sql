DROP TABLE IF EXISTS customers;
CREATE TABLE customers 
(
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    address TEXT NOT NULL
    
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders
(
	order_id INTEGER PRIMARY KEY AUTOINCREMENT,
	customer_id INTEGER,
	subscription_id INTEGER,
	purchase_date DATE,
	FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
	FOREIGN KEY (subscription_id) REFERENCES subscriptions(subscription_id)
);

DROP TABLE IF EXISTS subscriptions;
CREATE TABLE subscriptions
(
	subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
	description TEXT,
	price_per_month INTEGER,
	subscription_length TEXT
);
