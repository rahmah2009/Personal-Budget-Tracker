from utils import get_date
def add_transaction(transactions, type):
    # If type is income → ask for source + amount.
    if type == "income":
        category = input("Enter the source of income: ")
        description = input("Enter the expense description: ")
        amount = float(input("Enter the amount: "))
        date = get_date()
        transactions.append({
            "type": "income",
            "source": category,
            "description": description,
            "amount": amount,
            "date": date
            
        })
    # If type is expense → ask for category + description + amount.
    elif type == "expense":
        category = input("Enter the expense category: ")
        description = input("Enter the expense description: ")
        amount = float(input("Enter the amount: "))
        date = get_date()
        transactions.append({
            "type": "expense",
            "category": category,
            "description": description,
            "amount": amount,
            "date": date
        })

    else:
        print("Invalid transaction type. Please enter 'income' or 'expense'.")

