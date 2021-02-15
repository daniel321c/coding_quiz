import sys


def twoSumClosest(arr1, arr2, target):

    arr1 = sorted(arr1, key=lambda x: x[1])
    arr2 = sorted(arr2, key=lambda x: x[1])

    prt1 = 0
    prt2 = len(arr2)-1

    min_offset = sys.maxsize
    result = []

    while(prt1 < len(arr1) and prt2 > -1):

        sum = arr1[prt1][1]+arr2[prt2][1]

        if(abs(sum - target) < min_offset):
            result = [[arr1[prt1][0], arr2[prt2][0]]]
            min_offset = abs(sum - target)
        elif(abs(sum - target) == min_offset):
            result.append([arr1[prt1][0], arr2[prt2][0]])

        if(sum - target >= 0):
            prt2 -= 1
        else:
            prt1 += 1

    print(result)


# twoSumClosest([[1, 8], [3, 9], [2, 15]], [[1, 8], [2, 11], [3, 12]], 18)


import sys
def optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList):
    # WRITE YOUR CODE HERE
    
    
    forwardRouteList = sorted(forwardRouteList, key = lambda x:x[1])
    returnRouteList = sorted(returnRouteList, key = lambda x:x[1])
    
    ptr1 = 0
    ptr2 = len(returnRouteList)-1
    
    maxDis = -sys.maxsize -1
    result = []
    while(ptr1 <len(forwardRouteList) and ptr2 > -1):
        
        sum = forwardRouteList[ptr1][1] +returnRouteList[ptr2][1]
        
        if(sum > maxTravelDist):
            ptr2 -=1
        else:
            ptr1_end = ptr1
            ptr2_start = ptr2

            while(ptr1_end< len(forwardRouteList) and forwardRouteList[ptr1_end][1]== forwardRouteList[ptr1][1]):
                ptr1_end+=1
                
            
            while(ptr2_start> -1 and returnRouteList[ptr2_start][1]== returnRouteList[ptr2][1]):
                ptr2_start-=1

            if(sum >maxDis):
                maxDis = sum
                result = genPairs(ptr1, ptr1_end-1, ptr2_start+1, ptr2)
            elif(sum == maxDis):
                result = result + genPairs(ptr1, ptr1_end-1, ptr2_start+1, ptr2)
            
            ptr1 = ptr1_end

    print(result)
    return result

def genPairs(x_start, x_end, y_start, y_end):
    result = []
    for x in range(x_start, x_end+1):
        for y in range(y_start, y_end+1):
            result.append([x, y])
    
    return result
            

optimalUtilization(20, [[1, 8], [2, 7], [3, 14]], 
[[1, 5], [2, 10], [3, 14]])




