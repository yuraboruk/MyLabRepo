





from csv import reader
from csv import DictReader

'''with open('Cars Available for Sale.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        print(row)'''
        
        
'''with open('Cars Available for Sale.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Check file as empty
    if header != None:
        # Iterate over each row after the header in the csv
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            print(row)'''
            

'''with open('Cars Available for Sale.csv', 'r') as read_obj:
    # pass the file object to DictReader() to get the DictReader object
    csv_dict_reader = DictReader(read_obj)
    # iterate over each line as a ordered dictionary
    for row in csv_dict_reader:
        # row variable is a dictionary that represents a row in csv
        print(row)'''
        
        

# iterate over each line as a ordered dictionary and print only few column by column name
'''with open('Cars Available for Sale.csv', 'r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    for row in csv_dict_reader:
        print(row['Brand'], row['Model'], row['Year'], row['Body Type'], row['Price'])'''
        

# iterate over each line as a ordered dictionary and print only few column by column Number
'''with open('Cars Available for Sale.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        print(row[0:1])
        
        
        
        
        
        
        
        
        
   
        
        
        
      
 '''     
       
cars = [["BMW", "X5", "$80,000"], ["BMW", "335i", "$60,000"],["Subaru", "STi", "$50,000"], ["Subaru", "XTR", "$45,000"]]

  
def showResult(funcText, i):
    global cars
    result = []
    locResult = ()
    
    if i == 1:
        k = len(cars)
    else: 
        k = len(result)
    for _ in range(k):
        if (i == 1):
            if (cars[_][0] == funcText):
                result.append(cars[_])
                locResult = cars[_]
    return result
        
      
textBrand = input("Which brand would you like to buy? ")       
locResult = showResult(textBrand, 1)   
print(locResult)  

        
     
        
      
'''
team = [["Mike", "M", 20], ["Jimmy", "M", 30], ["Lorry", "F", 33], ["Tiffany", "F", 43], ["Jack", "M", 23], ["Lucy", "F", 25]]
result = []

def showResult(funcText, i):
    global team
    global result
    locResult = []
    
    if i == 1:
        k = len(team)
    else:
        k = len(result)
    for _ in range(k):
        if (i == 1):
            if (team[_][i] == funcText):
                result.append(team[_])
                locResult.append(team[_])
        
    return locResult 

textSex = input("Do you want to list (M)ales or (F)emales: ")
locResult = showResult(textSex, 1)
print(locResult)
'''




                            