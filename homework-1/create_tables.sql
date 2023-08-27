-- SQL-команды для создания таблиц
CREATE TABLE customers_data
(
	customer_id varchar(7) PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(100)
);

CREATE TABLE employee_data
(
	employee_id int PRIMARY KEY,
	fisrt_name varchar(100),
	last_name varchar(100),
	title varchar(200),
	birth_date date,
	notes varchar(200)
);

CREATE TABLE orders_data
(
	order_id int PRIMARY KEY,
	customer_id varchar(5) REFERENCES customers_data(customer_id),
	employee_id int REFERENCES employee_data(employee_id),
	order_date date,
	ship_city varchar(100)
);