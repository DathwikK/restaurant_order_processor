# Order Processor

This script processes an orders JSON file and generates two output files: `customers.json` and `items.json`.

## Usage

python order_processor.py <orders_file.json>

Example: python order_processor.py orders.json

## Input Format

The input file should be a JSON array of orders.  
Each order must have:
- `name`: customer name  
- `phone`: customer phone number  
- `items`: list of ordered items with `name` and `price`

Example:
[
{
"name": "Alice Johnson",
"phone": "+1234567890",
"items": [
{"name": "Coffee", "price": "3.50"},
{"name": "Bagel", "price": "2.00"}
]
}
]

## Output Files

### customers.json
Contains a mapping of phone numbers to customer names.

{
"+1234567890": "Alice Johnson"
}

### items.json
Contains each item’s price and the number of orders it appears in.

{
"Coffee": {"price": 3.5, "orders": 1},
"Bagel": {"price": 2.0, "orders": 1}
}

## Requirements

- Python 3
- Uses built-in `json` and `sys` modules
