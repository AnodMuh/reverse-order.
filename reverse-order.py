def revers(aList):
    reversList=[]
    for i in range(len(aList)-1,-1,-1):
        reversList.append(aList[i])
    return reversList

aList=[2,3,3,5,2,4,7,8]
print(revers(aList))