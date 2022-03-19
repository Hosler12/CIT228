import matplotlib.pyplot as matlib

labels = 'PNG', 'JPEG', 'SVG', 'GIF', 'Other'
numPets = [376,348,153,104,19]
explode = (.1, 0, 0, 0, 0)  # only "explode" the 1st wedge
wedgeColors=('lightgreen','purple','lavender','lemonchiffon', 'tan')

fig1, ax1 = matlib.subplots()
ax1.pie(numPets, explode=explode, labels=labels, autopct='%3.1f%%', shadow=True, startangle=-40, colors=wedgeColors)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
matlib.suptitle("Most popular image formats")

matlib.show()