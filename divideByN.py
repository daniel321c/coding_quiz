
def divideByN(n):

    start = 10

    prev = {}

    counter = 0

    residue = ""

    while(start > 0):

        quotient = int(start/n)
        start = (start % n)*10

        residue = residue + str(quotient)

        if(start not in prev):
            prev[start] = counter
            counter += 1
        else:
            break

    return residue[prev[start]:counter]


print(divideByN(33))
print(1/333)