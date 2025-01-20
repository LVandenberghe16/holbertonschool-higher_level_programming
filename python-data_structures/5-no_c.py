#!/usr/bin/python3
def no_c(my_string):
    rm = "Cc"
    translation = my_string.maketrans(my_string,my_string,rm)
    my_string = my_string.translate(translation)
    return my_string
