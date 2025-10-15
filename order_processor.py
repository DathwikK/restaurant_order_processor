import json
import sys

if len(sys.argv) < 2:
    print("Usage: python order_processor.py <orders_file.json>")
    sys.exit(1)

input_file = sys.argv[1]

# Load orders data
with open(input_file, "r") as f:
    orders = json.load(f)

# Create customers.json
customers = {}
for order in orders:
    phone = order["phone"]
    name = order["name"].strip()
    customers[phone] = name

with open("customers.json", "w") as f:
    json.dump(customers, f, indent=4)