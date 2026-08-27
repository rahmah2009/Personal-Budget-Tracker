# Personal Budget Tracker (CLI)

1. Introduction

The Personal Budget Tracker is a simple command-line application built with Python. It allows users to record their income and expenses and see how their money is being spent.

The project stores transactions in memory using a list of dictionaries.

2. Objectives

The application can:

- Add income and expenses.
- View all transactions.
- Calculate total income and expenses.
- Calculate the net balance.
- Show spending by category.
- Automatically record the transaction date.

3. Data Structure

A list called "transactions" is used to store the records.

Each transaction is stored as a dictionary containing details such as the type, amount, date, and either the income source or expense category and description.

4. Main Features

Add Income

The user enters the income source and amount, which are then added to the transaction list.

Add Expense

The user enters the category, description, and amount of the expense.

View Transactions

All recorded transactions are displayed in a simple formatted table.

View Summary

The program calculates:

- Total Income
- Total Expenses
- Net Balance

The net balance is calculated using:

"Net Balance = Total Income - Total Expenses"

Spending by Category

The program groups expenses such as Food, Transport, and School and calculates the total spent in each category.

Date Recording

The "datetime" module automatically adds the current date to each transaction.

5. Functions Used

The main functions are:

- "add_transaction()" — adds a new transaction.
- "view_all()" — displays transactions.
- "get_summary()" — calculates the financial summary.
- "view_by_category()" — calculates spending for each category.

Using functions keeps the code organized and easier to manage.

6. Python Concepts that will be Used

- Lists
- Dictionaries
- Functions
- Loops
- Conditional statements
- Arithmetic operations
- f-strings
- Parameters and return values
- Data grouping
- The "datetime" module

7. Example Output

===== SUMMARY =====
Total Income:    ₦150,000
Total Expenses:  ₦4,500
Net Balance:     ₦145,500

===== SPENDING BY CATEGORY =====
Food:            ₦3,000
Transport:       ₦1,500

8. Future Improvements

The project could be improved by adding:

- Saving transactions to a CSV file.
- Loading previous transactions.
- Monthly expense filtering.
- Category spending limits.
- Budget warnings.
- An ASCII chart for spending.
