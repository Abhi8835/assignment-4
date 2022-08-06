lst = [2,4,8,5,7,1,2,3,6,9,7]
def square(lst):
    return lst**2
data = list(map(square,lst))
print(data)

data = list(map(lambda lst : lst**2,lst))
print (data)