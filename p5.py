#write a program that merge 2 string by taking charachters alternativly in even index and odd index


def merge(string1,string2):
    i,j=0,0
    output=""
    while i<len(string1)or j<len(string2):
        if j<len(string2):
            output=output+string2[i]
        i+=1
        if i<len(string1):
            output=output+string1[j]
        j+=1
    print("the result is",output)   


merge("malek","musleh engineer")     

