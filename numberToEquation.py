import calculator


def formula(num, start, acc, result):

    if(start == len(num)):
        
        val = calculator.withMultiplication(acc, 0, len(acc)-1)

        if(val in result):
            result[val].append(acc)
        else:
            result[val] = [acc]
        return

    formula(num, start+1, acc+num[start], result)
    if(acc[-1].isdigit()):
        formula(num, start, acc+'+', result)
        formula(num, start, acc+'-', result)
        formula(num, start, acc+'*', result)
        formula(num, start, acc+'/', result)

def helper(num):
    # print(num)
    result = {}
    formula(num, 1, num[0], result)
    # print(result)
    return result

def split(num):
    for i in range(1, len(num)):
        # print(num[0:i], num[i:len(num)])

        map1 = helper(num[0:i])
        map2 = helper(num[i:len(num)])

        for key,val in map2.items():

            if(key in map1):
                for left_formula in map1[key]:
                    for right_formula in val:
                        print(left_formula + '=' + right_formula)

split('2+3*2-3')
