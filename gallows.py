import random

choices = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
attempts = 4

def choose_word(word_list):
    return random.choice(word_list)

def calculate_score(wrong_guesses):
    return max(attempts - wrong_guesses, 0)

class Gallow():

	def __init__(self):
		self.word = choose_word(choices)
		self.cypher = '-' * len(self.word)
		self.attempts = 4
		
	def round(self):

		while self.attempts != 0:
			print(self.cypher)
			guess = str(input('Try to guess the letter: ')).lower()

			if guess in self.word:
				print('Your guess is right')
				new = ''

				for i in range(len(self.word)):

					if guess == self.word[i]:
						new += guess

					else:
						new += self.cypher[i]
				self.cypher = new

			else:

				if self.attempts == 1:
					print('You lost!')
					break
				print('Your guess is wrong')
				self.attempts -= 1

			if self.cypher == self.word:
				print('You won!')
				break
		ans = str(input('Wanna play again? Y/N: '))
		start() if ans == 'Y' else print('\nBye')

def create_game():
    game = Gallow()
    return game

def start():
	game = Gallow()
	game.round()

if __name__ == '__main__':
	start()
