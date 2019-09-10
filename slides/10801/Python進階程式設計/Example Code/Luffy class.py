class Luffy:
	def __init__(self,dream):
		print("class 初始化的時候, 執行__init__")
		self.dream = dream

	name = "Monkey D. Luffy"
	age = 19

	def eatmeat(self):
		print("吃肉", self.dream)


L = Luffy("One Piece")
L.eatmeat()

