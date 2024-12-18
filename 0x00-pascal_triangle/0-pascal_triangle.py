#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    fin = []
    if n > 0:
        for i in range(1, n + 1):
            height = []
            C = 1
            for j in range(1, i + 1):
                height.append(C)
                C = C * (i - j) // j
            fin.append(height)
    return fin
