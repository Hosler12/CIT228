import matplotlib.pyplot as matlib

cubed=[]
inputVal=[1,2,3,4,5]
for num in inputVal:
    cubed.append(num*num*num)
ax1 = matlib.subplot(1,2,1)
ax1.plot(inputVal,cubed, c = 'red', marker = 'o', ls = '-.', lw = '1')
matlib.title("Cubed Numbers")
matlib.ylabel("Values Cubed")
matlib.xlabel("Input Values")
matlib.grid()

powed=[]
inputVal=[1,2,3,4,5]
for num in inputVal:
    powed.append(pow(num,2))
ax2 = matlib.subplot(1,2,2)
matlib.style.use('seaborn-poster')
ax2.plot(inputVal,powed, c = 'orange', marker = 'x', ls = '--', lw = '3')
matlib.title("Numbers Raised")
matlib.ylabel("Second Power")
matlib.xlabel("Input Values")
matlib.grid()

matlib.suptitle("Fun with Numbers")
matlib.subplots_adjust(top = .8, wspace = .3)
matlib.show()