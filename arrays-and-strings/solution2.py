stringList = input()
stringList = list(stringList)

def reverse(stringList,start,end):
    while start<end:
        stringList[start],stringList[end]=stringList[end],stringList[start]
        start+=1
        end-=1
    

reverse(stringList,0,len(stringList)-1)

currentIndex = 0
for i in range(len(stringList)+1):
    
    if (i==len(stringList)) or (stringList[i] == ' ') :
        reverse(stringList,currentIndex,i-1)
    
        currentIndex=i+1

print("".join(stringList))

# O(n)tc and O(1)sc