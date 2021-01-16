import smtplib
import time


def getLink(day):
	link = "https://organize.mlh.io/participants/events/635" + f"{day-1}" +"-lhd-build-day" + f"-{day}"
	return link

def remindTotallyNotRyan(day):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo() 
	server.starttls()
	server.ehlo()

	server.login('totallynotryan@mlh.io', "oejbcedkfsvkjsyn") #enter Totally Not Ryan's alternate password for gmail and (actual) user name here 

	subject = "Here's your reminder!"
	link = getLink(day)
	body = "Howdy Totally not Ryan! Here's your reminder to checkin @ MLH LHD: Build.\nClick the link: " + link
	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
		"totallynotryan@mlh.io", #sender
		"totallynotryan@mlh.io", #reciever
		msg 
		) 

	print("Email sent.") #just logging the fact that an email has been sent (lol)

	server.quit() #terminate server connection

day = 1 #Reminder for the seven days of hackathon
while day <= 7:
	remindTotallyNotRyan(day)
  day += 1
	time.sleep(432000)
