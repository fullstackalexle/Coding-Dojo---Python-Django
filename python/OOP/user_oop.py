class User:
	def __init__(self,name):
		self.name = name
		self.amount = 0

	def make_deposit(self,deposit_amount):
		self.amount += deposit_amount
		return self.amount

	def make_withdrawal(self,withdrawal_amount):
		if withdrawal_amount > self.amount:
			return "Insufficient funds."
		else:
			self.amount -= withdrawal_amount
			return self.amount

	def display_user_balance(self):
		print("User: %s, balance: $%d" % (self.name, self.amount) )
		return self.amount

	def transfer_money(self, other_user, amount):
		other_user.amount += amount
		self.amount -= amount
		self.display_user_balance()
		other_user.display_user_balance()

barrarighton = User("Barrarighton Sinclair");
tem = User("Tem Fost");
clara = User("Clara Jyness Vasscynthia");

barrarighton.make_deposit(200)
barrarighton.make_deposit(100)
barrarighton.make_deposit(75)
barrarighton.make_withdrawal(200)
barrarighton.display_user_balance()

tem.make_deposit(100)
tem.make_deposit(100)
tem.make_withdrawal(50)
tem.make_withdrawal(20)
tem.display_user_balance()

clara.make_deposit(500)
clara.make_withdrawal(100)
clara.make_withdrawal(200)
clara.make_withdrawal(50)
clara.display_user_balance()

clara.transfer_money(barrarighton,100)

