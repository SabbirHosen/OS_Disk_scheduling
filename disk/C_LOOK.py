queue = list(map(int, input('Enter request : ').split()))
header = int(input('Head Starting Positions : '))
lower_bound = int(input('Enter lower bound: '))
upper_bound = int(input('Enter upper bound: '))
u_queue = queue
u_queue.append(header)
u_queue.sort()

lower_queue = u_queue[: u_queue.index(header)]
upper_queue = u_queue[u_queue.index(header):]
lower_queue.insert(0, upper_queue[-1])
total = 0
calculating_string = ''
for i in range(0, len(upper_queue)-1):
    # print(i)
    total += abs(upper_queue[i] - upper_queue[i + 1])
    calculating_string = calculating_string + '|' + str(upper_queue[i]) + '-' + str(upper_queue[i + 1]) + '|' + '+'

for i in range(0, len(lower_queue)-1):
    total += abs(lower_queue[i] - lower_queue[i+1])
    if i == (len(lower_queue)-2):
        calculating_string = calculating_string + '|' + str(lower_queue[i]) + '-' + str(lower_queue[i + 1]) + '|'
    else:
        calculating_string = calculating_string + '|' + str(lower_queue[i]) + '-' + str(lower_queue[i+1]) + '|' + '+'
path = upper_queue + lower_queue[1:]
print('Path: ', ' '.join(list(map(str, path))))
print('Calculation: ', calculating_string)
print('Total head movement {}'.format(total))
