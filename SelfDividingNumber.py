def selfDividingNumbers(self, left, right):
    L = []
    for self in range(left, right + 1):
        if check(self):
            L.append(self)
    return L
def check(n):
    t = n
    while (t != 0):
        if ((t % 10 == 0) or (n % (t % 10) != 0)):
            return False
        t = t // 10
    return True
print(selfDividingNumbers(0, 1, 22))
