# Write the function that return this #a4bb6 => aebf
#the number is replaced by the charachter after by the same number order

def displacement(string):
    output=""
    for ch in string:
        if ch.isalpha():
            output+=ch
            c=ch
        else:
            output=output +chr(ord(c)+int(ch))
    print("the replaced string is",output)    
displacement("m1a3l5a3")
        

