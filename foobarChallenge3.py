
def sanitizeNegArr(arr):
    arr = sorted(arr)
    if len(arr)%2 == 1:
        arr.pop()
    return arr


xs = [-2]

if len(xs) == 1:
    return str(xs[0])
negArr = []
posArr = []
for num in xs:
    if num > 0:
        posArr.append(num)
    elif num < 0:
        negArr.append(num)

negArr = sanitizeNegArr(negArr)

if len(negArr) == 0 and len(posArr) == 0:
    print '0'
else:
    result = 1
    for num in posArr:
        result *= num
    for num in negArr:
        result *= num
    print str(result)

# xs = [2,0,2,2,0]

# greatestMin = 1 
# result = 1
# for num in xs:
#     if num != 0:

#         result *= num

#         if num < 0:
#             if greatestMin == 1:
#                 greatestMin = num
#             if num > greatestMin:
#                 greatestMin = num
# https://foobar.withgoogle.com/?eid=wJu34