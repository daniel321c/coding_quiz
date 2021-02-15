def nSum (arr, target, n, start, accSum, accArr, result):
    
    if(n == 0):
        if(accSum == target):
            result.append(accArr)
        return
    
    if(start >=len(arr)):
        return
    for i in range(start, len(arr)):
        new_acc = accSum + arr[i]
        new_arr = accArr.copy()
        new_arr.append(arr[i])
        nSum(arr, target, n-1,  i+1, new_acc, new_arr, result)


def nSum_helper(arr, target, n):
    result =[]
    nSum(arr, target, n, 0, 0, [], result)
    print(result)

nSum_helper([1,2,3,4,5,6,7, 8,9], 11, 3)