
from rejson import Client, Path
import json
import redis
import os




p = redis.Redis()
l = redis.Redis()

#p.set("Defender", '{ "name":"Mykolenko", "age":21, "nationality":"Ukrainian"}')
#l.set("Ukrainian", "[Mykolenko, Tsygancov]")
#l.append("Ukrainian", "Tsygancov")



#print(l.get ("Defender"))





#rpush



x = "{ name: Mykolenko, age: 21, nationality: Ukrainian}"
z = {"name": "Popov","age": "21","nationality": "Ukrainian"}


#y = json.dumps(x)




#p.set("Defender", y)
#print(p.get("Defender"))






#p.hset("Defender", "21" , "Mykolenko")

#print (p.hget("Defender"))



#.hmset("RedisKey", Defenders)

dyn = redis.Redis()

#str = input("Enter something...")

#dyn.set("Test1", x)
dyn.jsondocset ("Test2", z)

str = dyn.get("Test2")

print (str)

'''
Defenders = {"Name":"Mykolenko", "Age":"21", "Nationality":"Ukrainian", "Name":"Popov",
  "Age":"21", "Nationality":"Ukrainian"}
dyn.hmset("pythonDict", Defenders)
print(dyn.hgetall("pythonDict"))




'''