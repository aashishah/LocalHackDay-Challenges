#A visualisation of diiferent people's favorite harry potter characters.
import matplotlib.pyplot as plt
from matplotlib import style

characters = ["Harry Potter", "Ron Weasley", "Hermoine Granger", "Draco malfoy", "Dobby"]
numbers = [20, 15, 19, 18, 20]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
plt.pie(numbers, labels = characters, autopct='%1.1f%%', colors = colors, shadow=True, startangle=90)
plt.axis("equal")
plt.show()
