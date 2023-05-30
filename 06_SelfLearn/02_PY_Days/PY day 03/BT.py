def lesson_03_dict():
    dic = dict()
    x = int(input('enter number of elements: '))
    for i in range(1, x+1):
        dic[i] = i*i
    dic[2] = 8
    print(dic)


def lesson_04_tuple():
    x = int(input('enter number of elements: '))
    tup = tuple()
    li = list()
    for i in range(x):
        values = input('enter the elements: ')
        li.append(values)
        tup = tuple(li)
    print(tup)


lesson_04_tuple()
