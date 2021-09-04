d = {"key": 1, "key2": "2132", "key3": [213213, 324]}

# name: value pair

studentAge1 = {
    "张三": 15,
    "王五": 17,
    "李四": 16,
}
print(studentAge1)
studentAge1["李四"], studentAge1["张三"] = studentAge1["张三"], studentAge1["李四"]
print(studentAge1)
# studentAge1["王五"] = 17
# print("王五", studentAge1["王五"])
# print(studentAge1)
# del studentAge1["王五"]
# print(studentAge1)

# students = ["李四", "张三"]
# studentAges = [ 16, 15]

studentAge2 = [["李四", 16], ["张三", 15]]
studentAge2[0]

# a = 1
# b = 2
# c = a
# print(a, b)
# a = b
# b = c
# print(a, b)

# def swap(a, b):
#     temp = a
#     a = b
#     b = temp
#     return a, b

# a, b = swap(10, 20)
# print(a, b)

# a = 1
# b = 2
# print(a, b)
# a, b = b, a
# print(a, b)

# d = {}

# for i in range(1000000):
#     d[i] = i
# print(d)

# a = ["two", "one", "three"]
# def howBig(x):
#     if x == 'one':
#         x = 10
#     elif x == 'two':
#         x = 2
#     else:
#         x = 3
#     return x
# a.sort(key=howBig, reverse=True)
# print(a)



# def add(f1, f2):
#     return f1(1) + f2(2)

# def addOne(x):
#     return x + 1

# y = add(addOne, addOne)
# print(y)


# def sumIt(listCreator):
#     l = listCreator(3)
#     return sum(l)

# s = sumIt(range)
# # print(s)

# def add(x, y):
#     return x + y

# a = 1
# add(a, 2)

# d = {"a": -999, "b": []}
# x = sorted(d, reverse=True)
# print(x)    # ['b', 'a']
# y = {}
# for z in ['b', 'a']:
#     y[z] = d[z]
# print(y)

d = {"mike": 19, "jack": 18}
def howAge(person):
    return d[person]
x = sorted(d, key=howAge)
print(x)
y = {}
for z in x:
    y[z] = d[z]
print(y)

