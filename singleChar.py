# import queue
input = "aabbc"


def singleChar(s):
    i = 0
    for ch in s:
        i = i ^ ord(ch)
    return chr(i)


print(singleChar(input))
