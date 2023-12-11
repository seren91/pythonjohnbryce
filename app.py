print('dcndc')


arr= [1,12,74,81,8,7,14]
def bigger(arr):    
    #global arr
    start=arr[0]
    for item in arr:
        if start<item:
            start=item
    print(start)
    
bigger(arr)








