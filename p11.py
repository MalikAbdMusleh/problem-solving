#write a program that find the number of occurence of each charachter present in the string
# aabbc =>
def count_charachter(string):
    l=[]
    for ch in string:
        if ch not in l:
            l.append(ch)
    for pr in l:
        print(f"{pr} occurecces {string.count(pr)} times.")        

# count_charachter("mmaalleekk")

#same but sorted
def count_charachter_s(string):
    l=[]
    for ch in string:
        if ch not in l:
            l.append(ch)
    for pr in sorted(l):
        print(f"{pr} occurecces {string.count(pr)} times.")        

# count_charachter_s("mmaaaleekkaa")

#same but with a set function and sorted

def count_charachter_o(string):
    l=set(string)
    for ch in sorted(l):
        print(f"{ch} occurecces {string.count(ch)} times.")        

count_charachter_o("mmaaaleekkaa")