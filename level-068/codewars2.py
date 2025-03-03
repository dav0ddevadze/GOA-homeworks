def summation(num):
    numb=[0]
    for i in range(1,num+1):
        numb.append(i)
    return sum(numb)
print(summation(1))