

from Person import *

class StudentInfo(Person):
    
    def __init__(self, year):
        course = ""
        grade = 0
        self.printAge(year)
        
    def printAge (self, year):
        print("This year is from StudentInfo class: " + str(year))
        