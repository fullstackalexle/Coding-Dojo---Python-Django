class BankAccount:
	def __init__(self, interest_rate=0.01, balance=0):
		self.interest_rate = interest_rate
		self.balance = balance

	def deposit(self,amount):
		self.balance += amount
		return self
	
	def withdraw(self,amount):
		if amount > self.balance:
			self.balance -= 5
			print("Insufficient funds: Charging a $5 fee")
			return self 
		else:
			self.balance -= amount
			return self

	def display_account_info(self):
		print("Balance: $%d" % (self.balance))
		return self

	def yield_interest(self):
		if self.balance > 0:
			self.balance += (self.balance * self.interest_rate)
		return self

class User:
	def __init__(self,name):
		self.name = name
		self.accounts = { 
			"checking": BankAccount(), 
			"savings": BankAccount() 
		};

	def make_deposit(self,deposit_amount, type_of_account):
		self.accounts[type_of_account].balance += deposit_amount
		return self

	def make_withdrawal(self,withdrawal_amount, type_of_account):
		if withdrawal_amount > self.accounts[type_of_account].balance:
			return "Insufficient funds."
		else:
			self.accounts[type_of_account].balance -= withdrawal_amount
			return self

	def display_user_balance(self):
		print("User: %s, Savings Account Balance: $%d" % (self.name, self.accounts["savings"].balance) )
		print("User: %s, Checking Account Balance: $%d" % (self.name, self.accounts["checking"].balance) )
		return self

	def transfer_money(self, other_user, amount):
		other_user.accounts["checking"].balance += amount
		self.accounts["checking"].balance -= amount
		self.accounts["checking"].display_user_balance()
		other_user.accounts["checking"].display_user_balance()
		return self

user1 = User("user1")
user1.make_deposit(200,"checking").make_deposit(100,"savings").make_deposit(75,"checking").make_withdrawal(200,"checking").display_user_balance()
