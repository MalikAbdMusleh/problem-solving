#How to revers every internal content of the second string
def reverse_sec(string):
    #split the string into words
    string=string.split()
    #iterat over list
    output=[]
    i=0
    while i<len(string):
        #if the index is even the order is odd dont revers it
        if i%2==0:
            output.append(string[i])
        else:
            output.append(string[i][::-1])  
        i+=1   
    print(" ".join(output))
reverse_sec("one tow three four five")           


