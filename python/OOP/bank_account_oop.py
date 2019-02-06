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

checking = BankAccount();
savings = BankAccount();

checking.deposit(200).deposit(175).deposit(200).withdraw(180).yield_interest().display_account_info()

savings.deposit(500).deposit(1000).withdraw(500).withdraw(200).withdraw(80).withdraw(120).yield_interest().display_account_info()