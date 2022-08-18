def flatten(a, b):
    for x in a:
        if type(x) is list:
            flatten(x, b)
        else:
            b.append(x)
    return b
a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flattenList = []
flatten(a, flattenList)
print(flattenList)