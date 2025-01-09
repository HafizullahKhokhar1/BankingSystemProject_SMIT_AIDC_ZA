class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: {amount}")
            return f"{amount} deposited successfully."
        return "Invalid amount."

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrew: {amount}")
            return f"{amount} withdrawn successfully."
        return "Insufficient balance or invalid amount."

    def check_balance(self):
        return f"Current balance: {self.balance}"

    def add_transaction(self, description):
        self.transactions.append(description)

    def print_statement(self):
        if self.transactions:
            return "\n".join(self.transactions)
        return "No transactions available."

class Bank:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1

    def open_account(self, account_holder):
        account_number = self.next_account_number
        self.accounts[account_number] = BankAccount(account_number, account_holder)
        self.next_account_number += 1
        return f"Account created successfully. Account Number: {account_number}"

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def transfer(self, sender_account_number, receiver_account_number, amount):
        sender = self.get_account(sender_account_number)
        receiver = self.get_account(receiver_account_number)
        if sender and receiver:
            if sender.balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                return f"{amount} transferred from {sender_account_number} to {receiver_account_number}."
            return "Insufficient balance in sender's account."
        return "Invalid account numbers."

    def admin_check_total_deposit(self):
        return sum(account.balance for account in self.accounts.values())

    def admin_check_total_accounts(self):
        return len(self.accounts)


def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Banking System")
        print("1. Open Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Print Transaction Statement")
        print("7. Admin: Check Total Deposits")
        print("8. Admin: Check Total Accounts")
        print("9. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter account holder's name: ")
            print(bank.open_account(name))
        elif choice == "2":
            acc_num = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))
            account = bank.get_account(acc_num)
            if account:
                print(account.deposit(amount))
            else:
                print("Account not found.")
        elif choice == "3":
            acc_num = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))
            account = bank.get_account(acc_num)
            if account:
                print(account.withdraw(amount))
            else:
                print("Account not found.")
        elif choice == "4":
            acc_num = int(input("Enter account number: "))
            account = bank.get_account(acc_num)
            if account:
                print(account.check_balance())
            else:
                print("Account not found.")
        elif choice == "5":
            sender_acc = int(input("Enter sender's account number: "))
            receiver_acc = int(input("Enter receiver's account number: "))
            amount = float(input("Enter amount to transfer: "))
            print(bank.transfer(sender_acc, receiver_acc, amount))
        elif choice == "6":
            acc_num = int(input("Enter account number: "))
            account = bank.get_account(acc_num)
            if account:
                print(account.print_statement())
            else:
                print("Account not found.")
        elif choice == "7":
            print(f"Total deposits: {bank.admin_check_total_deposit()}")
        elif choice == "8":
            print(f"Total accounts: {bank.admin_check_total_accounts()}")
        elif choice == "9":
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
