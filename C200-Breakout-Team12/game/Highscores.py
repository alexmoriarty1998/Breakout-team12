class Highscores():
	scores = []
	names = []
	@staticmethod
	def load():
		f = open("highscores.txt", "r")
		for i in range(10):
			Highscores.scores.append(int(f.readline().rstrip()))
		for i in range(10):
			Highscores.names.append(f.readline().rstrip())
		print(Highscores.scores)
		print(Highscores.names)

	@staticmethod
	def add(score: int, name: str):
		for i in range(10) 
			if score > i:
				Highscores.scores[i] = score


