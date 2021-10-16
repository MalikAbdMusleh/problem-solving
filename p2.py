#How to reverse a words in a string
#using split method
def reverse_words(string):
    #split the string
    string=string.split()
    reversed_string=string[::-1]
    #join the list in a string with spaces
    print(" ".join(reversed_string))

 #test the function
# reverse_words("how are you sir?")

def reverse_wordsi(string):
    #split the string
    string=string.split()
    output=[]
    #reverse each word
    for word in string:
        output.append(word[::-1])
    print(" ".join(output))    
 #test the function
reverse_wordsi("how are you sir?")  