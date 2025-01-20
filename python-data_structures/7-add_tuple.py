#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure each tuple has at least two elements by adding 0s if necessary
    tuple_a = (tuple_a + (0, 0))[:2]
    tuple_b = (tuple_b + (0, 0))[:2]

    # Add corresponding elements
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
