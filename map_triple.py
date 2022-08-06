lst = [2,4,8,5,7,1,2,3,6,9,7]
def triple(lst):
    return lst*3
data = list(map(triple,lst))
print(data)

data = list(map(lambda lst : lst*3,lst))
print (data)