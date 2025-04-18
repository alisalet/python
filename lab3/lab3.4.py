class BankAccount:
    def __init__(self,initial_balance=0):
        self._balance=initial_balance
        self._transactions=[]

    def deposit(self,amount):
        """"Валидация пополнений + обновляет баланс"""
        if amount>0:
            self._balance+=amount
            self._transactions.append(f'Пополнение: +{amount:.2f}')
        else:
            print('Нельзя вносить отрицательное количество денег :(')

    def withdraw(self,amount):
        """Валидация снятия + обновление баланса"""
        if 0<amount<=self._balance:
            self._balance-=amount
            self._transactions.append(f'Снятие: -{amount:.2f}')
        else:
            print('Недостаточно средств или неверная сумма')

    @property
    def balance(self):
        return self._balance

    def show_transactions(self):
        """Выводит все операции"""
        print('История операций:')
        for transaction in self._transactions:
            print(transaction)
        print('\n')

if __name__=='__main__':
    client1=BankAccount(100)
    client1.deposit(500)
    client1.withdraw(123)
    print(f'Текущий баланс: {client1.balance:.2f}')
    client1.show_transactions()

    client2=BankAccount(1000000)
    client2.deposit(-1000000)
    client2.deposit(1)
    client2.withdraw(100)
    print(f'Текущий баланс: {client2.balance:.2f}')
    client2.show_transactions()