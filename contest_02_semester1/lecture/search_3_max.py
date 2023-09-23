
a = b = c = float('-inf')
item = input()

while item != '#':
    num = int(item)
    if num >= a:
        c = b
        b = a
        a = num
    elif num >= b:
        c = b
        b = num
    elif num >= c:
        c = num

    item = input()

print(c, b, a)
