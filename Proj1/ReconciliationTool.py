


'''
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

header = ["Date", "Transaction", "Amount"]
transactionsApp = [["2020-11-24", "PayPal", "100"],
                ["2020-11-18", "Contractor", "50.00"],
                ["2020-11-17", "ABD", "75"],
                ["2021-10-16", "LOL", "10"],
                ["2020-11-15", "LOOL", "100"],
                ["2020-11-14", "XYZW", "240"],
                ["2020-11-16", "Meal", "20"]]


with open ("inAppOld.csv", "w") as f:   
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(transactions)
    
    
    

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

#opening bank statement from user dialogue                
Tk().withdraw() 
filename = askopenfilename(title = "Select Bank Statement file",filetypes = [("CSV files","*.csv")]) 
rawDataBankStatement = fileReader (filename)

#opening in app file from user dialogue
Tk().withdraw()
filename = askopenfilename(title = "Select In App file",filetypes = [("CSV files","*.csv")])
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
    '''
    