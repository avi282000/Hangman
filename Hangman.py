#Hangman
import random
print("Welcome to HANGMAN!!!\nAhem....!Anyways, In this game, you just have to guess a few alphabets for a given word, in order to complete the word.\nYou will only be given TEN guesses.\nIf you succeed, the computer shall free a virtual prisoner.\nIf you fail, the prisoner WILL BE HANGED TO DEATH!!\nHis/her life depends on your knowledge and/or guesses\nSo, Good luck!")
a=random.randint(0,120)
print("Okay here we go!")
if a<10:
	word="Mittagessen"
	print("MI_ _A_E_ _E_")
	count=0
	point=0
	while count<10:
		user1=input("Incorrect Guesses:- {0}.\nType your guess,or the fruit of your knowledge,here:-".format(count))
		user=user1.capitalize()
		if len(user)>1:
			count+=1
			print("Stop messing around!Incorrect Guesses:- {0}.".format(count))
		elif user=="T":
			point+=2
		elif user=="G":
			point+=1
		elif user=="S":
			point+=2
		elif user=="N":
			point+=1
		else:
			count+=1	
		if point==6:
			break
		elif point>6:
			break
		else:
			pass
	if point==6:
		print("""Congrats! You just saved his/her life.The word is, indeed, "{0}"! """.format(word))
	elif point>6:
		print("You must've messed with the code and tried to cheat by typing a correct word multiple times. The prisoner will be hanged because of that!")
	else:
		print("""The Prisoner will be HANGED!!\nThe word was "Mittagessen". It's German for "lunch", which this prisoner will be turned into, for the fish, after the computer's done with it! """)
elif a<20:
	word="Mustang"
	print("M_ST_ _ G")
	count=0
	point=0
	while count<10:
		user1=input("Incorrect Guesses:- {0}.\nType your guess,or the fruit of your knowledge,here:-".format(count))
		user=user1.capitalize()
		if len(user)>1:
			count+=1
			print("Stop messing around!Incorrect Guesses:- {0}.".format(count))
		elif user=="U":
			point+=1
		elif user=="A":
			point+=1
		elif user=="N":
			point+=1
		else:
			count+=1
		if point==3:
			break
		elif point>3:
			break
		else:
			pass
	if point==3:
		print("""Congrats! You just saved his/her life.The word is, indeed, "{0}"! """.format(word))
	elif point>3:
		print("You must've messed with the code and tried to cheat by typing a correct word multiple times. The prisoner will be hanged because of that!")
	else:
		print("""The Prisoner will be HANGED!!\nThe word was "Mustang".That's gonna be his ride to hell!""")
elif a<30:
	word="Inevitable"
	print("IN_ _I_A_L_")
	count=0
	point=0
	while count<10:
		user1=input("Incorrect Guesses:- {0}.\nType your guess,or the fruit of your knowledge,here:-".format(count))
		user=user1.capitalize()
		if len(user)>1:
			count+=1
			print("Stop messing around!Incorrect Guesses:- {0}.".format(count))
		elif user=="E":
			point+=2
		elif user=="V":
			point+=1
		elif user=="T":
			point+=1
		elif user=="B":
			point+=1
		else:
			count+=1
		if point==5:
			break
		elif point>5:
			break
		else:
			pass
	if point==5:
		print("""Congrats! You just saved his/her life.The word is, indeed, "{0}"! """.format(word))
	elif point>5:
		print("You must've messed with the code and tried to cheat by typing a correct word multiple times. The prisoner will be hanged because of that!")
	else:
		print("""The Prisoner will be HANGED!!\nThe word was "Inevitable", as in "The prisoner's inevitable demise was imminent, as you were the chosen one to save her life!" """)
elif a<40:
	word="CRUELTY"
	print("C_ _ E_TY")
	count=0
	point=0
	while count<10:
		user1=input("Incorrect Guesses:- {0}.".format(count))
		user=user1.capitalize()
		if len(user)>1:
			count+=1
			print("Stop messing around!Incorrect Guesses:- {0}.\nType your guess,or the fruit of your knowledge,here:-".format(count))
		elif user=="R":
			point+=1
		elif user=="U":
			point+=1
		elif user=="L":
			point+=1
		else:
			count+=1
		if point==3:
			break
		elif point>3:
			break
		else:
			pass
	if point==3:
		print("""Congrats! You just saved his/her life.The word is, indeed, "{0}"! """.format(word))
	elif point>3:
		print("You must've messed with the code and tried to cheat by typing a correct word multiple times. The prisoner will be hanged because of that!")
	else:
		print("""The Prisoner will be HANGED!!\nThe word was "Cruelty".That's what the computer had with regards to the prisoner.""")
elif a<50:
	word="Yugoslavia"
	print("YU_ _ SL_VI_")
	count=0
	point=0
	while count<10:
		user1=input("Incorrect Guesses:- {0}.\nType your guess,or the fruit of your knowledge,here:-".format(count))
		user=user1.capitalize()
		if len(user)>1:
			count+=1
			print("Stop messing around!Incorrect Guesses:- {0}.".format(count))
		elif user=="G":
			point+=1
		elif user=="O":
			point+=1
		elif user=="A":
			point+=2
		else:
			count+=1
		if point==4:
			break
		elif point>4:
			break
		else:
			pass
	if point==4:
		print("""Congrats! You just saved his/her life.The word is, indeed, "{0}"! """.format(word))
	elif point>4:
		print("You must've messed with the code and tried to cheat by typing a correct word multiple times. The prisoner will be hanged because of that!")
	else:
		print("""The Prisoner will be HANGED!!\nThe word was "Yugoslavia".A country of this name existed from 1918 to 1992(well, it was officially broken up into Serbia and Montenegro,in 2003,after the unfortunate times of '92), in the Balkan Area of Eastern Europe.\nThat's where the Gulag,holding this prisoner, was! """)
elif a<60:
	word="Paradox"
	print("PA_A_ _ X")
	count=0
	point=0
	while count<10:
		user1=input("Incorrect Guesses:- {0}.\nType your guess,or the fruit of your knowledge,here:-".format(count))
		user=user1.capitalize()
		if len(user)>1:
			count+=1
			print("Stop messing around!Incorrect Guesses:- {0}.".format(count))
		elif user=="R":
			point+=1
		elif user=="D":
			point+=1
		elif user=="O":
			point+=1
		else:
			count+=1
		if point==3:
			break
		elif point>3:
			break
		else:
			pass
	if point==3:
		print("""Congrats! You just saved his/her life.The word is, indeed, "{0}"! """.format(word))
	elif point>3:
		print("You must've messed with the code and tried to cheat by typing a correct word multiple times. The prisoner will be hanged because of that!")
	else:
		print("""The Prisoner will be HANGED!!\nThe word was "Paradox". "[Insert_Something_Slightly_Funny_Here]" """)
else:
	word="SECRET"
	print("_ _ _ _ _ _")
	count=0
	point=0
	while count<10:
		user1=input("Incorrect Guesses:- {0}.\nType your guess,or the fruit of your knowledge,here:-".format(count))
		user=user1.capitalize()
		if count>1:
			count+=1
			print("Stop messing around! Incorrect guesses:- {0}".format(count))
		elif user=="S":
			point+=1
		elif user=="E":
			point+=2
		elif user=="C":
			point+=1
		elif user=="R":
			point+=1
		elif user=="T":
			point+=1
		else:
			count+=1
		if point==6:
			break
		elif point>6:
			break
		else:
			pass
	if point==6:
		print("""Congrats! You just saved his/her life.The word is, indeed, "{0}"! """.format(word))
	elif point>6:
		print("You must've messed with the code and tried to cheat by typing a correct word multiple times. The prisoner will be hanged because of that!")
	else:
		print("""The prisoner will be HANGED! The word was "Secret".Now, You'll have to keep this it!" """)