print("WELCOME TO THE QUIZ.\n Quick Rules:\n 1. Answer Yes/No questions with yes/no in full words. \n That's all.")

name = input("K. What's your name, bud?\n")
ans1 = input("Alright, {}. Do you think you are you a BLAHAJista?\n".format(name))
count = 0
hasBLAHAJ = False
if ans1.lower() == "yes":
	count += 10
	ans2 = input("Is that so? Where is BLAHAJ from?\n")
	if ans2.lower() in ["sweden", "ikea"]:
		count += 10

	ans3 = input("Uhuh. What is even a BLAHAJ?\n")
	if ans3.lower() in ["a shark", "shark"]:
		count += 10

	ans4 = input("Sure. Do you own a BLAHAJ?\n")
	if ans4.lower() == "yes":
		hasBLAHAJ = True

	ans5 = input("Hmm. Who is the BLAHAJGang leader?\n")
	if ans5.lower() in ["jack", "jacklyn", "jacklyn biggin"]:
		count += 10

	print("\n\nDRUM ROLL PLEASE. The final verdict:")
	if count == 10:
		print("False claims much? Not really a BLAHAJista :(")
	if count == 20:
		if hasBLAHAJ:
			print("Because you have a BLAHAJ, you are a BLAHAJista. BUT DO YOUR RESEARCH.")
		else:
			print("Not quite the BLAHAJista, do your research!")
	if count == 30:
		print("You are a half BLAHAJista.")
	if count == 40:
		if hasBLAHAJ:
			print("YOU ARE THE BIGGEST BLAHAJISTA EVER. ALL HAIL.")
		else:
			print("You have all the knowledge. But no BLAHAJ. A trip to IKEA is due.")


else:
	print("\nWhy are you taking this quiz then? -_-")





