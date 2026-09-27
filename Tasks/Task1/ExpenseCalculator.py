# Personal Expense Calculator

name = input("Enter your name: ")
category = input("Enter expense category: ")
expenses = int(input("Enter number of expenses: "))

total_expense = 0

for i in range(expenses):
    amount = float(input(f"Enter expense amount {i + 1}: ₹"))
    total_expense += amount

print("Student Name:", name)
print("Expense Category:", category)
print("Number of Expenses:", expenses)
print("Total Expense: ₹", total_expense)