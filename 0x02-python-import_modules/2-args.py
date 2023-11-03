#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

# Access the argv list and get its length
num_args = len(argv)

if num_args == 1:
    print("{} arguments.".format(num_args))
elif num_args == 2:
    print("{} argument:".format(num_args))
    print("{}: {}".format(argv[1]))
else:
    print("{} arguments:".format(len(argv) - 1))
    for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
