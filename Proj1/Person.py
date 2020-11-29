

import datetime

class Person:
    
    def __init__(self):
        
        age = 0
        gender = ""
        Residence = ""
        
        
    def age(self, yearOfBirth):
        
        today = datetime.datetime.now()
        return today.year - yearOfBirth
    
    def sex(self, gender):
        print ("Your gender is: " + gender)
        

    def printResidence(self):
        print ("You live in " + self.Residence)
        
    
        
        
        

        
    