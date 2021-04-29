#!/usr/bin/python3

if __name__ == "__main__":
    import sys

total = 0
for argv in range(len(sys.argv)):
    if (argv == 0):
        continue
    else:
        total += int(sys.argv[argv])
print(total)
