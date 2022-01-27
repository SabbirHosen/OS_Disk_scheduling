# Priority Scheduling

def sorting_process(processes):
    return sorted(processes, key=lambda x: x[2])


def gantt_generator(processes):
    time = 0
    waiting_time = 0
    gantt_string = ''
    for x in processes:
        waiting_time += time
        gantt_string = gantt_string + str(time) + x[0]
        time += x[1]

    gantt_string = gantt_string + str(time)
    # print('GANTT Chart String: ', gantt_string)
    # print('Average waiting Time: ', waiting_time/len(process))
    return gantt_string, waiting_time / len(processes)


if __name__ == '__main__':
    number_of_process = int(input('Enter Number of Process(s): '))
    i = 1
    process = []
    while number_of_process > 0:
        temporary_input = input(f'Enter Process Name, Brust Time and Priority with space separated {i}:')
        temporary_list = temporary_input.split()
        if len(temporary_list) == 3:
            t = [temporary_list[0], int(temporary_list[1]), int(temporary_list[2])]
            process.append(t)
            number_of_process -= 1
            i += 1
        else:
            print('Wrong format try again...')
    # process = [['p1', 21, 2], ['p2', 3, 1], ['p3', 6, 4], ['p4', 2, 3]]
    print(process)
    ready_queue = sorting_process(processes=process)
    print(ready_queue)
    priority = gantt_generator(processes=ready_queue)
    print('GANTT Chart String: ', priority[0])
    print('Average waiting Time: ', priority[1])

