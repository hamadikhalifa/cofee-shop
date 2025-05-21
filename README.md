# ☕ Coffee Shop Domain Modeling Project

## 📚 Overview

-this Python project simulates a simple coffee shop system using object-oriented programming (OOP) principles. It models the relationships between customers, coffees, and orders to mimic how real-world coffee purchases work.

-this is a Code Challenge project that demonstrates understanding of,
 OOP Concepts: Classes, Objects, Relationships
 Encapsulation and data validation
Class and instance methods
Simple CLI-based testing (`debug.py`)

---

## 📦 Classes & Responsibilities

### ✅ `Customer`
* represents a coffee shop customer
* keeps track of customer name
* can retrieve all their orders
* can retrieve all coffee types they've ordered
* can count how many times they've ordered a particular coffee

### ✅ `Coffee`
* represents a type of coffee
* stores the name of the coffee
* tracks all orders associated with this coffee
* returns customers who ordered it
* calculates average price paid for this coffee
* identifies the customer who spent the most on it

### ✅ `Order`
* represents an order made by a customer
* stores customer, coffee, and price (with validation)
* can be marked as purchased
* supports deleting an order
* can search/filter orders by coffee or customer

---

## 🧪 Features

* add and manage Customers, Coffees, and Orders
* validate price ranges (3.0 to 11.0)
* view all orders for a customer or coffee
* search for orders by customer or coffee
* mark orders as purchased
* delete orders
* calculate total and average spent
* manual testing using `debug.py`

---

## 🗂️ Project Structure

coffee-shop/
│
├── customer.py   # Defines Customer class
├── coffee.py     # Defines Coffee class
├── order.py      # Defines Order class
├── debug.py      # Script to manually test the program




    ## Author

    GitHub: @hamadikhalifa