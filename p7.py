# write a function the repeat the alphabit the value of the number next to 
# a4b2=>aaaabb

def multi_alpha(string):
    #put the alhpa into a variable and repeate it the previos number of time
    output=""
    for ch in string:
        if ch.isalpha():
            x=ch
        else:
            output=output+x*int(ch)
    print(output)    

# multi_alpha("m2a3l1k2")      

# write a function that repeat the alphabit the value of the number next to and sort it 
# a4b2=>aaaabb
def multi_alpha_sorted(string):
    #put the alhpa into a variable and repeate it the previos number of time
    output=""
    for ch in string:
        if ch.isalpha():
            x=ch
        else:
            output=output+x*int(ch)
    output=sorted(output)        
    print("the targit string is : ","".join(output))    

multi_alpha_sorted("m2b3l1z2")       
        
