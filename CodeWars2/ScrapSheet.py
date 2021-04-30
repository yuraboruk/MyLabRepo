

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




        


RomanDict = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
       

def solution(roman):
    
    
    Values = 0
    rom = [roman[x] for x in range(len(roman))]
    rom_iter = iter(rom)
    i = 0
    print (rom)
    for x in rom_iter:
        if i < len(rom)-1:
            if RomanDict[rom[i]] >= RomanDict[rom[i+1]]:
                Values += RomanDict[rom[i]]
                i += 1
            else:
                Values += RomanDict[rom[i+1]] - RomanDict[rom[i]]
                next (rom_iter)
                i += 2
                #continue
        elif i == len(rom)-1:
            Values += RomanDict[rom[i]]
            
            
            
    return str(Values)
        
        
     
       
res = solution('MCMXC')
print (res)
res = solution('MDCLXVI')
print (res)
res = solution('MMVIII')
print (res)

if x == False:
            array.insert(array.index(False), False)

#any(x is False for x in [0, 1, 3])

#False in filter(lambda x: isinstance(x, bool), [0, 1, 2])
#any(False is not 0 for x in array)   


def move_zeros(array):
    
    for x in array:
        if type(x) == int and type(x) != bool:
            if (x == 0 and type(x) == int):
                array.remove(x)
                array.append(x)
      
            
    return array







res = move_zeros([1,2,0,1,0,1,0,3,0,1])
print(res)

res = move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9])
print(res)
res = move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9])
print(res)
#res = move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9])
#print(res)
#Test.assert_equals(move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
#Test.assert_equals(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]),[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
#Test.assert_equals(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]),["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
#Test.assert_equals(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])  



import string
string.capwords("they're bill's friends from the UK")
>>>"They're Bill's Friends From The Uk"


replace(' ', '')))


def generate_hashtag(s):
    
    if 0 < len(s) <= 140:
        return "#" + s.title().replace(' ', '')
        #Cap = Slap.replace(' ', '')
        #return ("#" + Cap)
    else:
        return(False)
    
    



res = generate_hashtag('Codewars')
print(res)

res = generate_hashtag('Codewars Is The Best')
print(res)

res = generate_hashtag(' codewars is nice ')
print(res)








def cakes(recipe, available):
     
    portions = [int(available[item] / recipe[item]) if item in available else 0 for item in recipe]
    return min(portions)
        





recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1300, "sugar": 1200, "eggs": 5, "milk": 200}
res = cakes(recipe, available)
print (res)

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
res = cakes(recipe, available)
print (res)






res =  [(a, b), (b, a)] if a * b == s-a-b else ""
            return res
            
            
            
 Num = list(range(n+1))
    s = sum(Num)

    for a in Num[:-1]:
        for b in Num[1:]:
            if a*b == s-a-b and a != b:
                return [(a, b), (b, a)]
    return []





def remov_nb(n):
    
    s = sum(range(n+1))
    res = []
    
    for a in range(n):
        if (s - a)%(a + 1) == 0:
            b = (s - a)/(a + 1)
            if b <= n and a != b:
                    res.append((a, int(b)))
    return res
    


res = remov_nb(1000)
print (res)
res = remov_nb(100)
print (res)
res = remov_nb(101)
print (res)

(26, [(15, 21), (21, 15)])
        testing(100, [])
        testing(101, [(55, 91), (91, 55)])
      

def is_merge(s, part1, part2):
    
    if part1 + part2 == s:
        return True
    else:
        return False




res = is_merge('codewars', 'code', 'wars')
print(res)
res = is_merge('codewars', 'cdw', 'oears')
print(res)
res = not is_merge('codewars', 'cod', 'wars')
print(res)
'






def rank(st, we, n):
    
    res = []
    weInd = 0
    NameSum = 0
    Winner = []
    
    lowSt = st.lower()
    Names = lowSt.split(",")
    stLength = len(Names)
    if stLength == 0:
        return "No Participants"
    
    
    if stLength >= n:
        for Person in Names:
            for l in Person:
                NameSum += ord(l) - 96
            Winner.append((NameSum + len(Person)) * we[weInd])
            weInd += 1
                
        res = Winner.sort()
        return res[n]
        
        
        
        d['mynewkey'] = 'mynewvalue'

import operator
       
               
def rank(st, we, n): 
    
    res = []
    weInd = 0
    NameSum = 0
    
    WinList = {}
    

    lowSt = st.lower()
    Names = lowSt.split(",")
    stLength = len(Names)
    
    if not st:
        return "No participants"
    
    if stLength < n:
        return "Not enough participants"
    
    
    if stLength >= n:
        for Person in Names:
            for l in Person:
                NameSum += ord(l) - 96
            WinList[Person] = (NameSum + len(Person)) * we[weInd]
            
            weInd += 1
            NameSum = 0
       
        NewList = list(WinList)    
        print(NewList)
        NewList.sort(key = lambda x: (-x[1],x[0]))   
        #DesWinList = sorted(WinList.items(), key=operator.itemgetter(1),reverse=True)
        #DesWinList = sorted(WinList, key = lambda x: (-x[1],x[0]))
        #DesWinList.sorted(tup, key = lambda x: x[0]))
                
                
                
                #AlphWinList = sorted(WinList.keys(), key=lambda x:x.lower())
                
        return NewList[n-1][0]
            
        
         
        # WinList.keys(), key=lambda x:x.lower())
    
        return DesWinList[n-1][0].capitalize()
    
    
    
            
    



#res = rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4)
#print (res)
#res = rank("Lagon,Lily", [1, 5], 2)
#print (res)
#res = rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8)
#print (res)
#res = rank("", [4, 2, 1, 4, 3, 1, 2], 6)
#print (res)

res = rank("William,Willaim,Olivia,Olivai,Lily,Lyli", [1, 1, 1, 1, 1, 1], 1)
print (res)


def rank(st, we, n): 

    if not st:
        return "No participants"
    
    if n>len(we):
        return "Not enough participants"
    
    name_score = lambda name,w: w*(len(name)+sum([ord(c.lower())-96 for c in name]))
    
    scores= [name_score(s,we[i]) for i,s in enumerate(st.split(','))]
    print(scores)
    
    scores = list(zip(st.split(','),scores)) 
    print(scores)   
    
    scores.sort(key=lambda x: (-x[1],x[0]))
    print(scores)
    
    return scores[n-1][0]



res = rank("Willaim,Olivia,Olivai,Lily,Lyli,", [1, 1, 1, 1, 1, 1], 1)
print (res)


import re

def solution(s):
    #String = str(s)
    return re.sub(r"(\w)([A-Z])", r"\1 \2", s)




res = solution("helloWorld")
print(res)
#Test.assert_equals(solution("camelCase"), "camel Case")
#Test.assert_equals(solution("breakCamelCase"), "break Camel Case")




def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)



divide(2,5)



@lazy(n)
    def mul(a,b):
        return (a*b)

def lazy(n):
    def decor_real(func):
        
        
    return decor_real
        
    def mul(a, b):
        return a*b
    if n > 0:
        for j in range (3*n):
            
    
    if n == 1:
        return mul(a, b)
    
    
    def repeat_fun(times, f):
        for i  list(repeat(f(), x)
                    
                    
                    
                    
def lazy(n):
    def decor_real(f):
        def wrapper(a, b):
            if n > 1:
                return [f(a, b) if i == 0 or i == n else None for i in range(n+1)]
            elif n == 1: return f(a, b)
            elif n == -1: return None
            else:
                return [None if i == 0 or i == abs(n) else f(a, b) for i in range(abs(n)+1)]
        return wrapper
    return decor_real

@lazy(-4)
def mul(a, b):
return a*b





def lazy(n):
def decor_real(f):
def wrapper(a, b):
print("a = " + str(a) + " b = " + str(b) + " n = " + str(n))
if n > 1:
return [f(a, b) if i == 0 or i == n else None for i in range(n+1)]
elif n == 1: return f(a, b)
elif n == -1: return None
else:
return [None if i == 0 or i == abs(n) else f(a, b) for i in range(abs(n)+1)]
return wrapper
return decor_real
@lazy(2)
def mul(a, b):
return a*b





    
extCounter = -1
iterNum = 0

def lazy(n):
global extCounter
global iterNum
if iterNum != n:
iterNum = n
extCounter = -1

def decor_real(f):
def wrapper(*args, **kwargs):
global extCounter
extCounter += 1
if len(args) == 0:
return 2
elif len(args) == 1:
 if n > 1:
return (f(args[0]) if extCounter == 0 or extCounter%n else None)
elif n == 1: return f(args[0])
elif n == -1: return None
else:
return (None if extCounter == 0 or extCounter%abs(n) else f(args[0]))
elif len(args) == 2:
a = args[0]
b = args[1]
print("a = " + str(a) + " b = " + str(b) + " n = " + str(n)+ " Counter = " + str(extCounter))
if n > 1:
return (f(a, b) if extCounter == 0 or extCounter%n == 0 else None)
elif n == 1: return f(a, b)
elif n == -1: return None
else:
return (None if (extCounter+1)%abs(n) == 0 else f(a, b))
return wrapper
return decor_real




from collections import defaultdict

def stock_list(b, c):
    
    stock = []
    ans = []
    
    if b is None or c is None or len(b)==0 or len(c)==0:
        return ""
    
    
    for i in b:
        stock.append([i.split()[0][0], int(i.split()[1])])
        

    d = defaultdict(int)
    for x, y in stock:
        d[x] += y
    
    
    for item in c:
        if item in d:   
            ans.append(("(" + item + " : " + str(d.get(item)) + ")"))
        else:  
            ans.append(("(" + item + " : 0)"))
            
    jointAns = " - ".join(ans)
           
    return jointAns

        


#b = ['BBAR 150', 'CDXE 515', 'BKWR 250', 'BTSQ 890', 'DRTY 600']
#c = ['A', 'B', 'C', 'D']

b = []
c = ['B', 'R', 'D', 'X']

    
res = stock_list(b, c)
print (res)

#"(A : 200) - (B : 1140)"

'''




import operator

def calculate_winners(snapshot, penguins): 
    
    rem = []
    res = {} 
    spots = ["GOLD","SILVER","BRONZE"]
    
    swim = snapshot.replace("|","").split("\n")
    print(swim)
   
    
    for Penguin in swim:
        rem.append((Penguin[Penguin.index("p"):].count("-") + (Penguin[Penguin.index("p"):].count("~") * 2)))
    print (rem)
    res = dict(zip(penguins, rem))
    print(res)
    sortedRes = (sorted(res.items(), key=operator.itemgetter(1),reverse=False))
 
    
   
   
  

    return "GOLD: " + str(sortedRes[0][0]) + ", SILVER: " + str(sortedRes[1][0]) + ", BRONZE: " + str(sortedRes[2][0])
  
    
    
    
   







snapshot = """|-~~------------~--p-------|
|~~--~p------------~-------|
|--------~-p---------------|
|--------~-p----~~~--------|"""
penguins = ['Joline', 'Abigail', 'Jane', 'Gerry']


res = calculate_winners(snapshot, penguins)
print(res)

        #expected = "GOLD: Derek, SILVER: Francis, BRONZE: Bob"
        
        
        
        

        
        
        
        