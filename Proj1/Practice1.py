'''
Created on Nov 10, 2020

@author: rboruk
'''

import socket

boolVerification = True

'''
numOne = 2
numTwo = 0
myLIst = []

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

twoDimArray = {}

newlist = [x for x in fruits if "i" in x]

for x in fruits:
    if "i" in x:
        newlist.append(x)

print(newlist)

#numOne = int(input("Enter amount of times you want to see the word - something: "))
myStr = "strawberry"

numOne = len(myStr)

j = 0

for i in range(numOne):
#    if myStr[i] == "r":
#        continue
    j += 1
    twoDimArray[(0, i)] = myStr[i]

print("Number of letters in strawberry that are not 'r': " + str(j))

print(twoDimArray)


def printResult(result):
    text = "Your result>> " + str(result)
    print(text + '\n')
  
while boolVerification:
    try:
        numOne = int(input("Enter number 1: "))
        sign = input("Enter operation: ") 
        numTwo = int(input("Enter number 2: "))
        if (sign == "+"):
            result = numOne + numTwo
            printResult(result)
        elif(sign == "-"):
            result = numOne - numTwo
            printResult(result)
        elif(sign == "*"):
            result = numOne * numTwo
            printResult(result)
        elif(sign == "/"):
            result = numOne / numTwo
            printResult(result)
    except:
        print("dum dum, you have to enter the number")
        boolVerification = not boolVerification 


team = [("Mike", "M", 20), ("Jimmy", "M", 30), ("Lorry", "F", 33), ("Tiffany", "F", 43), ("Jack", "M", 23), ("Lucy", "F", 25)]
result = []

def showResult(funcText, i):
    global team
    global result
    locResult = []
    
    if i == 1:
        k = len(team)
    else:
        k = len(result)
    for _ in range(k):
        if (i == 1):
            if (team[_][i] == funcText):
                result.append(team[_])
                locResult.append(team[_])
        elif (i == 2):
            if (result[_][i] <= funcText):
                locResult.append(result[_])
    return locResult 

textSex = input("Do you want to list (M)ales or (F)emales: ")
locResult = showResult(textSex, 1)
print(locResult)
textAge = input("Until what age?: ")
locResult = showResult(int(textAge), 2)
print(locResult)

#Lab 1
#you have team of 8 people. Every person has different start time
#return list of people who start work after entered value

#Lab 2
#your client enters date, month and a year of birth
#you show in the result horoscope and the Chinese horoscope
#

#https://www.javatpoint.com/python-files-io
def table(n):    
    return lambda a:a*n # a will contain the iteration variable i and a multiple of n is returned at each function call    

n = int(input("Enter the number:"))    

#b = table(n) #the entered number is passed into the function table. b will contain a lambda function which is called again and again with the iteration variable i    
b = lambda a:a*n
for i in range(1,11):    
    print(n,"X",i,"=",b(i))
    n += 1


lst = (10,22,37,41,100,123,29)  
oddlist = tuple(filter(lambda x:(x%2 == 1),lst)) # the tuple contains all the items of the tuple for which the lambda function evaluates to true    
print(oddlist)

'''
f = open("new.csv",'w')
f.write(",,i can not only write',' but add as well int the file,,\n")
f.write(",20,Vasya,M,\n,30,Petya,M,")
#f.write(",30,Petya,M,\n")
f.close()

#with open("testtext.txt",'r') as f:    
#    content = f.read();    
#    print(content)   

