

#from Person import Person
import datetime
from Student import StudentInfo



'''

Team = [("Jack", 8.00, 16.00), ("Lisa", 8.00, 16.00), ("Jannella", 8.00, 16.00), ("Nicole", 16.00, 24.00), ("Ben", 16.00, 24.00), ("Mark", 16.00, 24.00), ("Stephanie", 0.00, 8.00), ("Ryan", 0.00, 8.00)]

#Team2 = [i for i in Team if i <= k]
answer = int(input("When would you like your appointment?"))


for a, b, c in Team:
    if b <= answer <= c:
        print (a)
'''
        


#Lab 2
#your client enters date, month and a year of birth
#you show in the result horoscope and the Chinese horoscope
#

'''
list = [("Sagitarus", 11-25, 12-25)]
BoD = input("What is your birthday? (mmdd)")

for a,b,c in list:
    if b <= BoD <= c:
        print (a)



import datetime

x = datetime.datetime.now()
print(x)

x = datetime.datetime(2020, 5, 17)

print(x)


#import datetime

from datetime import date
import pandas as pd

zodiac = [("Sagittarius", '2020-11-22', '2020-12-22'), ("Capricorn", '2020-12-23', '2021-01-20')]

first2020 = pd.date_range(start='2020-01-01', end='2020-12-01', freq='MS')



day = int(input("Input birthday: "))
month = int(input("Input month of birth (e.g. 01, 02 etc): "))
year = int(input("Input your year of birth: "))

dateResult = date(year, month, day)
for a, b, c in zodiac:
    if dateResult in pd.date_range(start = b, end = c):
        print (a)
        
        
        
        
        
        
        
        
        
        
        
        
        




if month == 'december':
    astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
elif month == 'january':
    astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
elif month == 'february':
    astro_sign = 'Aquarius' if (day < 19) else 'pisces'
elif month == 'march':
    astro_sign = 'Pisces' if (day < 21) else 'aries'
elif month == 'april':
    astro_sign = 'Aries' if (day < 20) else 'taurus'
elif month == 'may':
    astro_sign = 'Taurus' if (day < 21) else 'gemini'
elif month == 'june':
    astro_sign = 'Gemini' if (day < 21) else 'cancer'
elif month == 'july':
    astro_sign = 'Cancer' if (day < 23) else 'leo'
elif month == 'august':
    astro_sign = 'Leo' if (day < 23) else 'virgo'
elif month == 'september':
    astro_sign = 'Virgo' if (day < 23) else 'libra'
elif month == 'october':
    astro_sign = 'Libra' if (day < 23) else 'scorpio'
elif month == 'november':
    astro_sign = 'scorpio' if (day < 22) else 'sagittarius'


#print("Your Astrological sign is :",astro_sign)




#request the client to input a word until we want to exit by pressing "q"
#count vowels, consonants and count characters and symbols

def searchValueInStr(word, list):
    counter = 0
    for a in word:
        if a in list:
            counter += 1
    return counter

            

word = input ("Please input your 'Word' here: ")

while word != "q":
    

    result = str(searchValueInStr(word, "aeiouAEIOU"))
    print ("You have this many vowels: " + result)
    result = str(searchValueInStr(word, "bcdfg"))
    print ("You have this many consonants: " + result)
    result = str(searchValueInStr(word, "12345"))
    print ("You have this many numeric characters: " + result)
    word = input("Please input your 'Word' here: ")
'''

#objPerson = Person()
year = int(input("What year were you born? "))
gender = input("What is your gender? ")
location = input("Where do you live? ")
objPerson = StudentInfo(year) #cause the function has return
objPerson.Residence = location

 
objPerson.sex(gender) #function has no return
objPerson.printResidence()



           