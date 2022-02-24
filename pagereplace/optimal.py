# OPTIMAL PAGE REPLACEMENT (OPT)
def opt(s, capacity):
    f, fault, pf = [], 0, 'Miss'
    print("\nString|Frame →\t", end='')
    for i in range(capacity):
        print(i, end=' ')
    print("Hit\\Miss\n   ↓\n")
    occurance = [None for i in range(capacity)]
    for i in range(len(s)):
        if s[i] not in f:
            if len(f) < capacity:
                f.append(s[i])
            else:
                for x in range(len(f)):
                    if f[x] not in s[i + 1:]:
                        f[x] = s[i]
                        break
                    else:
                        occurance[x] = s[i + 1:].index(f[x])
                else:
                    f[occurance.index(max(occurance))] = s[i]
            fault += 1
            pf = 'Miss'
        else:
            pf = 'Hit'
        print("   %d\t\t" % s[i], end='')
        for x in f:
            print(x, end=' ')
        for x in range(capacity - len(f)):
            print(' ', end=' ')
        print(" %s" % pf)
    print(f"\nTotal Page Faults: {fault}")


if __name__ == '__main__':
    print("Enter the number of frames: ", end="")
    frames = int(input())

    print("Enter the reference string: ", end="")
    # Take any of two algorithms and other one remove
    requests = list(map(int, input().strip().split(sep=',')))
    print('\n\nOPTIMAL PAGE REPLACEMENT (OPT) OUTPUT : ')
    opt(s=requests, capacity=frames)
