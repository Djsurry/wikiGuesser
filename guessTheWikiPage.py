# finished project
import wikipedia
import sys
randomPage = wikipedia.random(1)
randomPageSummary = wikipedia.summary(randomPage)
guesses = 0
print(randomPageSummary)
print("\n")
while guesses != 3:
	print("guess the name of the article. " + str(3-guesses) + " remaining.")
	guess = input()
	if guess.lower() == randomPage.lower():
		print('correct!')
		sys.exit()
	else:
		guesses += 1
print("better luck next time. the name was " + randomPage + ".")
sys.exit()
		

