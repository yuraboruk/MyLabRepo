

'''
def create_phone_number(n):
    nString = ''.join(str(x) for x in n)    
    return  "(" + nString[0:3] + ") " + nString[3:6] + "-" + nString[6:10]
   
   

    
    
    




res = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print (res)
res = create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
print (res)
res = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print (res)



# return items from list
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


###########################

# isinstance --> to check for type
#def filter_list(l):
    #return [i for i in l if isinstance(i, int)]
    
    
    



def duplicate_count(text):
    for x in text:
        if text.count(x) >= 2:
            return (x.count)
        
        
        return [x for x in text if x == te]

    








res = duplicate_count("abcde")
print (res)
res = duplicate_count("abcdea")
print (res)
"." "," "!" "?" ":"



def pig_it(text):
    #return " ".join([x[1:] + x[0] + "ay" if x not in (".", ",", "!", "?", ":") else x for x in text.split(" ")])
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in text.split(" ")])

res = pig_it("Pig, latin is cool")
print (res)
res = pig_it("This is my string !")
print (res)

    




#Test.assert_equals(pig_it('Pig latin is cool')
#Test.assert_equals(pig_it('This is my string')





class Team:
    
    
    def __init__(self, Name, Nationality, Position):
        self.Name = Name
        self.Nationality = Nationality
        self.Position = Position
        
    
    def get_Position(self):
        return self.Name + "'s position is " + self.Position
    
    
    def get_Nationality(self):
        return self.Name + " is from " + self.Nationality
    
    
    def get_Info(self):
        return self.Name + " is a(n) " + self.Position + " from " + self.Nationality
    
    
    
    
    
    
    
No15 = Team("Viktor Tsygancov", "Ukraine", "attacker")

print (No15.get_Info())
    
    

northCount = 0


def dirReduc(arr):

    for x in range(len(arr[1:])):
        if x <= len(arr[1:]):
            if (arr[x-1] == "SOUTH" and arr[x] == "NORTH") or (arr[x-1] == "NORTH" and arr[x] == "SOUTH") or (arr[x-1] == "WEST" and arr[x] == "EAST") or (arr[x-1] == "EAST" and arr[x] != "WEST"):
                arr.pop(x-1)
                arr.pop(x-1)
                arr = dirReduc(arr)
    return arr

    for x in range(1,len(arr[1:])):
        if arr[x-1] == "NORTH" and arr[x] == "SOUTH":
            arr.pop(x-1)
            arr.pop(x-1)  
            arr = dirReduc(arr)
        if arr[x-1] == "SOUTH" and arr[x] == "NORTH":
            arr.pop(x-1)
            arr.pop(x-1)
            arr = dirReduc(arr)
        if arr[x-1] == "EAST" and arr[x] == "WEST":
            arr.pop(x-1)
            arr.pop(x-1)
            arr = dirReduc(arr)
        if arr[x-1] == "WEST" and arr[x] == "EAST":
            arr.pop(x-1)
            arr.pop(x-1)
            arr = dirReduc(arr)
                
    return arr









a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
res = dirReduc(a)
print (res)
u =["NORTH", "WEST", "SOUTH", "EAST"]


'''


#def count_smileys(arr):
    
                
        
        
        



#res = count_smileys([])
#print (res)

list = [':D',':~)',';~D',':)']
a = str(list)
x = a.split()
print (x)
#res = count_smileys(a)
#print(res)
#Test.assert_equals(count_smileys([':)',':(',':D',':O',':;']), 2)
#Test.assert_equals(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)

        
        
        
        
