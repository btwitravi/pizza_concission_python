# pizza_concession_python 🍕 
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
# Objective 

A simple Python-based console project that simulates a pizza ordering system.  
Users can view the menu, select items case-insensitively, add them to a cart, and get the final bill.

## Features
- 📋 Display pizza menu with prices
- 🔍 Case-insensitive item selection
- ❌ Handles invalid inputs gracefully
- 🛒 Cart system with multiple items
- 💵 Automatic total bill calculation

- 📂 Project Structure

pizza_concission_python/
│
├── pizza_concession.py   # Main source code
└── README.md             # Project documentation


## How to Run
1. Make sure Python 3 is installed on your system.
2. Clone this repository:
   git clone https://github.com/btwitravi/pizza_concession_python.git
## 📓 Jupyter Notebook
You can also view and run this project in Jupyter Notebook:  
[Pizza Concession.ipynb (2)](Pizza%20Concession.ipynb (2))

## 📌 Sample Output

--------------------------------- Menu -------------------------
Marghretia Pizza                    - Rs.399.00
Cheese & Corn Pizza                 - Rs.499.00
Cheese & Tomato Pizza               - Rs.499.00
Double Cheese & Marghretia Pizza    - Rs.539.00
Fresh Veggies Pizza                 - Rs.539.00
Farmhouse Pizza                     - Rs.599.00
Preppy paneer pizza                 - Rs.599.00
Veggies Paradise Pizza              - Rs.699.00
Cheese Dominator Pizza              - Rs.839.00
Cheese Pizza                        - Rs.839.00
----------------------------------------------------------------

Select an item (q for quit): Burger  
❌ Item Not Available please choose from the menu  

Select an item (q for quit): Cheese Dominator pizza  
✅ Cheese Dominator Pizza is added to cart!  

Select an item (q for quit): Cheese pizza  
✅ Cheese Pizza is added to cart!  

Select an item (q for quit): Fry Rice  
❌ Item Not Available please choose from the menu  

Select an item (q for quit): Cheese & Corn pizza  
✅ Cheese & Corn Pizza is added to cart!  

Select an item (q for quit): q  

------------------------- Your Order ---------------------------
Cheese Dominator Pizza  
Cheese Pizza  
Cheese & Corn Pizza
