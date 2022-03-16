import random
alphas = "0123456789abcdefghijklmnopqrstuvwxyz"

def key(length):
    chars = []
    for i in range(length):
        chars.append(alphas[random.randrange(len(alphas))])
    return "".join(chars)
alpha2 = ['0','1','2','3','4','5','6','7','8,','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def toNums(strin):
    res = []
    for char in strin:
        for i in alpha2:
            if char == i:
                res.append(str(alpha2.index(char)))
    return "".join(res)

def isVal(nums):
    if int(nums) % 6968 == 0:
        return True
    else:
        return False


def totalEval(strin):
    toNumd = toNums(strin)
    return isVal(toNumd)

while True:
    p = key(64)
    if totalEval(p):
        print("Valid key: " + p)
        break
