

#lambda functions/expressions --> anonymous, short, throw-away function

#lambda argument(s)/bound variable(s): expression that will be returned

#lambda function supports all kinds of input arguments just like a def function

#lambda function only accepts single expression --> does not need to be assigned to a value

#lambda function can’t contain any statements (return, try, if, for, etc) (only to return True/False)

#map, filter, reduce are most often used with lambda functions

import functools

#1
seven = lambda x: 3*x+1
print (seven(2))

#2
#three = (lambda x, y: x+y)(1, 2)
print((lambda x, y: x+y)(1,2))

#3
print(sorted(range(-5, 6), key=lambda x: x**2))

#4
fullName = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print (fullName("  yura", "BORUK"))


#5 map
# map() is useful when you need to apply a transformation function to each item in an iterable and transform them into a new iterable.
# map() function takes 2 arguments: an input mapping function and an iterable. The mapping function will be applied to each element in the iterable. map() function returns an iterator containing the mapped elements.

a = [1,2,3,4,5,6,7,8,9,10]

newList = list(map(lambda x: x+1, a)) # list(map(lambda x: x+1, [1,2,3,4,5,6,7,8,9,10]))
print (newList)

#6 filter
#filter() function takes the same arguments as map(): an input filtering function and an iterable. 
#The filtering function will be applied to each element and filter() function returns an iterator containing the filtered elements.

newList = list(filter(lambda x: x%2==0, a))
print (newList)



#7 reduce
#The function reduce(func, sequence) continually applies the function to the sequence and returns a single value. 
#functools.reduce

f = functools.reduce(lambda a,b: a+b,[47,11,42,13])
print (f)



#8 lexical closure (a fancy name for a function that remembers the values from the enclosing lexical scope even when the program flow is no longer in that scope)
# x + n lambda can still access the value of n even though it was defined in the make_adder function (the enclosing scope).
def make_adder(n):
    return lambda x: x + n

plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4))

print(plus_5(4))

