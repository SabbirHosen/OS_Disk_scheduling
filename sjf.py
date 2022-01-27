# Sortest Job First

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


def sorting_process(processes):
    return sorted(processes, key=lambda x: x[1])


if __name__ == '__main__':
    # Take input from user process name and brust time
    number_of_process = int(input("Enter Number of Process"))
    process = list()
    while number_of_process != 0:
        process_name = input('Process Name: ')
        brust_time = int(input('Brust Time: '))
        temp = (process_name, brust_time)
        process.append(temp)
        number_of_process -= 1

    sorted_process = sorting_process(processes=process)
    fcfs = gantt_generator(processes=sorted_process)
    print('GANTT Chart String: ', fcfs[0])
    print('Average waiting Time: ', fcfs[1])
