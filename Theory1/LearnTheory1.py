


# public vs private
class Robot ():
    
    
    def __PrivateRobot (self):
        print ("I am Private Robot")
        
    
    def PublicRobot (self):
        print ("Calling Private Robot")
        self.__PrivateRobot ()
        print ("I am public Robot")
        
    
#bot = Robot()

#bot.__PrivateRobot()
#bot.PublicRobot()




#
text = "abcd"
#text = raw_input("Please insert your text here: ")
reverse = ""
for i in range(len(text)):
    reverse += text[-1*(i+1)]

    
print (reverse)
    