
from abc import ABC, abstractmethod
from time import time


class User(ABC):
	def __init__(self, first_name, last_name, email):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.created_on = time()
	def set_first_name(self, name):
		self.first_name = name
	def set_last_name(self, name):
		self.last_name = name
	@property
	def full_name(self):
		return f"{self.first_name} {self.last_name}"
	@property
	@abstractmethod
	def id(self):
		pass
	def __repr__(self) -> str:
		return f"<{self.email}, {self.created_on}>"
	def __str__(self) -> str:
		return f"<{self.full_name}, {self.email}>"
	def __hash__(self) -> int:
		return int(self.created_on * 1000)
	def __lt__(self, obj):
		return self.created_on < obj.created_on
	def __eq__(self, obj):
		return self.created_on == obj.created_on or self.email == obj.email
	def __gt__(self, obj):
		return self.created_on > obj.created_on

class Employee(User):
	def __init__(self, first_name, last_name, email, home_addr, security_level, department):
		super().__init__(first_name, last_name, email)
		self.home_addr = home_addr
		self.security_level = security_level
		self.department = department
	@property
	def id(self):
		return f"<{self.full_name}, {self.department}>"
	def change_department(self, dep):
		self.department = dep

class Customer(User):
	def __init__(self, first_name, last_name, email, shipping_addr, billing_addr, purchase_history):
		super().__init__(first_name, last_name, email)
		self.shipping_addr = shipping_addr
		self.billing_addr = billing_addr
		self.purchase_history = purchase_history
	@property
	def id(self):
		return f"<{self.email}, {self.shipping_addr}>"
	def change_billing_addr(self, addr):
		self.billing_addr = addr
	def change_shipping_addr(self, addr):
		self.shipping_addr = addr

john = Employee("John", "Remming", "johnrem@gmail.com", "864 Cocoa Drive", 2, "Marketing")
joe = Employee("Joe", "Chorsin", "jchorsin@gmail.com", "County Hwy L", 2, "Marketing")
lilly = Employee("Lilly", "Noshton", "lnoshton@gmail.com", "451 Midway Drive", 2, "Accounting")

emmy = Customer("Emmy", "Jousting", "emmosting@gmail.com", "984 Nautilus Street", "984 Nautilus Street", [ "Soap" ])
jouhan = Customer("Jouhan", "Jousting", "emjousty@gmail.com", "986 Nautilus Street", "984 Nautilus Street", [ "Soap" ])
darek = Customer("Darek", "Kostok", "dakostok@gmail.com", "441 Ave", "441 Ave", [ "Soap" ])

all_users = [john, joe, lilly, emmy, jouhan, darek]

print(all_users)
print(sorted(all_users))

employees = {
	john: "fired",
	joe: "layed off",
	lilly: "promoted"
}
print(employees)