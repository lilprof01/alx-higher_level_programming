#!/usr/bin/python3
for i in range(0, 26, 1):
    print("{:c}".format(122 - i) if i % 2 == 0 else "{:c}".format(90 - i), end="")
