# VERSION 2.0 OF THE CHALLENGE OF MAKING A BANKING SYSTEM
# WITH UPDATES NOW
import textwrap


def menu():
 menu = """\n
 =============== MENU ===============
 [0]\tDeposit
 [1]\tWithdraw
 [2]\tExtract
 [3]\tNew Account
 [4]\tList Accounts
 [5]\tNew User
 [6]\tQuit
 => """
 return input(textwrap.dedent(menu))

def deposit(balance, amount, statement, /):
 if value > 0:
 balance += value
 statement += f"Deposit:\tR$ {value:.2f}\n"
 print("\n=== Deposit made successfully! ===")
 else:
 print("\n@@@ Operation failed! The value entered is invalid. @@@")

 return balance, statement

def withdraw(*, balance, amount, statement, limit, number_withdrawals, limit_withdrawals):
 exceeded_saldo = value > balance
 exceeded_limit = value > limit
 exceeded_withdrawals = number_withdrawals >= withdrawal_limit

 if exceeded_balance:
 print("\n@@@ Operation failed! You don't have enough balance. @@@")

 elif exceeded_limit:
 print("\n@@@ Operation failed! Withdrawal amount exceeds limit. @@@")

 elif exceeded_withdrawals:
 print("\n@@@ Operation failed! Maximum number of withdrawals exceeded. @@@")

 elif value > 0:
 balance -= value
 extract += f"Withdrawal:\t\R$ {value:.2f}\n"
 number_withdrawals += 1
 print("\n=== Withdrawal completed successfully! ===")

 else:
 print("\n@@@ Operation failed! The value entered is invalid. @@@")

 return balance, statement

def display_extract(balance, /, *, extract):
 print("\n=============== EXTRACT ===============")
 print("No movements were carried out." if not extract else extract)
 print(f"\nBalance: R$ {balance:.2f}")
 print("======================================")

def create_user(users):
 cpf = input("Enter CPF (Number only): ")
 user = filter_user(cpf, users)

 if user:
 print("\n@@@ There is already a user with this CPF! @@@")
 return

 name = input("Enter full name: ")
 date_birth = input("Enter date of birth (dd--mm--yyyy): ")
 address = input("Enter the address (street, number - neighborhood - city/state acronym): ")

 usuarios.append({"name": name, "date of birth": date_birth, "cpf": cpf, "address": address})

 print("=== User registered successfully! ===")

def filter_user(cpf, users):
 usuarios_filtrados = [user for user in users if user["cpf"] == cpf]
 return filtered_users[0] if filtered_users else None


def create_account(agency, account_number, users):
 cpf = input("Enter the user's CPF: ")
 user = filter_user(cpf, users)

 if user:
 print("\n=== Account Created Successfully! ===")
 return {"agency": agency, "account_number": account_number, "user": user}

 print("\n@@@ User not found, account creation flow closed! @@@")

def list_accounts(accounts):
 for account in accounts:
 line = f"""\
 Agency:\t{account["agency"]}
 C/C:\t\t{account["account_number"]}
 Holder:\t{account["user"]["name"]}
 """
 print("=" * 100)
 print(textwrap.dedent(line))

def main():
 WITHDRAWAL_LIMIT = 3
 AGENCY = "0001"

 balance = 0
 limit = 500
 extract = ""
 number_withdrawals = 0
 users = []
 accounts = []

 whileTrue:
 option = menu()

 if option == "0":
 value = float(input("Enter the deposit amount: "))

 balance, statement = deposit(balance, amount, statement)

 elif option == "1":
 value = float(input("Enter the withdrawal value: "))

 balance, statement = withdraw(
 balance=balance,
 value=value,
 extract=extract,
 limit=limit,
 number_withdrawals=number_withdrawals,
 limit_saques=LIMITE_SAQUES,
 )





 elif option == "2":
 display_statement(balance, statement=statement)

 elif option == "3":
 create_user(users)

 elif option =="4":
 account_number = len(accounts) + 1
 account = create_account(AGENCY, account_number, users)

 if counts:
 accounts.append(account)

 elif option =="5":
 list_accounts(accounts)

 elif option =="6":
 break

 else:
 print("Invalid operation, please select the desired operation again.")


main()
