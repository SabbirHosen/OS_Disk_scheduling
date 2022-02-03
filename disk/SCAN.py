queue = list(map(int, input('Enter request : ').split()))
header = int(input('Head Starting Positions : '))
lower_bound = int(input('enter lower bound: '))
upper_bound = int(input('enter upper bound: '))

u_queue = queue
u_queue.append(header)
u_queue.append(lower_bound)
u_queue.append(upper_bound)
u_queue.sort()
# print('t', u_queue)

lower_queue = u_queue[: u_queue.index(header) + 1]
# lower_queue.append(header)
lower_queue.sort(reverse=True)
upper_queue = u_queue[u_queue.index(header) + 1: -1]
upper_queue.insert(0, lower_bound)
# print('l', lower_queue)
# print('u', upper_queue)
total = 0
calculating_string = ''
for i in range(0, len(lower_queue)-1):
    # print(i)
    total += abs(lower_queue[i] - lower_queue[i+1])
    calculating_string = calculating_string + '|' + str(lower_queue[i]) + '-' + str(lower_queue[i+1]) + '|' + '+'
for i in range(0, len(upper_queue)-1):
    # print(i)
    total += abs(upper_queue[i] - upper_queue[i + 1])
    if i == (len(upper_queue)-2):
        calculating_string = calculating_string + '|' + str(upper_queue[i]) + '-' + str(upper_queue[i + 1]) + '|'
    else:
        calculating_string = calculating_string + '|' + str(upper_queue[i]) + '-' + str(upper_queue[i + 1]) + '|' + '+'

path = lower_queue + upper_queue[1:]
print('Path: ', ' '.join(list(map(str, path))))
print('Calculation: ', calculating_string)
print('Total head movement {}'.format(total))