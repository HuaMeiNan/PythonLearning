# --* coding:  utf-8 -*-

def findMinAndMax(l):
    s = []
    for i in l:
        s.append(i)

    return max(s),min(s),s

x = [1,2,3,4]
q = findMinAndMax(x)
print(q)