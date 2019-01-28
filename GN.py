#The guessing-a-number-game (I'm not too good at coming up with names)
print("Welcome to yet another game by me. In this game, the computer will generate a random integer, between 0 and 100. All you have to guess what it is. Shouldn't be that hard,right?.............right?")
import random
import math
a=random.randint(0,100)
c=64*math.sqrt(a)
print("Hint",c)
b=input("Anyway, the computer has generated the integer. Guess what it is and type it here: ")
if b.isdigit()==False:
	print("Come on with the jokes pal! -_- \nJust type a number between 1 and 100 next time.Try again, if you want to.")
elif a==int(b):
	print("Congratulations! You've got it correct! The number was, indeed, {0}!".format(b))
elif int(b)<0:
	print("Come on with the jokes pal! -_- \nJust type a number between 1 and 100 next time.Try again, if you want to.")
elif int(b)>100:
	print("Come on with the jokes pal! -_- \nJust type a number between 1 and 100 next time.Try again, if you want to.")
else:
	print("Nah! It wasn't {0}. In fact, it was {1}. Better luck next time though!".format(b,a))