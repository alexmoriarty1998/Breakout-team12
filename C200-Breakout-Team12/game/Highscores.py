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

	@staticmethod
	def isHighScore(score: int):
		# will this score appear on the highscores list?
		return score > Highscores.scores[9]

	@staticmethod
	def add(score: int, name: str):
		###   SCORE   #
		if score < Highscores.scores[9]:
			# not a highscore
			return

		# highscore goes into the list, but not at the beginning
		firstIndexGreaterThan = None
		for i in range(10):
			if score > Highscores.scores[i]:
				firstIndexGreaterThan = i
				break

		beginningPortion = Highscores.scores[0:firstIndexGreaterThan]
		endPortion = Highscores.scores[firstIndexGreaterThan:-1]

		newList = beginningPortion + [score] + endPortion

		Highscores.scores = newList

		### NAME
		beginningPortion = Highscores.names[0:firstIndexGreaterThan]
		endPortion = Highscores.names[firstIndexGreaterThan:-1]

		newList = beginningPortion + [name] + endPortion

		Highscores.names = newList

	@staticmethod
	def printScores():
		print(Highscores.scores)
		print(Highscores.names)
