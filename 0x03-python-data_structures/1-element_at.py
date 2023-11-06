#!/usr/bin/python3
def element_at(my_list, idx):
    lenght = len(my_list)

    if idx < 0 or idx > len(my_list):
        print("NONE")
    else:
        print("Element at index {:d} is {}".format(idx, my_list.index(idx)))
