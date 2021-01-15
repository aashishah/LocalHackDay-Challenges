from bs4 import BeautifulSoup

with open("temp.html") as html_file:
	soup = BeautifulSoup(html_file, "lxml")

for article in soup.find_all("div", class_ = "article"):
	
	headline = article.h2.a.text
	print(headline)

	summary = article.p.text
	print(summary)

	try:
		vid_src = article.find("iframe", class_ = "youtube-player")["src"]
		vid_id = vid_src.split("/")[4].split("?")[0]
		yt_link = f'http://youtube.com/watch?v={vid_id}'

	except:
		yt_link = None

	print(yt_link)
