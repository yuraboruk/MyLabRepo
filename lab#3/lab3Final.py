

#YB 11.12.20


try:
    import operator
    import collections
    import datetime
    import csv
    import os
    from itertools import chain
    from tkinter import *
    from tkinter.filedialog import askopenfilename
    
except ImportError:
    from Tkinter import *



"0", "0", "0", "0", "0", "0", "2", "9", "5", "14", "8", "7", "4", "6", 
"2", "8", "14", "17", "11", "4", "12", "13", 
"14", "12", "15", "1", "16", "19", "14", "17", 
"7", "22", "14", "15", "20", "14", "4", "11", 
"18", "23", "24", "21", "25"


#1 - Sort numbers by ascending; create dictionary with pairs {x:n}; export to a csv file
##  Sort in to dictionary {key:value}


original = ["0", "0", "0", "0", "0", "0", "2", "9", "5", "14", "8", "7", "4", "6", 
"2", "8", "14", "17", "11", "4", "12", "13", 
"14", "12", "15", "1", "16", "19", "14", "17", 
"7", "22", "14", "15", "20", "14", "4", "11", 
"18", "23", "24", "21", "25"]




#turn list of str to int 
for i in range(len(original)): 
    original [i] = int(original [i])
    

#sorting original list   
original.sort ()


#creating a dictionary { list item : n list item}
resDict = {}
for i in original:
    count = original.count (i)
    resDict [i] = count


# importing dictionary into csv   
header = [" Value ", " # of Values "]   
with open ('Table In Order.csv', 'w') as f:  
    writer = csv.writer (f)
    writer.writerow (header)
    for key, value in resDict.items ():
        writer.writerow ([key, value])


##########################################


#2 - export a dictionary with numbers that repeat into csv

# import a new dictionary into a csv file, if value is greater or equal to 2
header = [" Value ", " # of Values "]
with open ('Table With Repeats.csv', 'w') as f:  
    writer = csv.writer (f)
    writer.writerow (header)
    for key, value in resDict.items ():
        if value > 1:
            writer.writerow ([key, value])
        
        
##########################################


#3 - show which number repeats the most, and the least


#showing key for the largest value
maxval = max(resDict.values())
maxValue = [key for key, value in resDict.items() if value==maxval]
print 'The value that is repeated the most is', maxValue


#OR with Operator
'''
maxValue = max(resDict.items(), key=operator.itemgetter(1))[0] 
print 'The value that is repeated the most is', maxValue
'''


#showing values that repeat the least
minval = min(resDict.values())
minValue = [key for key, value in resDict.items() if value==minval]
print 'And the values that are repeated the least are', minValue


        

        
        

        
       
