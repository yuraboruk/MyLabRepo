'''
print ("Blablabla")
print ("Blabla" + " :)")
greeting = "Hello,"
name = "Yura"

print (greeting + ' ' + name)

lastname = input("Please enter your last name ")
# input --> will be called first. The value it returns is assigned to a variable name
print (name + ' ' + lastname)
# will ask to input last name


# /n --> causes to start a new line

splitstring = "This string has been\nsplit over\nseveral\nlines"
print(splitstring)


# \t --> tab

tabbedstring = "1\t2\t3\t4\t5"
print (tabbedstring)



line1 = "We"
line2 = "win"
print (line1 + " " + line2)
print (line2[1])


name = "Dynamo Kiev"

#print (name[0:6]) #up to but not including 6 --> Dynamo

print(name)

'''



i = 100
print ("Basic service is {0} dollars, Advanced is {1} dollars, and Premium is {2} dollars".format(i, i + 20, i + 60))

