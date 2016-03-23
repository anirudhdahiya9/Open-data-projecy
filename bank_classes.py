# define class for Account
class my_account:
	#constructor
	def __init__(self, name=""):
		#instance variables
		self.__name = name    # Double underscores implies private variable
		self.__balance = 0
			
	#instance methods
	def deposit(self,amount):
		print ("Depositing amount: " + str(amount))
		self.__balance = self.__balance + amount


	def withdraw(self,amount):
		if ((self.__balance - amount) >= 0):
			print ("Withdrawing amount: " + str(amount))
			self.__balance = self.__balance - amount
		else:
			print ("Insufficient balance of: " + str(self.__balance) + " , You are withdrawing: " + str(amount))

	def __str__(self):
		return "%s account balance is: %s" % (self.__name , self.__balance)


def main():
	a = my_account("Luffy")
	a.deposit(100)
	print a
	a.withdraw(50)
	print a
	a.withdraw(75)
	print a
	

if __name__ == "__main__":
	main()
