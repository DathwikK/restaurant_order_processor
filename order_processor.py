import json
import sys

def main():
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

    # Create items.json
    items = {}
    for order in orders:
        for item in order["items"]:
            item_name = item["name"].strip()
            price = float(item["price"])

            # Initialize the item entry if not present
            if item_name not in items:
                items[item_name] = {"price": price, "orders": 0}

            # Increment order count
            items[item_name]["orders"] += 1

    with open("items.json", "w") as f:
        json.dump(items, f, indent=4)

    print("customers.json and items.json created successfully!")

if __name__ == "__main__":
    main()