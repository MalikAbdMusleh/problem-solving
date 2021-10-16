# Write a program that remove dublicate charachter in a string

#using not in and for loop
def remove_duplicate(string):
    output=""
    for ch in string:
        if ch not in output:
            output+=ch
    print(output)
# remove_duplicate("maalllliiiikkk") 
#using list and not in and for loop
def remove_duplicate_l(string):
    output=[]
    for ch in string: 
        if ch not in output:
            output.append(ch)
    print("".join(output))
    #test the function
# remove_duplicate_l("maalllliiiikkk") 
 
#using set function 
def remove_duplicate_S(string):
    #transmit the string into a set (object) using set function  
    output=set(string)
    #join the set into a string (the only problem is no garanty for the elements) random arrangment
    print("".join(output)) 

#test the function
remove_duplicate_S("maalllliiiikkk") 