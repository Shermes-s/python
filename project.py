# 1

l2 = []
def flatten(x):
    if isinstance(x,list):
        for y in x:
            if isinstance(y,list):
                flatten(y)
            else:
                l2.append(y)
    else:
        l2.append(x)
    return l2

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(l))

# 2

def reverser(x):
    if isinstance(x,list):
        x.reverse()
        for y in x:
            if isinstance(y,list):
                reverser(y)

l3 = [[1,2],[3,4],[5,6,7]]
reverser(l3)
print(l3)