# this class is static, to avoid having to pass around an instance of it everywhere

from shutil import copyfile


class Highscores:
	scores = []
	names = []

	@staticmethod
	def load():
		f = open("highscores.txt", "r")
		for i in range(10):
			Highscores.scores.append(int(f.readline().rstrip()))
		for i in range(10):
			Highscores.names.append(f.readline().rstrip())
		f.close()

	@staticmethod
	def isHighScore(score: int):
		# will this score appear on the highscores list?
		return score > Highscores.scores[9]

	@staticmethod
	def add(score: int, name: str):
		###   SCORE   #########################################################
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

		###   NAME   ##########################################################
		beginningPortion = Highscores.names[0:firstIndexGreaterThan]
		endPortion = Highscores.names[firstIndexGreaterThan:-1]

		newList = beginningPortion + [name] + endPortion

		Highscores.names = newList

	@staticmethod
	def printScores():
		# for testing
		print(Highscores.scores)
		print(Highscores.names)

	@staticmethod
	def flush():
		# commits changes to highscore list into the highscores file
		open("highscores.txt", "w").close()  # clears the existing highscores file
		f = open("highscores.txt", "w")
		for i in Highscores.scores:
			f.write(str(i) + '\n')
		for i in Highscores.names:
			f.write(i + '\n')
		f.close()

	@staticmethod
	def reset():
		copyfile("highscores_default.txt", "highscores.txt")
