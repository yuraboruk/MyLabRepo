
class Node:

    def __init__(self, data, level):

        self.left = None
        self.right = None
        self.data = data
        self.level = level
        self.maxlevel = 1

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data, self.level + 1)
                    if self.maxlevel < self.level + 1:
                        self.maxlevel = self.level + 1
                       
                else:
                    templevel = self.left.insert(data)
                    if self.maxlevel < templevel:
                        self.maxlevel = templevel
                    
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data, self.level+1)
                    if self.maxlevel < self.level+1:
                        self.maxlevel = self.level+1
                       
                else:
                    self.right.insert(data)
                    if self.maxlevel < templevel:
                        self.maxlevel = templevel
                        
        else:
            self.data = data
            
        return self.maxlevel


# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
            




numLevels = 1
tempLevel = 1


def maxOfTwo(tempLevel):
    global numLevels
    if numLevels < tempLevel:
        numLevels = tempLevel


# Use the insert method to add nodes
root = Node(12, 1)
tempLevel = root.insert(6)


maxOfTwo(tempLevel)

tempLevel = root.insert(14)
maxOfTwo(tempLevel)

tempLevel = root.insert(3)
maxOfTwo(tempLevel)

tempLevel = root.insert(1)
maxOfTwo(tempLevel)


root.PrintTree()

print ("Num Level = " + str(numLevels))

print (str(2**numLevels))

print (str(root.maxlevel))