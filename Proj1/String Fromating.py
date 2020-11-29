name = "Yura"
print ("Hello, %s!" % name)

age = 23
print ("%s is %d years old." % (name, age))

mylist = [1,2,3]
print ("A list: %s" % mylist)

'''
%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)
'''


info = ("Yura", "Boruk" , 24)
intro = "Hello,"

print (intro % info)




