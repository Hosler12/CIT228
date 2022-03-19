import matplotlib.pyplot as matlib
import numpy as np

# percentage of fast food consumption per day by different sexes and age groups
#https://www.cdc.gov/nchs/data/databriefs/db322_table.pdf#page=1

men = [37.9,46.5,37.6,25.6]
women = [35.4,43.3,37.8,22.7]
total=[36.6,44.9,37.7,24.1]
age_range=["Under 20","20-39","40-59","Over 60"]
barWidth=.25

bar1 = np.arange(len(age_range))
bar2 = [x + barWidth for x in bar1]
bar3 = [x + barWidth for x in bar2]

matlib.xticks([r + barWidth for r in range(len(age_range))], age_range)

matlib.bar(bar1, men, color ='green', width=barWidth, label="Men")
matlib.bar(bar2,women, color="red",  width=barWidth, label="Women")
matlib.bar(bar3, total, color="black", width=barWidth,  label="Total")

matlib.ylabel("Percentage")
matlib.xlabel("Age Range")
matlib.title("Percentage of fast food consumption by age group")
matlib.legend(loc="best")

matlib.show()