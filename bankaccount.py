class BankAccount:
  def __init__(self):
    self.balance=0
  def __del__(self):
    print("jai shree ram")
    print("     WELCOME to our atm !!!")
  def deposit(self):
    amount=float(input("Enter amount to be Deposited: "))
    self.balance += amount
    print("\n Amount Avlaible BAlance:",amount)

  def withdraw(self):
    amount = float(input("Enter amount to be Withdrawn: "))
    if self.balance>=amount:
      self.balance-=amount
      print("\n You Withdrew:", amount)
    else:
      print("\n Insufficient balance ")

  def display(self):
    print("\n Available Balance is=",self.balance)
    print("HAVE A NICE DAY!!\n Thank You")
del s
s =BankAccount()
s.deposit()
s.withdraw()
s.display()

