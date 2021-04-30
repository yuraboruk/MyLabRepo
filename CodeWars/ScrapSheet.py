

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
        
        
        

def switcheroo(string):
    
    for i in string:
        if i == "a":
            return string.replace("a","b").replace()
            
        

    


res = switcheroo("abc")
print (res)
#"bac")
#test.assert_equals(switcheroo('aaabcccbaaa'), 'bbbacccabbb') 




def spin_words(sentence):

    return " ".join(i[::-1] if len(i) >= 5 else i for i in sentence.split())
    
   




res = spin_words("Welcome")
print(res)




def dig_pow(n, p):
    
    sum = counter = 0
    num = str(n)
    
    for i in num:
        sum += int(i)**(p+counter)
        counter += 1
    return (int(sum/n) if not sum%n else -1)
    
    
    
res = dig_pow(89, 1)
print(str(res))
        
        
        





def play_pass(s, n):
    
    
    newString = ""
    counter = 0
    s = s.lower()
    
    for i in s:
        index = 0
        if i.isdigit():
            newString += str(9 - int(i))
        elif i.isalpha():
            if (ord(i) + n) > ord("z"):
                index = ord(i) + n - ord("z") + 96
            else:
                index = ord(i) + n                
            if counter % 2 == 0:
                newString += chr(index).upper()
            else:
                newString += chr(index)
        else:
            newString += i
        counter += 1
    
    return newString[::-1]
    
     
        
       
    
    
    
    
res = play_pass("I LOVE YOU!!!", 1)
print (res)

res = play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2)
print (res)
    
    
    



def find_outlier(integers):
    
    odd = []
    even = []
     
    for x in integers:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)

            
    if len(odd) > len(even):
        return (int(even[0]))
    else:
        return (int(odd[0]))





res = find_outlier([2])
print (res)
res = find_outlier([160, 3, 1719, 19, 11, 13, -21])
print (res)




def persistence(n):
    
    whileBool = False
    res = 1
    counter = 0
    str1 = str(n)
    
    if n < 10:
        return 0
    
    while not whileBool:
        
        for x in str1:
            res = res * int(x)
        
        if res > 10:
            str1 = str(res)
            counter += 1
            res = 1
            
        else:
            counter += 1
            whileBool = True
           
            
    return counter
    
  
    
def is_valid_walk(walk):
    
    if len(walk) != 10:
        return False
    
    if walk.count("n") == walk.count("s") and walk.count("e") == walk.count("w"):
        return True
    
    
    
    
    
    
    

res = is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])
print(res)
res = is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])
print(res)
#test.expect(not is_valid_walk(['w']), 'should return False');
#test.expect(not is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), 'should return False');

    


 
 
 
def likes(names):
    
    
    
    if len(names) == 0:
        return "no one likes this"
    
    if len(names) == 1:
        return "{} likes this".format(names[0])
    
    if len(names) == 2:
        return "{} and {} like this".format(names[0], names[1])
    
    if len(names) == 3:
        return "{}, {} and {} like this".format(names[0], names[1], names[2])
    
    if len(names) >= 4:
        return "{}, {} and {} others like this".format(names[0], names[1], len(names) - 2)
        
    
        





res = likes([])
print(res)
res = likes(['Peter'])
print(res)
res = likes(['Jacob', 'Alex'])
print(res)
res = likes(['Max', 'John', 'Mark'])
print(res)
res = likes(['Alex', 'Jacob', 'Mark', 'Max'])
print(res)





def order(sentence):
    
    counter = 0
    l = sentence.split()
    d = {}
    
    for item in sentence:
        if item.isdigit():
            d[int(item)] = l[counter]
            counter += 1
    
    
    return " ".join(d[i+1] for i in range(len(l)))
        
 
  
res = order("is2 Thi1s T4est 3a")
print (res)
#res = order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
#res = order(""), "")






def flap_display(lines, rotors):
    
    ans = []
    l =[]
  
    order = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789"
    
    lenOrder = len(order)
    print (order.index("B")+1)
    
    
    for x in range(len(lines)):
        l.clear()
        l = [order.index(y) for y in lines[x]]
        lenL = len(l)
        for flap in range(len(rotors[x])): 
            for item in range(flap, lenL):
                if l[item] + rotors[x][flap] >= lenOrder:
                    l[item] = (l[item] + rotors[x][flap])%lenOrder
                    
                else:    
                    l[item] = l[item] + rotors[x][flap] 
        print(l)
        
        ans.append("".join(order[i] for i in l))
    
    
    
    return ans

    
    
    
        
       
       
        

    
    
    
   
    
res = flap_display(["CODE"],[[20,20,28,0]])
print(res)





def flat_rotors(before, after):
    
    order = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789"
 

    
    for item in range(len(before)):
        
        
        b = [order.index(y) for y in before[item]] 
        a = [order.index(y) for y in after[item]] 
        newList = [0 for y in range(len(after[item]))]
    print (b)
    print (a)
        
        #for i in range(len(before[item])):
            #for y in range(i, len(after[item])):
               
                #newList[y] = abs(b[i] - a[y])
                #print(newList)
                
            


res = flat_rotors(["HELLO "], ["WORLD!"])
print(res)
#rotors = [[15,49,50,48,43,13]]




def flat_rotors(before, after):

    order = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789"
    l = len(order)
    finList = []
    
    if (len(before) or len(after) == 0) or before is None or after is None:
        return "x"
        
        
    for i in range(len(before)):
     
  
        begIndex = [order.index(y) for y in before[i]] 
        endIndex = [order.index(y) for y in after[i]] 
        
        newList = [0 for y in range(len(begIndex))]
        
        for b in range(len(begIndex)):

            
            sumList = sum(newList[0:b])
            
            if begIndex[b] + sum(newList[0:b]) > endIndex[b]:
                resNum = l-(sum(newList[0:b]) + begIndex[b])%l + endIndex[b]
                if resNum >= l:
                    resNum = resNum - l
                
            else: 
                resNum = endIndex[b] - (begIndex[b] + sum(newList[0:b]))
                              
            for e in range(b, len(endIndex)):
        
                newList[e] = resNum
    
        finList.append(newList)
        
    return finList    
    

    
res = flat_rotors("",["DOG"])
print (res)  
    
    
    

    
    
    
    
print(' * \n* *')
print('   *   \n  * *  \n *   * \n* * * *')
print("       *       \n      * *      \n     *   *     \n    * * * *    \n   *       *   \n  * *     * *  \n *   *   *   * \n* * * * * * * *")
    



newList = []
    for i in str(n):
        newList.append(int(i))


    
    for i in newList:
        if len(newList[i]) >= 2:
            ans = sum(newList)
    
    return ans


def digital_root(n):
    
    
    
    while n >= 10:
        
        newString = str(n)
    
        n = sum(int(i) for i in newString)
              
    return n
        
    
    
    




#newList = list(map(lambda x: x+1, a))



res = digital_root(16)
print(res)
res = digital_root(942)
print(res)
#Test.assert_equals(digital_root(132189)
#Test.assert_equals(digital_root(493193)




def zero(): #your code here
def one(): #your code here
def two(): #your code here
def three(): #your code here
def four(): #your code here
def five(): #your code here
def six(): #your code here
def seven(): #your code here
def eight(): #your code here
def nine(): #your code here

def plus(): #your code here
def minus(): #your code here
def times(): #your code here
def divided_by(): #your code here
    
    
    
    


res = seven(times(five()))
print (res)
res = four(plus(nine()))
print (res)
#eight(minus(three())), 5)
#six(divided_by(two())), 3)






def run(tricks):
    
    counter = 0
    
    for i in tricks:
        sum = (i['probability'])*(i['points']*i['mult_base']**counter)
        print (sum)
        counter += 1
        (i['probability'])*()
        
        while ((i['probability'])*(i['points']*i['mult_base']**counter))+sum > sum:
            
        
        
    






# Maximum expected score: 154.096245
res = run([{ 'name': 'kickflip', 'points': 100, 'mult_base': .8, 'probability': .85 }],)
#{ 'kickflip': 4, });
print(res)


# Maximum expected score: 276.058476...
#test.assert_equals(run([{ 'name': 'kickflip', 'points': 100, 'mult_base': .8, 'probability': .95 },
                        #{ 'name': 'impossible', 'points': 500, 'mult_base': .99, 'probability': .1 },]),
#{ 'kickflip': 8, });                   
                   
# Maximum expected score: 643.503147...
#test.assert_equals(run([{ 'name': 'kickflip', 'points': 100, 'mult_base': .8, 'probability': .95 },
                        #{ 'name': 'pop shove it', 'points': 50, 'mult_base': .75, 'probability': .995 },
                        #{ 'name': '360 flip', 'points': 250, 'mult_base': .825, 'probability': .9 },]),
#{ 'kickflip': 3, 'pop shove it': 8, '360 flip': 4, });

                   
                   
#point value * multiplier base^number of times already performed



(1) s'(t) = -b * s(t) * i(t)
(2) i'(t) =  b * s(t) * i(t) - a * i(t)
(3) r'(t) =  a * i(t)


(I)    S[k+1] = S[k] - dt * b * S[k] * I[k]
(II)   I[k+1] = I[k] + dt * (b * S[k] * I[k] - a * I[k])
(III)  R[k+1] = R[k] + dt * I[k] *a





def epidemic(tm, n, s0, i0, b, a):
    
    dt = tm/n
    i = i0

    for day in range(n):
        
        s1 = s0 - dt * b * s0 * i0
        i1 = i0 + dt * (b * s0 * i0 - a * i0)
        
        if i1 > i0:
            i = i1
        
        s0 = s1
        i0 = i1
        
        
    return int(i)




tm = 18 ;n = 432 ;s0 = 1004 ;i0 = 1 ;b = 0.00209 ;a = 0.51

res = epidemic(tm, n, s0, i0, b, a)
print (res)







def duplicate_encode(word):
    
    res = ""
    
    for i in word.lower():
        if word.lower().count(i) > 1:
            res += ")"
        else:
            res += "("
    return res

    
    
    return "".join(")" if word.lower().count(i) > 1 else "(" for i in word.lower())







res = duplicate_encode("din")
#"((("
print (res)
res = duplicate_encode("rEcede")
#"()()()"
print (res)





def count_bits(n):

    return bin(n).count("1")





res = count_bits(0)
print(res)
res=count_bits(4)
print(res)




def tribonacci(signature, n):
    
    for i in range(n-3):
        signature.append(sum(signature[-3::]))
    return signature[:n]
    
        
        
    
res = tribonacci([1, 1, 1], 1) 
print(res)
#[1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
res = tribonacci([0, 0, 1], 10)
print(res)
#[0, 0, 1, 1, 2, 4, 7, 13, 24, 44])




def song_decoder(song):
    
           
    #song = [i for i in song.split("WUB") if i != ""]
    
    return " ".join([i for i in song.split("WUB") if i != ""])
        
    


res = song_decoder("AWUBWUBWUBBWUBWUBWUBC")
print(res)
#Test.assert_equals(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C","multiples WUB should be replaced by only 1 space")
#Test.assert_equals(song_decoder("WUBAWUBBWUBCWUB"), "A B C","heading or trailing spaces should be removed")
    



def find_even_index(arr):
    
    
    for i in range(len(arr)):

        
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
        
    return -1




res = find_even_index([1,2,3,4,5,6])
print(res)
#3
res= find_even_index([1,100,50,-51,1,1])
print(res)
#1





def iq_test(numbers):
    
    even = []
    odd = []
    res = numbers.split(" ")
    
    for i in res:
        
        if int(i) % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
        
        if len(even) > 1 and len(odd) != 0:
            return res.index(odd[0])+1
        
        elif len(odd) > 1 and len(even) != 0:
            return res.index(even[0])+1
            
    return 0

            
            
    
    




res = iq_test("2 4 7 8 10")
print(res)
res = iq_test("1 2 2")
print(res)





def tickets(people):
    
    twentyFive = 0
    fifty = 0
    
    for i in people:
        
        if i == 25:
            twentyFive += 1
        
        if i == 50:
            if twentyFive == 0: return "NO"
            fifty += 1
            twentyFive -=1
        
        if i == 100:
            if twentyFive == 0 or (fifty == 0 and twentyFive < 3):
                if fifty > 0:
                    fifty -= 1
                    twentyFive -=1
                else:
                    twentyFive -= 3
    return "YES"
                
    
    
        
            
        
        



res = tickets([25, 25, 50])
print(res)
res = tickets([25, 100])
print(res)




def unique_in_order(iterable):
    
    res = []
    before = ""
    
    for i in iterable:
        if i != before:
            res.append(i)
            before = i
    return res
            
            



res = unique_in_order([1,2,2,3,3])
print(res)
                   
#['A','B','C','D','A','B'])



def beggars(values, n):
   
   
    return [sum(values[i::n]) for i in range(n)]
    

res = beggars([1,2,3,4,5],1)
print(res)
#[15])
res = beggars([1,2,3,4,5],2)
print(res)
#[9,6])
res = beggars([1,2,3,4,5],3)
print(res)
#[5,7,3])
    



def high(x):


    top = winner = 0
    result = ""
    
    
    for word in x.split(" "):
        top = 0
        for letter in word:
            top += (ord(letter) - 96)
        
    
        if top > winner:
            winner = top
            result = word
            
    return result
         
            
            
  return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
    

    



res = high('man i need a taxi up to ubud')
print(res)
# 'taxi')
res = high('what time are we climbing up the volcano')
print(res)
#'volcano')
res = high('take me to semynak')
print(res)





def valid_parentheses(string):
    
    counter = 0
    
    if len(string) < 1:
        return True
    
    
    for i in string[::-1]:
        
        if i == ")":
            counter += 1
        
        elif i == "(":
            if counter > 0:
                counter -= 1
            else:
                return False
            
    return (True if counter == 0 else False)
        
        
        
        
    
    
    
    
    
res = valid_parentheses("  (")
print(res)
#False)
res = valid_parentheses(")test")
print(res)
#False)
res = valid_parentheses("")
print(res)
#True)
res = valid_parentheses("hi())(") 
print(res)                
#False)
res = valid_parentheses("hi(hi)()")   
print(res)                
#True)
# 'semynak')






l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]



def sum_pairs(ints, s):
    
    for i in range(len(ints)):
        y = s-ints[i]
        
        if y in ints[:i]:
            return [ints[i],y]
    
    return None
    
            
        
    
    
       
           
   
    

res = sum_pairs([1, 4, 8, 7, 3, 15], 8)
print(res)
#== [1, 7], "Basic: %s should return [1, 7] for sum = 8" % l1)
res = sum_pairs(l2, -6)
print(res)
#== [0, -6], "Negatives: %s should return [0, -6] for sum = -6" % l2)
res = sum_pairs(l3, -7) 
print(res)
#== None, "No Match: %s should return None for sum = -7" % l3)
res = sum_pairs(l4, 2)
# == [1, 1]
print(res)
res = sum_pairs(l5, 10)
print(res)
# == [3, 7], "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5)
res = sum_pairs(l6, 8)
print(res)
# == [4, 4], "Duplicates: %s should return [4, 4] for sum = 8" % l6)
res = sum_pairs(l7, 0)
print(res)
# == [0, 0], "Zeroes: %s should return [0, 0] for sum = 0" % l7)
res = sum_pairs(l8, 10)
print(res) 
#== [13, -3], "Subtraction: %s should return [13, -3] for sum = 10" % l8)




def make_readable(seconds):
    h = int(seconds/3600)
    m = int((seconds-h*3600)/60)
    s = int(seconds-(h*3600)-(m*60))
    print(str(seconds% 60))
    #return "{:02d}:{:02d}:{:02d}".format(h,m,s)


    
    
    
    
res = make_readable(0)
print(res)
#"00:00:00")
res = make_readable(5)
print(res)
#"00:00:05")
res = make_readable(86399)
print(res)
#"23:59:59")
res = make_readable(359999)
print(res)
#"99:59:59")

'''


def order_weight(strng):
    
    num = []
    res = []
    summ = 0

   
    
    
    if len(strng) == 0:
        return ""
    
    num = strng.split(" ")
    
    for number in num:
        summ = 0
        for i in number:
            summ += int(i)
            
        
        
        res.append((summ,number))
        
    res.sort()   
    return " ".join(i[1] for i in res)





    
    
    
res = order_weight("103 123 4444 99 2000")
print(res)

#"2000 103 123 4444 99")
res = order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")
print(res)
# "11 11 2000 10003 22 123 1234000 44444444 9999")
res = order_weight("")
print(res)


