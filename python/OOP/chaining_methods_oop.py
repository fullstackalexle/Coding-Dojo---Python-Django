class User:
	def __init__(self,name):
		self.name = name
		self.amount = 0

	def make_deposit(self,deposit_amount):
		self.amount += deposit_amount
		return self

	def make_withdrawal(self,withdrawal_amount):
		if withdrawal_amount > self.amount:
			return "Insufficient funds."
		else:
			self.amount -= withdrawal_amount
			return self

	def display_user_balance(self):
		print("User: %s, balance: $%d" % (self.name, self.amount) )
		return self

	def transfer_money(self, other_user, amount):
		other_user.amount += amount
		self.amount -= amount
		self.display_user_balance()
		other_user.display_user_balance()
		return self

barrarighton = User("Barrarighton Sinclair");
tem = User("Tem Fost");
clara = User("Clara Jyness Vasscynthia");

barrarighton.make_deposit(200).make_deposit(100).make_deposit(75).make_withdrawal(200).display_user_balance()

tem.make_deposit(100).make_deposit(100).make_withdrawal(50).make_withdrawal(20).display_user_balance()

clara.make_deposit(500).make_withdrawal(100).make_withdrawal(200).make_withdrawal(50).display_user_balance().transfer_money(barrarighton,100)

