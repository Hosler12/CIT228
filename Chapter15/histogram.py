import matplotlib.pyplot as matlib
#scores showing how many yards students ran in 12 minutes
# 1 mile = 1,760 yards
fitness_test=[2901,1760,3000,2824,3235,2050,2265,2500,2400,2625,3550,1850,1890,3200,2900,2975,3000,2220,2250]

matlib.hist(fitness_test, bins=10, color="green")
matlib.ylabel("# of Students")
matlib.xlabel("Yards")
matlib.suptitle("Yards ran in 12 minutes")

matlib.show()