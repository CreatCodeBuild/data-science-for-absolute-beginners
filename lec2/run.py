from a import function

function()  # 函数名()  执行这个函数

# i = 0
# while i < 10:
#     print("将要删除一个文件: y")
#     x = input()
#     print("you typed", x)
#     i += 1

def average(list):
    return sum(list) / len(list)    # /

# 变量名 = 运行某个函数的结果或者数值或者其他变量

# l = []
# i = 0
# while i < 5:
#     x = input()
#     l.append(int(x))    # integer
#     i +=  1              # i = i+1

# print(l)
# avg = average(l)
# print("平均数是：", avg)

# row = ['*','*','*','*','*','*','*','*','*','*']
# game_map = []
# i = 0
# while i < 10:
#     game_map.append(row)
#     i += 1

game_map = [
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '@', '*', '*', '*', '*', '*', '*', '*'], 
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], 
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], 
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], 
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], 
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], 
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], 
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], 
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]

def show_map():
    for each_row in game_map:       # for each_element in container:
                                    #    do something
        print(each_row)


def move_left(pos_x, pos_y):
    if pos_y == 0:
        return pos_x,pos_y
       
    game_map[pos_x][pos_y-1] = "@"
    game_map[pos_x][pos_y] = "*"
    return pos_x, pos_y-1

def move_right(pos_x, pos_y):
    if pos_y == 9:
        return pos_x,pos_y
       
    game_map[pos_x][pos_y+1] = "@"
    game_map[pos_x][pos_y] = "*"
    return pos_x, pos_y+1

def move_up(pos_x, pos_y):
    if pos_x == 0:
        return pos_x,pos_y
       
    game_map[pos_x-1][pos_y] = "@"
    game_map[pos_x][pos_y] = "*"
    return pos_x-1, pos_y

def move_down(pos_x, pos_y):
    if pos_x == 9:
        return pos_x,pos_y
       
    game_map[pos_x+1][pos_y] = "@"
    game_map[pos_x][pos_y] = "*"
    return pos_x+1, pos_y
# move_left(1,2)
# show_map()

pos_x = 1
pos_y = 2
while True:
    show_map()
    direction = input()
    if direction == "a": 
        pos_x, pos_y = move_left(pos_x, pos_y)
    if direction == "d":
        pos_x, pos_y = move_right(pos_x, pos_y)

    if direction == "w": 
        pos_x, pos_y = move_up(pos_x, pos_y)
    if direction == "s":
        pos_x, pos_y = move_down(pos_x, pos_y)

