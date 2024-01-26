class PersonAccount:
    def __init__(self, first_name, last_name, incomes, expenses):
        self.first_name = first_name
        self.last_name = last_name
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self):
        total_income = 0
        for income in self.incomes:
            total_income += income
        return total_income

    def total_expense(self):
        total_expenses = 0
        for expense in self.expenses:
            total_expenses += expense
        return total_expenses
    
    def account_balance(self):
        return self.total_income() - self.total_expense()
    
    def account_info(self):
        return f"Welcome {self.first_name} {self.last_name}. Your account balance is {self.account_balance()}"



person = PersonAccount('nicolas', 'luevano', {100, 200, 300}, {50, 50, 50, 50})

print(person.total_income())
print(person.account_info())