

a = 1   # let a be 1 让a为1
b = 2
c = a + b
print(c)

d = "你好，世界" # string 一串字符, character sequence
e = [1, 2, 3, 4, 5]    # average, mean 平均数 3
                       # medium 中位数

def average(list):
    return sum(list) / len(list)

# 求和
def get_sum(list):
    sum = 0
    for number in list:
        sum = sum + number
    return sum

# 求积
def get_product(list):
    product = 1         # identity number 
    for number in list:
        product = product * number
    return product


print(average(e), get_sum(e))
a = average(e)
b = get_sum(e)
print(a,b,a+b)


# print(get_product(e))
# # print(get_product(e))
# # print(120)
# # 120
# a = get_product(e)
# print(a)
# print(a+10)

# [10, 11]

# 声明新函数
#  def 函数名(参数列表):
#      函数体

# 使用函数
# 函数名(参数列表)

# print(average(e), get_sum(e))
# print(3, get_sum(e))
# print(3, 15)
# 3.0 15


# 某一年的一月一日是周x
# 1：  3
# 2：  4
# 3：  5
# 4：  6
# 5：  7
# 6：  1
# 7：  2
# 8：  3
# 10： 5
# 14： 2
# 20： 1
# 28： 2
# 92： 3

# 3 / 7 3除以7，7除3

# x [1-7]
def weekday(n, x):
    a = (n+(x-1))%7
    return a
    
        


    
        




# if 10 == 10:
#     whatever
#     xxx
#     xxxxx
#     xxx
#     xxx
# else:
#     whatever
#     xxx
#     xxxxx
#     xxx
#     xxx

# 余数

# 3 / 10 = 0 ... 3
# 10 / 3 = 3 ... 1




