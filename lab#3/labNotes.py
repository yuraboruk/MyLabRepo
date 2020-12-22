
#YB 11.12.20


"0", "2", "9", "5", "14", "8", "7", "4", "6", 
"2", "8", "14", "17", "11", "4", "12", "13", 
"14", "12", "15", "1", "16", "19", "14", "17", 
"7", "22", "14", "15", "20", "14", "4", "11", 
"18", "23", "24", "21", "25"


#1 - Sort numbers by ascending; export to a csv file in a pair {x:,n}
##  Sort in to dictionary {key:value}
##  print(len(dict) --> # of items in dict

#list methods:
'''
append()  Adds an element at the end of the list
clear()    Removes all the elements from the list
copy()    Returns a copy of the list
count()    Returns the number of elements with the specified value
extend()    Add the elements of a list (or any iterable), to the end of the current list
index()    Returns the index of the first element with the specified value
insert()    Adds an element at the specified position
pop()    Removes the element at the specified position
remove()    Removes the first item with the specified value
reverse()    Reverses the order of the list
sort()    Sorts the list
'''

#dictionary methods:
'''
clear()    Removes all the elements from the dictionary
copy()    Returns a copy of the dictionary
fromkeys()    Returns a dictionary with the specified keys and value
get()    Returns the value of the specified key
items()    Returns a list containing a tuple for each key value pair
keys()    Returns a list containing the dictionary's keys
pop()    Removes the element with the specified key
popitem()    Removes the last inserted key-value pair
setdefault()    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()    Updates the dictionary with the specified key-value pairs
values()    Returns a list of all the values in the dictionary
    minval = min(resDict.values())
    minValue = [key for key, value in resDict.items() if value==minval]     Returns keys with minimum values
'''


try:
    import collections
    import datetime
    import csv
    import os
    from itertools import chain
    from tkinter import *
    from tkinter.filedialog import askopenfilename
except ImportError:
    from Tkinter import *





original = ["0", "2", "9", "5", "14", "8", "7", "4", "6", 
"2", "8", "14", "17", "11", "4", "12", "13", 
"14", "12", "15", "1", "16", "19", "14", "17", 
"7", "22", "14", "15", "20", "14", "4", "11", 
"18", "23", "24", "21", "25"]




#turn list of str to int 
for i in range(len(original)): 
    original[i] = int(original[i])

#sorting original list   
original.sort ()
#print original

resDict = {}

#creating a dictionary { list item : n list item}
for i in original:
    count = original.count(i)
    resDict [i] = count


# importing dictionary into csv   
header = [" Value ", " # of Values "]    
    
with open('Ordered.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    writer.writerow(header)
    for key, value in resDict.items():
        writer.writerow([key, value])






