

def calculator(s):

    stack = []

    ret = 0
    cur = 0
    sign = 1
    for c in s:
        if(c.isdigit()):
            cur = 10*cur + int(c)
        elif(c != ' '):
            ret = ret + sign * cur
            cur = 0
            if(c == '('):
                stack.append(ret)
                stack.append(sign)
                ret = 0
                sign = 1
            elif(c == ')'):
                tmp_sign = stack.pop()
                tmp_ret = stack.pop()
                ret = tmp_ret + tmp_sign*ret
            elif(c == '+'):
                sign = 1
            elif(c == '-'):
                sign = -1

        else:
            continue
    ret = ret + sign * cur

    return ret


def simpleCal(s, start, end):

    ret = 0
    cur = 0
    sign = 1
    while (start <= end):
        if(s[start].isdigit()):
            cur = 10*cur + int(s[start])

        elif (s[start] != ' '):
            ret = ret + sign * cur
            cur = 0
            if(s[start] == '('):
                ret, start = simpleCal(s, start+1, end)
            elif(s[start] == ')'):
                return ret, start
            elif(s[start] == '+'):
                sign = 1
            elif(s[start] == '-'):
                sign = -1
        start += 1
    ret = ret + sign * cur
    return (ret, start)


input = '1+1'
print(simpleCal(input, 0, 2))



def withMultiplication(s, start, end):

    ret = 0
    cur = 0

    while(start <= end and s[start].isdigit()):
        cur = 10*cur+int(s[start])
        start+=1
        
    while(start <= end and s[start] == '*'):
        start+=1
        nextval = 0
        while(start <= end and s[start].isdigit()):
            nextval = 10*nextval+int(s[start])
            start+=1
            
        cur = cur * nextval

    
    if(start <= end and s[start] == '+'):
        cur = cur + withMultiplication(s, start+1, end)
    
    return cur

print(withMultiplication('1+2*3*3+1', 0, 8))
