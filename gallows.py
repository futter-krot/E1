# Created using Python 3.9.2

import random, pytest

def round():
	choices = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
	word = random.choice(choices)
	cypher = '-' * len(word)
	attempts = 4

	while attempts != 0:
		print(cypher)
		guess = str(input('Try to guess the letter: ')).lower()

		if guess in word:
			print('Your guess is right')
			new = ''

			for i in range(len(word)):

				if guess == word[i]:
					new += guess

				else:
					new += cypher[i]
			cypher = new

		else:

			if attempts == 1:
				print('You lost!')
				break
			print('Your guess is wrong')
			attempts -= 1

		if cypher == word:
			print('You won!')
			break
	ans = str(input('Wanna play again? Y/N: '))
	round() if ans == 'Y' else print('\nBye')

if __name__ =='__main__':
	round()
