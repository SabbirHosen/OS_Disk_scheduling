# FIFO page replacement algorithm
def fifo(s, capacity):
    f, fault, top, pf = [], 0, 0, 'Miss'
    print("\nString|Frame →\t", end='')
    for i in range(capacity):
        print(i, end=' ')
    print("Hit\\Miss\n   ↓\n")
    for i in s:
        if i not in f:
            if len(f) < capacity:
                f.append(i)
            else:
                f[top] = i
                top = (top + 1) % capacity
            fault += 1
            pf = 'Miss'
        else:
            pf = 'Hit'
        print("   %d\t\t\t" % i, end='')
        for x in f:
            print(x, end=' ')
        for x in range(capacity - len(f)):
            print(' ', end=' ')
        print(" %s" % pf)
    print(f"Total Page Faults: {fault}")


if __name__ == '__main__':

    print("Enter the number of frames: ", end="")
    frames = int(input())

    print("Enter the reference string: ", end="")
    requests = list(map(int, input().strip().split(sep=',')))
    print('\n\nFIRST IN FIRST OUT (FIFO) OUTPUT : ')
    fifo(s=requests, capacity=frames)
