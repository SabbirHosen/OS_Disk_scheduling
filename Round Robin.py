# Round Robin Scheduling

def gantt_generator(processes, qt):
    test =[]
    time = 0
    waiting_time = 0
    gantt_string = ''
    # print('from', processes)
    # print(processes[0][1])
    for x in processes:
        x.append(0)
        x.append(0)
    # print(processes)
    while len(processes) != 0:
        for x in processes[:]:
            # print('for', x[0])
            # print('be',processes)
            # print('w', waiting_time)
            # print('t', time)
            if x[1] >= qt:
                waiting_time += qt
                # print('if', x[0])
                gantt_string = gantt_string + str(time) + x[0]
                x[1] -= qt
                x[3] = x[3] + time - x[2]
                x[2] = waiting_time

                time += qt


            else:
                # print('else', x[0])
                waiting_time += x[1]
                gantt_string = gantt_string + str(time) + x[0]
                x[3] = x[3] + time - x[2]
                x[2] = waiting_time
                time += x[1]
                x[1] -= x[1]
                test.append(x)
                processes.remove(x)
            # print('af', processes)


    print(test)
    total = 0
    for x in test:
         total = total + x[3]

    gantt_string = gantt_string + str(time)
    # print('GANTT Chart String: ', gantt_string)
    # print('Average waiting Time: ', waiting_time/len(process))
    return gantt_string, total/len(test) # waiting_time / len(processes)


if __name__ == '__main__':
    number_of_process = int(input('Enter Number of Process(s): '))
    i = 1
    process = []
    while number_of_process > 0:
        temporary_input = input(f'Enter Process Name, Brust Time with space separated {i}:')
        temporary_list = temporary_input.split()
        if len(temporary_list) == 2:
            t = [temporary_list[0], int(temporary_list[1])]
            process.append(t)
            number_of_process -= 1
            i += 1
        else:
            print('Wrong format try again...')
    # process = [['p1', 21], ['p2', 3], ['p3', 6], ['p4', 2]]
    quantam = int(input("Enter Quantam Number: "))
    # print(process)
    # print(process[0][1])
    priority = gantt_generator(processes=process, qt=quantam)
    print('GANTT Chart String: ', priority[0])
    print('Average waiting Time: ', priority[1])

