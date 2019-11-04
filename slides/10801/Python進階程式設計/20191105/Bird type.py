class Bird:
	def fly(self):
		print("I can fly.")

b = Bird()
b.fly()
print(Bird.__class__)


'''
def fly(self):
        print("I can fly.")

Bird = type("Bird", (object,), {'fly':fly})

b = Bird()
b.fly()
'''

