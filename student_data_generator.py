import helper
### public variable section ###
###############################
# number of samples needed
sample_num=100
# degree range :)
degree_range=100
# target file (overwrite)
file_name="student_sample.csv"

###############################
########### Rules #############
# The student pass if he7she got at least 50%  of the average of first and second midterm and at least 50% of the final

## the labels
labels=["first term","second Term","Final","Result"]

##get csv writer
csv_writer=helper.get_csv_writer(file_name)

## store the labels
csv_writer.writerow(labels)

for i in range(sample_num):
    new_sample=helper.get_sample(degree_range)
    csv_writer.writerow(new_sample)    
