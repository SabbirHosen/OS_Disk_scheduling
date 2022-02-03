queue = list(map(int, input('Enter request : ').split()))
header = int(input('Head Starting Positions : '))
queue.insert(0, header)
print('Path: ', ' '.join(list(map(str, queue))))
total = 0
calculation_string = ''
for i in range(0, len(queue)-1):
    if queue[i] >= queue[i+1]:
        total += queue[i] - queue[i+1]
        calculation_string = calculation_string + str(queue[i]) + '-' + str(queue[i+1])
    else:
        total += queue[i+1] - queue[i]
        calculation_string = calculation_string + str(queue[i+1]) + '-' + str(queue[i])
    if i+1 != len(queue):
        calculation_string += '+'
print('Calculation: ', calculation_string)
print('Total head movement {}'.format(total))
