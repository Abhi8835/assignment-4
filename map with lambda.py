lst = [85,47,65,95,22,88,11,77,4]
def cube(lst):
    return lst**2
data = list(map(cube,lst))
print(data)

data = list(map(lambda lst : lst**2,lst))
print (data)