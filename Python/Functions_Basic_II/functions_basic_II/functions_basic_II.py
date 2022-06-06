#countdown
def countdown(num):
    output = []
    for x in range(num, -1, -1):
        output.append(x)
    return output
print(countdown(5))

#print and return
def print_return(list):
    print(list[0])
    return list[1]
print(print_return([1,4]))

#first plus length
def fancy_function(list):
    return list[0] + len(list)
print(fancy_function([8, 2, 3, 4, 5]))

#values greater than second
def sassy_function(list):
    if len(list) < 2:
        return False
    output = []
    for x in range(0, len(list)):
        if list[x] > list[1]:
            output.append(list[x])
    print(len(output))
    return output
print(sassy_function([5, 2, 3, 2, 1, 4]))
print(sassy_function([3]))

#this length, that value
def dazzle_function(size, value):
    output = []
    for x in range(0, size):
        output.append(value)
    return output
print(dazzle_function(4, 7))
print(dazzle_function(6, 2))