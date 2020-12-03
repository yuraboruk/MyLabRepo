# lab 2

import datetime
import csv 
import os
from  itertools import chain
from Tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

'''

create a table with heading (10*5)
    write car brand, model, year, color, body type
    
    
    
choose by brand: client chooses brand --> create a new file to show #filter




Javatpoint is your helper


ask to input the model, new file is created (with data stamp) --> here is the path to the new file




cars = open("cars.csv",'w')
cars.write("List of cars available for sale\n")
cars.write(",Brand,Model,Year,Body Type,Colour,Price\n 1, BMW, X3, 2017, SUV, Black, $100000\n 2, BMW, 335i, 2018, Sedan, Silver, $85000\n 3, Subaru, STi, 2015, Sedan, Blue, $45000\n 4, Subaru, WRX, 2017, Hatchback, Yellow, $60000")

#f.write(",30,Petya,M,\n")
cars.close()

#with open("testtext.txt",'r') as f:    
#    content = f.read();    
#    print(content)   

wish = input("Please let us know which model you are interested in buying: ")



import csv

f = open('cars.csv')
csv_f = csv.reader(f)

#for row in csv_f:
    #print (row)
    


for row in csv_f:
    print (row(2))



col_list = ["Brand", "Model", "Year", "Body Type", "Colour", "Price"]

print(["Brand"])
'

import csv    
with open('lol.csv', mode='w') as l:    
    fieldnames = ['emp_name', 'dept', 'birth_month']    
    writer = csv.DictWriter(l, fieldnames=fieldnames)    
    writer.writeheader()    
    writer.writerow({'emp_name': 'Parker', 'dept': 'Accounting', 'birth_month': 'November'})    
    writer.writerow({'emp_name': 'Smith', 'dept': 'IT', 'birth_month': 'October'})    
    writer.writerow({'emp_name': 'BMW', 'dept': 'X3', 'birth_month': '2017'})
    
#############    

Header = [["Brand", "Model", "Year", "Body Type", "Price"]]      
BMW = [["BMW", "X3", "2017", "SUV", "$100,000"],
       ["BMW", "335i", "2018", "Sedan", "$85,000"]]
Subaru = [["Subaru", "STi", "2015", "Sedan", "$50,000"],
          ["Subaru", "WRX", "2016", "Sedan", "$60,000"]]
Honda = [["Honda", "Civic", "2018", "Sedan", "$40,000"],
          ["Honda", "CRV", "2011", "SUV", "$10,000"]]

import csv
with open('Cars Available for Sale.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(Header)
    writer.writerows(BMW)
    writer.writerows(Subaru)
    writer.writerows(Honda)
   
  
choice = input("What vehicle do you want to buy? ")    
with open('Cars Available for Sale.csv') as f:
    reader = csv.reader(f)
if choice == "BMW":
    print(BMW)
if choice == "Subaru":
    print(Subaru)
if choice == "Honda":
    print(Honda)

######
            
'''


'''
Header = ["Brand", "Model", "Year", "Body Type", "Price"]    
BMW = [["BMW", "X3", "2017", "SUV", "$100,000"],
       ["BMW", "335i", "2018", "Sedan", "$85,000"]]
Subaru = ["Subaru", "STi", "2015", "Sedan", "$50,000"]
Honda = [["Honda", "Civic", "2018", "Sedan", "$40,000"],
          ["Honda", "CRV", "2011", "SUV", "$10,000"],
          ["Honda", "Odyssey", "2011", "Van", "$10,000"]]

Manufacturee = [["Brand", "Country", "City", "Manufacturer"],
                ["BMW", "Germany", "Berlin", "Manufacturer 1"],
                ["Subaru", "Japan", "Tokyo", "Manufacturer 2"],
                ["Honda", "Japan", "Kioto", "Manufacturer 3"]]

with open ("Manufacturer.csv", 'w') as m:
    writer = csv.writer(m)
    writer.writerows(Manufacturee)



with open('Cars Available for Sale.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(Header)
    writer.writerows(BMW)
    writer.writerow(Subaru)
    writer.writerows(Honda)
   Cars Available for Sale.csv 
     

def fileReader(file):
    test = []
    with open(file) as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            test.append(row)
    return test

choice = input("What vehicle are you interested in? ")  
cars = fileReader("Cars Available for Sale.csv")
manufact = fileReader("Manufacturer.csv")


cars[0].extend(manufact[0][1:4])

with open("Final File.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(cars[0])
    
    for line in manufact:
        if line [0] == choice:
            for row in cars:
                if row [0] == line [0]:
                    row.extend(line[1:4])
                    writer.writerow(row)
#extract data from 2 files based on input and combine into a new file
'''                  


'''
k = 0        
               
with open('Selection.csv', 'w') as a:
    writer = csv.writer(a)
    writer.writerow(test[0])
    for _ in test:
        if choice == _[0]:
            k += 1
            writer.writerow(_)

if k == 0:
    print ("Your search has shown zero items.")
elif k == 1:
    print ("Your sear has shown 1 item.")
else:
    print ("Your search has returned " + str(k) + " items")
      


############
header = ["Date", "Transaction", "Amount"]
transactions = [["2020-11-24", "PayPal", "100"],
                ["2020-11-24", "Contractor", "50"],
                ["2020-11-25", "ABC", "75"],
                ["2020-11-26", "LOL", "10"],
                ["2020-11-26", "XYZ", "230"],
                ["2020-11-26", "Meal", "20"]]
transactionsApp = [["2020-11-24", "PayPal", "100"],
                ["2020-11-24", "Contractor", "50.00"],
                ["2020-11-25", "ABC", "74"],
                ["2021-10-26", "LOL", "10"],
                ["2020-11-25", "LOL", "10"],
                ["2020-11-26", "XYZ", "230"],
                ["2020-11-26", "Meal", "20"]]

          
with open ("Bank Statement.csv", "w") as f:   
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(transactions)

with open ("InApp.csv", "w") as a:
    writer = csv.writer(a)
    writer.writerow(header)
    writer.writerows(transactionsApp)


'''
def fileReader(file):
    resList = []
    with open(file) as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            resList.append(row)
    return resList

def autoSum(rawData):
    resList = []
    sum = 0
    length = len(rawData)
    for i in range(length):
        if i == length-1:
            continue
        if i < length-2:
            if rawData [i][0] == rawData [i+1][0]:
                sum = sum + float(rawData [i][2])
            else:
                sum = sum + float(rawData [i][2])
                resList.append ([rawData[i][0], sum])
                sum = 0
        else:
            sum = sum + float(rawData [i][2])
            resList.append ([rawData[i][0], sum])
            
    return resList
      

    
#function to sort raw data list by first element of the table
def sortByDate(elem):
    return elem[0]

#this function compares two sets of data for dates and total transaction values
#and validates matches vs inconsistencies
def dataMatch (collapsedDataBankSatatement, collapsedInApp):
    resList = []
    resList.append(["Date", "Result"])
    for date in collapsedDataBankSatatement:
        for dateInApp in collapsedInApp:
            if date[0] == dateInApp[0]:
                if date[1] == dateInApp[1]:
                    resList.append([date[0], "Ok"])
                    break
                else:
                    resList.append([date[0], date[1] - dateInApp[1]])
                    break                
#implementing edge case (no date is found) in Bank Statement 
    for dateInApp in collapsedInApp:
        elem_to_find = dateInApp[0]
        res1 = elem_to_find in chain(*collapsedDataBankSatatement)
        if not res1:
            resList.append ([dateInApp[0], "Date not found on the Bank Statement"])
#implementing edge case (no date is found) in App       
    for date in collapsedDataBankSatatement:
        elem_to_find = date[0]
        res1 = elem_to_find in chain(*collapsedInApp)
        if not res1:
            resList.append ([date[0], "Date not found In App"])    
    return resList

                    
print ("Started")
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename(title = "Select Bank Statement file",filetypes = [("CSV files","*.csv")]) # show an "Open" dialog box and return the path to the selected file
print (filename)

#read raw data from files and input it into the list
rawDataBankStatement = fileReader (filename)

print ("Started second file")

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename(title = "Select In App file",filetypes = [("CSV files","*.csv")]) # show an "Open" dialog box and return the path to the selected file
print (filename)

rawDataInApp = fileReader (filename)



#sorting raw data by "date" column
rawDataBankStatement.sort(key=sortByDate)
rawDataInApp.sort(key=sortByDate)


   

#colliding dates and summing transaction values for both files
collapsedDataBankSatatement = autoSum(rawDataBankStatement)
collapsedInApp = autoSum(rawDataInApp)
#print(collapsedDataBankSatatement)

resList = dataMatch (collapsedDataBankSatatement, collapsedInApp)

#write result to 
current_date = datetime.datetime.now()
with open ('Result {}.csv'.format(current_date), "w") as f:   
    writer = csv.writer(f)
    writer.writerows(resList)
    


