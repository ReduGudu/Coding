'''Assignment - 1: Use least square method to obtain appropriate fit for the data
x = [1, 4, 7, 11, 15, 20, 30, 50, 77, 92, 100] and y = [    5    20    52   121   228   403   903  2504  5929  8464 10005]
Enamul Hoque'''

from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")
#Calling the values of x and y
x=[1,4,7,11,15,20,30,50,77,92,100]
y=[5,20,52,121,228,403,903,2504,5929,8464,10005]
print("The value of x=",x)
print("\nThe value of y=",y)
#Plotting the graph
plt.plot(x,y,label="line",linewidth=2)
plt.xlabel="X-axis"
plt.ylabel="Y-axis"
plt.scatter(x,y)
plt.show()

#finding the mean
sumx=sum(x)
sumy=sum(y)

meanx=sumx/len(x)
meany=sumy/len(y)

devx=list()
devy=list()
#Finding the values of (x-meanx) and (y-meany)
for w in x:
    x1=w-meanx
    devx.append(x1)
print("\nThe elements of (x-meanx)\n",devx)

for t in y:
    y1=t-meany
    devy.append(y1)
print("\nThe elements of (y-meany)\n",devy)

#suaring (x-meanx)
squareddevx=list()

for m in devx:
    sqrtdevx=m**2
    squareddevx.append(sqrtdevx)

m=sum(squareddevx)
print("\nThe sum of the suare of the elements of (x-meanx)=",m)
i=0
#Finding the values of (x-meanx)*(y-meany) and getting the sum of the values
sumofproduct=list()


for i in range(len(devx)):

    c=devx[i]*devy[i]
    sumofproduct.append(c)
n=sum(sumofproduct)
print("\nThe sum of (x-meanx)*(y-meany)=",n)
#Finding the slope
slope=n/m

print("\nThe slope is=",slope)
print("We know, that,\ny=a0+a1x ")
print("Again in the equation,\nx=meanx\ny=meany\nand, a1=slope\nSo, the equation becomes meany=a0+(slope*meanx)")
a0=meany-(slope*meanx)
print("So,\nThe value of a0:",a0)
print("The final equation is:y=",a0,"-",slope,"x")


