def sub(x, y, base):
    carry = 0
    result = ''
    for i in range(len(x)-1 , -1, -1):
        a = int(x[i])
        b = int(y[i])
        c = 0
        if a >= b + carry:
            c = a - b - carry
            carry = 0
        else:
            c = a + base - b - carry
            carry = 1

        result = str(c) + result

    return result

n = '210022'
base = 3

cycle = {n:0}
acc = 0
while True:
    acc += 1
    x = ''.join(sorted(n, reverse=True))
    y = ''.join(sorted(n))
    n = sub(x, y, base)
    if n in cycle:
        break
    else:
        cycle[n] = acc 
        print n, acc


