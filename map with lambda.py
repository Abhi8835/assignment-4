lst = [2,4,8,5,7,1,2,3,6,9,7]
def cube(lst):
    return lst**3
data = list(map(cube,lst))
print(data)

data = list(map(lambda lst : lst**3,lst))
print (data)