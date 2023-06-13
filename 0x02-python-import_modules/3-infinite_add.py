#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    summation = 0
    for i in range(len(sys.argv) - 1):
        summation += int(sys.argv[i + 1])
    print(summation)
