



try:
    import datetime
    import csv
    import os
    from itertools import chain
    from tkinter import *
    from tkinter.filedialog import askopenfilename
except ImportError:
    from Tkinter import *

'''
header = ["Transaction", "Date", "Amount"]
transactionsAppOld = [["PayPal", "2020-11-24", "100"],
                ["Contractor", "2020-11-18", "50.00"],
                ["ABD", "2020-11-17", "75"],
                ["LOL", "2021-10-16", "10"],
                ["LOOL", "2020-11-15", "100"],
                ["XYZW", "2020-11-14", "240"],
                ["Meal", "2020-11-16", "20"]]

transactions = [["PayPal", "2020-11-24", "100"],
                ["Contractor", "2020-11-24", "50"],
                ["ABC", "2020-11-25", "75"],
                ["LOL", "2020-11-26", "10"],
                ["XYZ", "2020-11-26", "230"],
                ["Meal", "2020-11-26", "20"]]
transactionsApp = [["PayPal", "2020-11-24", "100"],
                ["Contractor", "2020-11-24", "50.00"],
                ["ABC", "2020-11-25", "74"],
                ["LOL", "2021-10-26", "10"],
                ["LOL", "2020-11-25", "10"],
                ["XYZ", "2020-11-26", "230"],
                ["Meal", "2020-11-26", "20"]]

          
with open ("Bank Statement.csv", "w") as f:   
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(transactions)

with open ("InApp.csv", "w") as a:
    writer = csv.writer(a)
    writer.writerow(header)
    writer.writerows(transactionsApp)

with open ("inAppOld.csv", "w") as f:   
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(transactionsAppOld)
    '''    
    


#transfer each row csv file format to list format
def fileReader(file):
    resList = []
    with open(file) as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            resList.append(row)
    return resList

#summing transactions by date
def autoSum(rawData):
    resList = []
    sum = 0
    length = len(rawData)
    for i in range(length):
        if i == length-1:
            continue
        if i < length-2:
            if rawData [i][1] == rawData [i+1][1]:
                sum = sum + float(rawData [i][2])
            else:
                sum = sum + float(rawData [i][2])
                resList.append ([rawData[i][1], sum])
                sum = 0
        else:
            sum = sum + float(rawData [i][2])
            resList.append ([rawData[i][1], sum])
            
    return resList
      

    
#function to sort raw data list by first element of the table
def sortByDate(elem):
    return elem[1]

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

#serching for duplicates in both in app files
def dupSearch (rawDataInApp, rawDataInAppOld):
    resList = [[""],
               ["Duplicates found in both App files"],
               [""],
               ["Transaction", "Date in Old App", "Date in New App", "Amount"]]
    
    for dataInApp in rawDataInApp:
        for dataInOldApp in rawDataInAppOld:
            if dataInApp [0] != "Transaction" and dataInApp [0] == dataInOldApp [0] and dataInApp[2] == dataInOldApp [2]:
                resList.append ([dataInApp[0], dataInOldApp[1], dataInApp[1], dataInApp [2]])
    
    return resList
                                
        
    

#opening bank statement from user dialogue                
Tk().withdraw() 
filename = askopenfilename(title = "Select Bank Statement file",filetypes = [("CSV files","*.csv")]) 
rawDataBankStatement = fileReader (filename)

#opening in app file from user dialogue
Tk().withdraw()
filename = askopenfilename(title = "Select In App file",filetypes = [("CSV files","*.csv")])
rawDataInApp = fileReader (filename)

#opening old in app file from user dialogue
Tk().withdraw()
filename = askopenfilename(title = "Select Previous In App file",filetypes = [("CSV files","*.csv")])
rawDataInAppOld = fileReader (filename)


#sorting raw data by "date" column
rawDataBankStatement.sort(key=sortByDate)
rawDataInApp.sort(key=sortByDate)
#print (rawDataInApp)
   

#colliding dates and summing transaction values for both files
collapsedDataBankSatatement = autoSum(rawDataBankStatement)
collapsedInApp = autoSum(rawDataInApp)
#print(collapsedDataBankSatatement)

resList = dataMatch (collapsedDataBankSatatement, collapsedInApp)

resDuplicateList = dupSearch (rawDataInApp, rawDataInAppOld)

#write result to 
current_date = datetime.datetime.now()
with open ('Result {}.csv'.format(current_date), "w") as f:   
    writer = csv.writer(f)
    writer.writerows(resList)
    writer.writerows(resDuplicateList)
    
    


    

    