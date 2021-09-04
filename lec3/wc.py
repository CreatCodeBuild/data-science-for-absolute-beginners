# # Input Output
# # IO

# # File IO

f = open('shakespear.txt')
content = f.read()
f.close()

# print(content) # string 字符串/文字
lines = content.split('\n')

total_number_of_lines = len(lines)
words_per_line = []
i = 0
while i < total_number_of_lines:
    words = lines[i].split(' ')
    words_per_line.extend(words)
    i += 1

print(words_per_line)

# print(lines)

# print(content.split(' '))
# a = 1
# a.split()
