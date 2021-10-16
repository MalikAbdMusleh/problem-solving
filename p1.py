#write a programe that reverse a string
#slice opereator
def reverse_str(string):
    output=string[::-1]
    #it mean slice from start to end and reverse it (-1) step
    #if step =1 the index will increase 1 ,-1 decrease 1
    print(output)

# reverse_str("malek") 

def reverse_stri():
    string=input("enter a string to reverse it")
    output=string[::-1]
    #it mean slice from start to end and reverse it (-1) step
    #if step =1 the index will increase 1 ,-1 decrease 1
    print(output)
# reverse_stri()  

def reversed_str(string):
    output=reversed(string) # return an reversed object
    output="".join(output) # join it 
    print(output)
reversed_str("malek")  