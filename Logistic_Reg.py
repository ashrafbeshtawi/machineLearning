
import helper,math
import matplotlib.pyplot as plt
import numpy as np
#   Input
##################################

#The file of the Data set
data_set="height_sex.csv"


#################################

## reading the csv file
data=helper.read_csv(data_set,[1,2])
height=data[0]
sex=data[1]

label1=height[0]
label2=sex[0]

height=helper.string_float(height[1:])
sex=helper.string_float(sex[1:])
## linear regression
m,c,max_x,min_x=helper.linear_reg(height,sex)

print(m,c,min_x,max_x)



## start ploting
# the regression line
x=np.linspace(0,max_x,int(max_x-min_x))
y_regression=m*x+c
y=1/(1+np.exp(-(m*x+c)))#np.exp(m*x+c)/(1+np.exp(m*x+c))#m*x+c 
y_test=x**2
plt.plot(x, y_regression, '-b', label='linear regression')
plt.plot(x, y, '-g', label='logisitc regression')
#plt.plot(x, y_test, '-b', label='logisitc regression')
# the points
plt.plot(height, sex, 'ro')
plt.show()