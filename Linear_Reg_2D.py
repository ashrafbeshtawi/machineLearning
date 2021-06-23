
import helper,math
import matplotlib.pyplot as plt
import numpy as np
#   Input
##################################

#The file of the Data set
data_set="SAT_GPA.csv"


#################################



# data set
x_list=[]
y_list=[]



### get csv reader
reader=helper.get_csv_reader(data_set)

## reader the data
for data in reader:
    x_list=x_list+[data[0]]
    y_list=y_list+[data[1]]

#store the labels
x_label=x_list[0]
y_label=y_list[0]
x_list=x_list[1:]
y_list=y_list[1:]

## conver data from string to numbers
for i in range(len(x_list)):
    x_list[i]=float(x_list[i])
    y_list[i]=float(y_list[i])


# Calculating the linear regression values
m,c,max_x,min_x=helper.linear_reg(x_list,y_list)
##################################################################
## end of calculation
## start ploting
# the regression line
x=np.linspace(min_x,max_x,100)
y=m*x+c
plt.plot(x, y, '-b', label='y=mx+c')
# the points
plt.plot(x_list, y_list, 'ro')
plt.show()

