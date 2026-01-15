print("------------------------- Practice Day 21 ------------------------")

# mini project day 5

# Expense Tracker App
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description=""):
        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }
        self.expenses.append(expense)
        print(f"Added expense: {expense}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        for idx, expense in enumerate(self.expenses, start=1):
            print(f"{idx}. Amount: ${expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

    def total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"Total expenses: ${total}")
# Example usage
tracker = ExpenseTracker()
tracker.add_expense(50, "Groceries", "Weekly grocery shopping")
tracker.add_expense(20, "Transport", "Gas for car")
tracker.view_expenses()
tracker.total_expenses()

# Simple Budget Planner
class BudgetPlanner:
    def __init__(self, monthly_budget):
        self.monthly_budget = monthly_budget
        self.expenses = 0

    def add_expense(self, amount):
        self.expenses += amount
        print(f"Added expense: ${amount}. Total expenses: ${self.expenses}")

    def check_budget(self):
        remaining_budget = self.monthly_budget - self.expenses
        if remaining_budget > 0:
            print(f"You are within budget. Remaining budget: ${remaining_budget}")
        else:
            print(f"You have exceeded your budget by ${-remaining_budget}!")
# Example usage
budget_planner = BudgetPlanner(500)
budget_planner.add_expense(150)
budget_planner.add_expense(200)
budget_planner.check_budget()

print("------------------------ End of Practice Day 21 ------------------------")