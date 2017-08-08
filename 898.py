# # from numpy import np
#
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6]])
# # c = np.concatenate((a, b), axis=0)
# # print(c)


def bubbleSort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

list = [54,26,93,17,77,31,44,55,20]
print(set(list))
bubbleSort(list)
print(list)


x = {"a":"1","b":"4","c":"2"}
y = sorted(x.keys(), key =x.values())
print(y)