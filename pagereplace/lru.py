# LEAST RECENTLY USED
def lru(s, capacity):
    f, st, fault, pf = [], [], 0, 'Miss'
    print("\nString|Frame →\t", end='')
    for i in range(capacity):
        print(i, end=' ')
    print("Hit\\Miss\n   ↓\n")
    for i in s:
        if i not in f:
            if len(f) < capacity:
                f.append(i)
                st.append(len(f) - 1)
            else:
                ind = st.pop(0)
                f[ind] = i
                st.append(ind)
            pf = 'Miss'
            fault += 1
        else:
            st.append(st.pop(st.index(f.index(i))))
            pf = 'Hit'
        print("   %d\t\t\t" % i, end='')
        for x in f:
            print(x, end=' ')
        for x in range(capacity - len(f)):
            print(' ', end=' ')
        print(" %s" % pf)
    print(f"\nTotal Page Faults: {fault}" )


if __name__ == '__main__':
    print("Enter the number of frames: ", end="")
    frames = int(input())

    print("Enter the reference string: ", end="")
    # Take any of two algorithms and other one remove
    requests = list(map(int, input().strip().split(sep=',')))
    print('\n\nLEAST RECENTLY USED (LRU) OUTPUT : ')
    lru(s=requests, capacity=frames)
