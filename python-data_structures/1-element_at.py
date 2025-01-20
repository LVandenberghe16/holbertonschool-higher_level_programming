#!/usr/bin/python3
def element_at(my_list, idx):
    size = len(my_list)
    if idx > size:
        return None
    elif idx < 0:
        return None
    else:
        return my_list[idx]
