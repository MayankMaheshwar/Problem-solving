inputArr = list(map(int,input().split()))

#first approach with O(n**2)tc and O(1)sc

"""
i=0
while len(inputArr) > i:
    if inputArr[i]%2 == 0:
        inputArr.insert(i+1,inputArr[i])
        i+=1
    i+=1

print(inputArr)        
"""

#second approach with O(n)tc and O(n)sc 

"""

from collections import  deque
deq = deque(inputArr)
result = []
while len(deq)>0:
    cur = deq.popleft()
    print(cur)
    if cur%2==0:
        result.append(cur)
    result.append(cur)
print(result)       

"""






