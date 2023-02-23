def a(s):
    d={"u":0,"l":0}
    for c in s:
        if c.isupper():
            d["u"]+=1
        elif c.islower():
            d["l"]+=1
        else:
            pass
    print('no. of upper case characters: ',d["u"])
    print('no. of lower case characters: ',d["l"]) 
a('The quick Brow Fox')