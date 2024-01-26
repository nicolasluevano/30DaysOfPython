class Statistics:
    def __init__(self, ages: list):
        self.ages = ages

    def count(self):
        return len(ages)

    def sum(self):
        return sum(ages)

    def min(self):
        ages.sort()
        return ages[0]

    def max(self):
        return ages[-1]

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(self.sum() / self.count())

    def median(self):
        sorted_data = ages
        n = self.count()

        if n % 2 == 0:
            middle1 = sorted_data[n // 2 - 1]
            middle2 = sorted_data[n // 2]
            median = (middle1 + middle2) / 2
        else:
            median = sorted_data[n // 2]

        return median
    
    def mode(self):
        frequency = {}
        for age in ages:
            if age in frequency:
                frequency[age] += 1
            else:
                frequency[age] = 1

        # Find the mode(s) and their frequency
        mode = []
        max_frequency = 0
        for key, value in frequency.items():
            if value > max_frequency:
                mode = [key]
                max_frequency = value
            elif value == max_frequency:
                mode.append(key)

        return {mode[0], max_frequency}


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print(data.count())
print(data.sum())
print(data.min())
print(data.max())
print(data.range())
print(data.mean())
print(data.median())
print(data.mode())


# Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self, first_name, last_name, incomes, expenses):
        self.first_name = first_name
        self.last_name = last_name
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self):
        total_income = 0
        for key, value in self.incomes.items():
            total_income += value
        return total_income

    def total_expense(self):
        total_expenses = 0
        for key, value in self.expenses.items():
            total_expenses += value
        return total_expenses
    
    def add_income(self, description, total):
        self.incomes[description] = total

    def add_expense(self, description, total):
        self.expenses[description] = total
    
    def account_balance(self):
        return self.total_income() - self.total_expense()
    
    def account_info(self):
        return f"Welcome {self.first_name} {self.last_name}. Your account balance is {self.account_balance()}"



person = PersonAccount('nicolas', 'luevano', {"income1": 100, "income2": 200, "income3": 300}, {"expense1": 50, "expense2": 50, "expense3": 50})

print(person.incomes)
print(person.add_income("expense5", 900))
print(person.incomes)


    