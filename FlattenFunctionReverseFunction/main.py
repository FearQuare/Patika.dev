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

def reverse(a, b):
    lenght = len(a) - 1
    while(lenght > -1):
        if type(a[lenght]) is list:
            b1 = []
            reverse(a[lenght], b1)
            b.append(b1)
        else:
            b.append(a[lenght])
        lenght -= 1
    return b
reverseList = []
b = [[1, 2], [3, 4], [5, 6, 7]]
reverse(b, reverseList)
print(reverseList)


