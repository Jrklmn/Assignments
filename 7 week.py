def chopped(t):
    del t[0::3]
    return None

Numbers = [1,2,3,4]
print("my list before call chop function =>",Numbers)
chopped(Numbers)
print("my list after call chop function =>",Numbers)


def middle(x):
    t = sorted(x)
    print("my list after calling middle function =>", t)
    return t[1:3:]


numbers = [1,2,3,4]
print("my list before calling middle function =>",numbers)
result = middle(numbers)
print("new list after calling middle function =>",result)