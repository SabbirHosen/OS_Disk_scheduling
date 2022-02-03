queue = list(map(int, input('Enter request : ').split()))
header = int(input('Head Starting Positions : '))

path = [header]
total = 0
calculating_string = ''
queue.append(header)
while len(queue) > 1:
    queue.remove(header)
    minimum = float('inf')
    for i in queue:
        if minimum > abs(header - i):
            minimum = abs(header - i)
            temp = i
    calculating_string = calculating_string + '|' + str(header) + '-' + str(temp) + '|'
    total += abs(header - temp)
    header = temp

    path.append(temp)
    if len(queue) != 1 and len(queue) != 0:
        calculating_string += '+'
    else:
        path.append(queue[0])

print('Path: ', ' '.join(list(map(str, path[:-1]))))
print('Calculation: ', calculating_string)
print('Total head movement {}'.format(total))