list1=[1,1,2,2,[4,5,6,4,4,3],[2,8,9,6,6,7],2,1,6,8]



countdict={}



for i in list1:
    if type(i)==list:
       for j in i:
           if j in countdict:
               countdict[j]=countdict[j]+1
           else:
               countdict[j]=1         
    else:
        if i in countdict:
            countdict[i]=countdict[i]+1
        else:
            countdict[i]=1    




print("Occurences of each values :", " ",countdict)        






