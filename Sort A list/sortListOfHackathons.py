#Sorting List Of Hackathons alphabettically

from datetime import datetime

def sortAlphabetically(hackathons):
	sortedH = []
	for name in hackathons.keys():
		sortedH.append(name)

	sortedH.sort()
	print("List sorted alphabetically:") 
	print(sortedH)

def sortByDates(hackathons):
        dates = []
        dates = sorted(hackathons.items(), key = lambda date: datetime.strptime(date[1], '%d %b %Y'))
        print("List sorted based on dates:") 
        print(dates)

hackathons = {"Cruz Hacks" : "15 Jan 2021", 
"HackDavis": "16 Jan 2021",
"Hack the Northeast Beyond" : "15 Jan 2021",
"SB Hacks": "15 Jan 2021",
"BoilerMake" : "22 Jan 2021",
"Rose Hack": "16 Jan 2021",
"Elle Hacks": "15 Jan 2021"
}

sortAlphabetically(hackathons)
sortByDates(hackathons)
