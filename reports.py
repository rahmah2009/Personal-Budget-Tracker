from datetime import datetime

transactions = [
    {
        "type": "expense",
        "category": "Food",
        "amount": 5000
    },
    {
        "type": "expense",
        "category": "Transport",
        "amount": 10000
    },
    {
        "type": "expense",
        "category": "Food",
        "amount": 10000
    },
    {
        "type": "expense",
        "category": "School",
        "amount": 15000
    },
    {
        "type": "expense",
        "category": "Data",
        "amount": 10000
    }
]

def view_by_category():
    categories = {}

    for transaction in transactions:
        if transaction["type"] == "expense":
            category = transaction['category']
            amount = transaction['amount']

            if category not in categories:
             categories[category] = 0

        categories[category] += amount

    print("\n===== SPENDING BY CATEGORY =====")

    if not categories:
        print("No expenses found.")
        return

    for category, total in categories.items():
        print(f"{category}: ₦{total:,.2f}")

view_by_category()