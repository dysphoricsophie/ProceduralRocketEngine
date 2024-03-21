import random
import matplotlib.pyplot as plt

s = [3, 7, 3, 4]
colors = ['red', 'green', 'blue', 'orange']
labels = str("Prophase\n" + str(round(s[0]/17, 4)*100) + "%"),\
         str("Anaphase\n" + str(round(s[1]/17, 4)*100) + "%"),\
         str("Metaphase\n" + str(round(s[2]/17, 4)*100) + "%"),\
         str("Telophase\n" + str(round(s[3]/17, 4)*100) + "%")
plt.pie(s, labels=labels, colors=[random.choice(colors), random.choice(colors), random.choice(colors), random.choice(colors)])
plt.show()
