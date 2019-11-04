class Bird:
        def __init__(self):
                print("init")
        def fly(self):
                print("fly")
        def __new__(self):
                print("new")
                #return object.__new__(self)

b = Bird()
b.fly()

