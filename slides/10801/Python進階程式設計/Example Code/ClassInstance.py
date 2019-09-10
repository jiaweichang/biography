class Luffy:
        def __init__(self):
                self.name="Luffy"
        name = "Monkey D. Luffy"
        age = 19

L = Luffy()

L.name = "777"
Luffy.name = "666"

print(L.name)
print(Luffy.name)

LL = Luffy()
print(LL.name)
print(Luffy.name)

