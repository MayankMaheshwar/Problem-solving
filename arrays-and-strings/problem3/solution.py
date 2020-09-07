def checkSum(arr,total):
    dic={}  # used a dictionary
    
    for value in arr:
        remain=total-value
        dic[value]=remain
        if remain in dic:
            return True
    
    return False      


if __name__=="__main__":
    arr=list(map(int,input().split()))
    total=int(input())
    print(checkSum(arr,total))
  
# O(n)tc and O(n)sc  