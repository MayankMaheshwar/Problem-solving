def indexes(arr,target):
    if target<min(arr):
        return -1
    elif target==sum(arr):
        return tuple(range(0,len(arr))) 
    elif any(arr[i]==target for i in range(len(arr))):
        return arr.index(target)
    else:
        dic={}
        for i in range(1,len(arr)):





if __name__=="__main__":
    arr=list(map(int,input().split()))
    target=int(input())
    print(indexes(arr,target))
  