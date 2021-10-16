#write a program that inputs string with alphabit and digits and seperate the alphabit about the digits

def alpha_digits(string):
    numbers=[]
    alphabit=[]
    #sort the string in to a list
    string=sorted(string)
    #sperate the charachters into tow lists
    for ch in string:
        if ch.isalpha():
            alphabit.append(ch)
        else:
            numbers.append(ch)
    #  add the tow lists into one list        
    output=numbers+alphabit
    #join the out put into a string 
    print("the sepration is ","".join(output))
    #test the function
alpha_digits("ma1le2k3")
