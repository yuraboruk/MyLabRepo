from _ast import Or

# Populating a dictionary:

#1
d = {"Name":"Yura"}
#print(d)

#2
d["Age"] = 24
#print(d)

#3
t = (["Name", "Yura"], ["Age",24])
d = dict(t)
#print(d)

#or

d = dict([("Name", "Yura")])
#print(d)

#4  -  from two lists
names = ["Nick", "Alice", "Kitty"]
professions = ["Programmer", "Engineer", "Art Therapist"]

professions_dict = {}
for i in range(len(names)):
    professions_dict[names[i]] = professions[i]
#print(professions_dict)

#5  -  from two lists !!!!!*****
names_and_professions = dict(zip(names, professions))
#print(names_and_professions)

#6
names_and_professions = dict.fromkeys(names, professions)  #  -  will assign the entire Values to each of the keys
#print(names_and_professions)







#        disct.items()  -  returns all pairs in dict as tuples
#        dict.keys()  -  returns all keys in dict / dict.values()  -  as tuples


#        dict.pop(key)  -  retrieves a particular value and removes the element form dict


#        dict[key]  -  retrieves the value
#        dict.get(key)  -  retrieves the value


#        dictionary1.update(dictionary2)  -  If any key of the second dictionary matches with any key of the first dictionary then the corresponding value of the first dictionary will be updated by the corresponding value of the second dictionary

d1 = {"Name":"Yura"}
d2 = {"Name":"Boruk"}

d1.update(d2)
#print(d1)


#        sorted(dictionary)  -  sorts the key values only

#print(sorted(x))


#    sort by values

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
#print({k: v for k, v in sorted(x.items(), key=lambda item: item[1])}) #  -  item[0] for keys / item[1] for values

