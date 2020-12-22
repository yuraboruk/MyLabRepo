#



#text = "abcd"
text = input("Please insert your text here: ")
reverse = ""
for i in range(len(text)):
    reverse += text[len(text)-1-i]

    
print (reverse)
    