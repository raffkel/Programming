from abc import ABC, abstractmethod

class AbstractFinancialAccount(ABC):
    
    @abstractmethod
    def display_balance():
        pass

class FinancialAccount(AbstractFinancialAccount):
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def add_income(self, amount, description):     #Доходы
        self.balance += amount
        self.transactions.append((amount, description, 'Доходы'))

    def add_expense(self, amount, description): # Расходы
        self.balance -= amount
        self.transactions.append((amount, description, 'Расходы'))

    def remove_transaction(self, index): #Удаление
        if index < len(self.transactions):
            amount, description, transaction_type = self.transactions[index]
            if transaction_type == 'Доходы':
                self.balance -= amount
            elif transaction_type == 'Расходы':
                self.balance += amount
            del self.transactions[index]
        else:
            print("Неверная позиция транзакции.")

    def print_transactions(self): #История
        print("История транзакции:")
        for i, transaction in enumerate(self.transactions):
            amount, description, transaction_type = transaction
            if transaction_type == 'Доходы':
                type_symbol = '+'
            elif transaction_type == 'Расходы':
                type_symbol = '-'
            print(f"{i+1}. {type_symbol} {amount}: {description}")

    def display_balance(self): #Баланс
        print(f"Баланс: {self.balance}")


# Меню
account = FinancialAccount()

try:
    while True:
        print("1. Добавить доходы")
        print("2. Добавить расходы")
        print("3. Убрать транзакции")
        print("4. Вывести историю транзакций")
        print("5. Показать баланс")
        print("0. Выйти")
        choice = input("Выберите цифру (0-5): ")
    
        if choice == '1':
            amount = float(input("Напишите сумму дохода: "))
            description = input("Добавьте описание: ")
            account.add_income(amount, description)
            print("Доход добавлен.\n")
        elif choice == '2':
            amount = float(input("Напишите сумму расхода: "))
            description = input("Добавьте описание: ")
            account.add_expense(amount, description)
            print("Расход добавлен.\n")
        elif choice == '3':
            index = int(input("Напишите номер позиции транзакции для удаления: "))
            account.remove_transaction(index - 1)
            print("Транзакция успешна убрана.\n")
        elif choice == '4':
            account.print_transactions()
            print()
        elif choice == '5':
            account.display_balance()
            print()
        elif choice == '0':
            break
        else:
            print("Неверный выбор.Попытайтесь снова.\n")
except:
    print('error')