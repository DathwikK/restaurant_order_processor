# Restaurant Order Processor

## Overview
The **Restaurant Order Processor** is a simple Python script that reads a JSON file containing customer orders and produces two summary files:
- `customers.json` — a list of customers mapped by phone number  
- `items.json` — a summary of each item’s price and how many times it was ordered

This project is designed to make it easier to analyze basic order data for small businesses or internal reporting.

## Design
The script follows a straightforward design:
1. **Input Handling** — Takes an input JSON file from the command line.
2. **Data Loading** — Reads and parses order data using Python’s built-in `json` module.
3. **Customer Extraction** — Creates a unique list of customers based on their phone numbers.
4. **Item Summary** — Counts item occurrences and stores their latest recorded price.
5. **Output Files** — Writes results to `customers.json` and `items.json` for further reference.

The program uses only standard Python libraries (`json` and `sys`), making it lightweight and portable.

## Usage
To run the script, use the command:
python order_processor.py <orders_file.json>

Example:
python order_processor.py orders.json

After running, two new files will be created in the current directory:
- `customers.json`
- `items.json`

In order to view the contents of these files use these commands:
cat customers.json
cat items.json

## Input Format
The input JSON file should contain an array of orders.  
Each order must include the customer’s name, phone number, and a list of items.

Example `example_orders.json`:
[
    {
        "timestamp": 1702219784,
        "name": "Damodhar",
        "phone": "732-555-5509",
        "items": [
            {
                "name": "Cheese Madurai Masala Dosa",
                "price": 13.95
            },
            {
                "name": "Onion Chilli Masala Dosa",
                "price": 11.95
            }
        ],
        "notes": "extra spicy"
    },
    {
        "timestamp": 1684443264,
        "name": "Tom",
        "phone": "609-555-2301",
        "items": [
            {
                "name": "Cheese & Onion Chilli Masala Dosa",
                "price": 12.95
            },
            {
                "name": "Onion Rava Mysore Masala Dosa",
                "price": 14.95
            }
        ],
        "notes": ""
    }
]

## Output Files

### customers.json
Contains phone numbers mapped to customer names:
{
    "732-555-5509": "Damodhar",
    "609-555-2301": "Tom",
    "609-555-5508": "Kunal",
    "609-555-0326": "Bhargavi",
    "732-555-1919": "Shanmukhi",
    "732-555-4109": "Matt"
}

### items.json
Contains item names, their price, and the number of times each was ordered:
{
    "Cheese Madurai Masala Dosa": {
        "price": 13.95,
        "orders": 1232
    },
    "Onion Chilli Masala Dosa": {
        "price": 11.95,
        "orders": 1234
    },
    "Cheese & Onion Chilli Masala Dosa": {
        "price": 12.95,
        "orders": 1200
    }
}

## Requirements
- Python 3.7 or higher
- No external dependencies
