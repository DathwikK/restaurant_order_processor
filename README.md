# Dosa Order Processor 

This project processes a year's worth of Dosa restaurant orders to generate two summary reports: one for customers and another for menu items. It is designed to help the restaurant organize its customer and item data more efficiently.

---

##  Overview
The script reads a JSON file of restaurant orders and creates:
- **`customers.json`** — Maps each customer's phone number to their name.
- **`items.json`** — Summarizes each menu item's price and total number of times ordered.

Both outputs are stored as JSON files in the project directory.

---

##  Input Format
The input JSON file should contain an array of orders, where each order looks like this:

```json
{
    "timestamp": 1702219784,
    "name": "Damodhar",
    "phone": "732-555-5509",
    "items": [
        {"name": "Cheese Madurai Masala Dosa", "price": 13.95},
        {"name": "Onion Chilli Masala Dosa", "price": 11.95}
    ],
    "notes": "extra spicy"
}
