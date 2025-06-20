numMap={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}

def getcombo(digits):
    combos=['']
    if digits == "":
        return [""]
    for digit in digits:
        updatedcombo=[]
        for i in combos:
           for j in numMap[int(digit)]:
               updatedcombo.append(i+j)
        combos=updatedcombo            

    print(combos)


print(getcombo(""))


        

    