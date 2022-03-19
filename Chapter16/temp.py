import csv
import matplotlib.pyplot as matlib
from datetime import datetime

date=[]
temp_max = []
temp_min = []

with open('Chapter16/temp_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header_row=next(csv_reader)
    for row in csv_reader:
        date.append(datetime.strptime(row[2],'%Y-%m-%d'))
        if row[4]=='NULL':
            temp_max.append(0)
        else:
            temp_max.append(float(row[4]))
        if row[5]=='NULL':
            temp_min.append(0)
        else:
            temp_min.append(float(row[5]))

matlib.scatter(date, temp_max, c='red', label="temp max",s=50)
matlib.scatter(date, temp_min, c='blue', label="temp min",s=50)
matlib.ylabel("Temp")
matlib.xlabel("Dates")

matlib.legend(loc='lower right', ncol=2, fontsize=8)
matlib.grid()

matlib.suptitle("Traverse City Temps")
matlib.show()