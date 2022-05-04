'''If you're reading this, hello! This is my beginner's attempt at creating a fun little chatbot. Enjoy!'''

from time import sleep
def main():
	#the sleep command is pretty neat, has text after the sleep command delayed by as many seconds as are in the ()
	print("If you\'re reading this then you've been chosen to test my Python project!") ; sleep(3)
	print("Exciting, right? Yeah, not really. It won't be too boring, I promise.") ; sleep(3)
	print("Your job is to do whatever this bot tells you and hope it doesn't break on you") ; sleep(3)
	print("This version will be testing out basic Python functions. It'll be more complex in later versions") ; sleep(3)
	(yourName) = input("First off, what's your name? ")
	print("If that worked correctly, then that means your name is " + (yourName) + ".") ; sleep(3)
	nameLen = len(yourName)
	#use str to turn numbers into strings or else it reads it as "Your name has exactly" + 3 + "letters in it", and that makes no sense
	#when you use str it's like changing 3 into "three"
	print("Your name has exactly " + str(nameLen) + " letters in it.") ; sleep(3)
	print("Getting a computer to say your name may not seem like too big a feat...") ; sleep(3)
	print("That's because it isn't. Still pretty cool to me, though.") ; sleep(3)
	print("Okay, " + (yourName) + ", here\'s the deal.") ; sleep(3)
	print("I'm going to ask you a couple of questions in order to test how well I can respond.") ; sleep(3)
	print("Question #1")
	#input doesn't work because of python 2, so remember to use input instead.
	favAnimal = input("Do you prefer cats or dogs? ")
	if favAnimal == "cats":
		print("Good choice. I'm more of a cat person too.") ; sleep(3)
	elif favAnimal == "dogs":
		print("Dogs are pretty neat. I like Boston Terriers the most.") ; sleep(3)
	else:
		print(favAnimal + " are an interesting choice, but not what I was looking for.") ; sleep(3)
	print("Okay, on to the next question.") ; sleep(3)
	print("Question #2")
	favColor = input("What is your favorite color? ")
	#I use *in []* just in case someone uses caps on the first letter, this way it picks up either Red or red since it's case sensitive
	if favColor in ["red", "Red"]:
		print("What a coincidence! Red is my favorite color too!") ; sleep(3)
	else:
		print(favColor + " is definitely a nice color, I personally prefer red.") ; sleep(3)
	print("Alrighty, next one") ; sleep(3)
	print("Question #3")
	yourAge = input("How old are you? ")
	print(yourAge + ", huh? I'll probably have some witty banter concerning age in a later update.") ; sleep(3)
	print("Okay, last question") ; sleep(3)
	print("Question #4")
	neoCool = input("Is Neo a cool dude? *yes or no* ")
	if neoCool in ["yes", "Yes"]:
		print("Awww, thanks :)") ; sleep(3)
	elif neoCool in ["no", "No"]:
		print(">:(") ; sleep(3)
		print("Rude") ; sleep(3)
	print("Anyways, here's what I've gathered about you, " + (yourName) + ".") ; sleep(3)
	print("When it comes to pets, you prefer " + favAnimal + ".") ; sleep(3)
	if favColor in ["red", "Red"]:
		print("Your favorite color is Red, which is an awesome choice, by the way.") ; sleep(3)
	else:
		print("Your favorite color is " + favColor + ". Not a bad choice.") ; sleep(3)
	print("You are " + yourAge + " years old.") ; sleep(3)
	if neoCool in ["yes", "Yes"]:
		print("And finally, you think that Neo is a cool dude.") ; sleep(3)
		print("Because of that, I will not be submitting your information to the NSA.") ; sleep(3)
	elif neoCool in ["no", "No"]:
		print("And finally, you think that Neo is not a cool dude.") ; sleep(3)
		print("On a completely unrelated note, your information has been submitted to the NSA.") ; sleep(3)
	else:
		print("Also if you're seeing this, then that means you broke the last question by not responding with")
		print("either *yes* or *no*. So I guess that makes you a rebel. Congrats.") ; sleep(3)
	print("Thank you for your compliance :)") ; sleep(3)
	input('This test has finished. Hit ENTER to exit.')
main()