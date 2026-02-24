# Wood-Board-Inventory-System

## 📌 Overview

This project is a **console-based inventory and customer management system** for managing wood boards in a warehouse or furniture production environment.

The system allows you to:

* Manage wood boards (add, delete, rename, update stock)
* Manage customers
* Sell boards to customers
* Track how many boards customers buy
* Automatically apply customer discounts based on purchase volume

This project is written in **Python** and focuses on practicing:

* Object-Oriented Programming (OOP)
* Data structures
* Business logic design
* Inventory management concepts

---

## ⚙️ Features

### 🪵 Board Management

* Add new board
* Rename board
* Rename factory
* View board info
* Increase stock
* Delete board

### 👤 Customer Management

* Add customer
* View customer info
* Delete customer
* Automatic discount calculation based on purchases

### 💰 Sales System

* Sell boards to customers
* Reduce board stock
* Increase customer purchase count
* Prepare discount updates

---

## 🧠 Business Rules

### Discount Logic

| Boards Bought | Discount |
| ------------- | -------- |
| < 10          | 5%       |
| 10–49         | 15%      |
| 50–99         | 25%      |
| 100+          | 50%      |

---

## 🏗️ Architecture

### Data Storage

The system currently stores data **in memory** using lists:

* `BOARDS_LIST`
* `CUSTOMERS_LIST`

Future improvement: persistence with JSON.

---

### Core Concepts Practiced

* Searching objects by ID
* Separation of concerns
* Reusable helper functions (`find_board`, `find_customer`)
* Safe transaction logic
* Clean conditional flow
* Inventory transaction modeling

---

## 🚀 Future Improvements

Planned upgrades:

* JSON persistence (save/load data)
* Automatic discount recalculation after sale
* Menu-based CLI interface
* Sales history logging
* Staff management
* Price system + revenue tracking
* Edge banding inventory
* Data validation and error handling
* Multi-file project architecture
* GUI version

---

## 🎯 Purpose

This project is designed as a **learning project** to strengthen understanding of:

* OOP design
* Inventory systems
* Business logic modeling
* Clean Python structure

---

## 👤 Author

Built as a learning and practice project.
