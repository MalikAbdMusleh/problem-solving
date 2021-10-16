#write a program to print charachters at even and odd index seperately
def string_chr(string):
    i=0
    #write the charachters present at even index 
    print("the even charachter index present :")
    while i<len(string):
        print(string[i])
        i+=2
    #write the charachters present at odd index 
    print("the odd charachter index present :")    
    i=1
    while i<len(string):
        print(string[i])
        i+=2
# string_chr("malek")               

#write a program to print charachters at even and odd index seperately 
#with slice operator
def string_chr_S(string):
    i=0
    #write the charachters present at even index 
    print("the even charachter index present :",string[0::2])
    #write the charachters present at odd index 
    print("the odd charachter index present :",string[1::2])
#test the function     
string_chr_S("malek")    
