# write a function the repeat the alphabit the value of the number next to return the alpha then the repeatation of it
# aaaabb=>a4b2

def repeated_alpha(string):
    #put the chatachter in to variable
    #put the number of counted alphabet
    previos=string[0]
    output ="" 
    i=1
    c=1
    while i<len(string):
        if string[i]==previos:
            c+=1
        else:
            output=output+str(c)+previos
            previos=string[i]
            c=1
        if i==len(string)-1:
            output=output+str(c)+previos
        i+=1
    print("the finel result is : ",output)


repeated_alpha("aaacccbbbd")


