#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    try:
        while (x > a):
            print("{}".format(my_list[a]), end="")
            x += 1
    except IndexError:
        None
    print("")
    return (a)
