import random,csv
from math import inf
# check if the student pass 
def shall_pass(sample):
    midterms_averg=(sample[0]+sample[1])/2
    if (midterms_averg>= 50) and sample[2]>=50:
        return True
    else:
        return False

### generate random sample ###
def get_sample(degree_range):
    sample=[]
    # generate random data for midterms and final
    for i in range(3):
        sample=sample+[random.randrange(0,degree_range)]
    # add the final result for the student
    sample=sample+[shall_pass(sample)]
    return sample

### open file and return csv writer
def get_csv_writer(file_name):
    #open the file
    fb= open(file_name,"w")
    #prepare the writer
    csv_writer= csv.writer(fb)
    return csv_writer

### open file and return csv reader
def get_csv_reader(file_name):
    #open the file
    fb= open(file_name,"r")
    #prepare the reader
    csv_reader= csv.reader(fb)
    return csv_reader

## get mean of data
def mean_of_data(data_set):

    num_of_sampels=len(data_set)
    sum=0
    mean=0
    for i in range(num_of_sampels):
        sum=sum+data_set[i]
    
    mean=sum/num_of_sampels
    return mean

##read csv file 
def read_csv(path,needed_coloms):
    ## result
    result=[]
    ## get reader
    reader=get_csv_reader(path)
    ## create sub lists
    for i in range(len(needed_coloms)):
        result=result+[[]]
    ## getting the data
    for row in reader:
        index=0
        for colom in needed_coloms:
            result[index]=result[index]+[row[colom]]
            index+=1
    return result

## string list to float
def string_float(mylist):

    result=[]
    for item in mylist:
        result+=[float(item)]
    return result


def linear_reg(xlist,ylist):
    ## calculate the mean
    x_mean=mean_of_data(xlist)
    y_mean=mean_of_data(ylist)


    ### calculate sum((x_i-x_mean)*(y_i-y_mean)) and  (x_i-x_mean)**2
    zahler_summe=0
    nenner_summe=0

    ### max x and min x
    max_x=-inf
    min_x=inf
    for i  in range(len(xlist)):
        #zähler
        zahler_summe=zahler_summe+((xlist[i]-x_mean)*(ylist[i]-y_mean))
        #nenner
        nenner_summe=nenner_summe+(xlist[i]-x_mean)**2
        ### max x and min x
        if(xlist[i]>max_x):
            max_x=xlist[i]

        if(xlist[i]<min_x):
            min_x=xlist[i]

    ### calculating m for y=mx+c
    m=zahler_summe/nenner_summe
    ### calculating c
    c=y_mean-m*x_mean
    return m,c,max_x,min_x



