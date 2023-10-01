#!/usr/bin/python3
"""Finds Peak of List"""
def find_peak(list_of_integers):
    """Find Peak in the list

    Args:
        list_of_integers: list of int
    Returns:
        the value or None
    """
    lis = list_of_integers
    b = len(lis)
    if (b <= 2):
        return (None)
    for i in range(1, b - 1):
	    if (lis[i - 1] <= lis[i] >= lis[i + 1]):
	        return (lis[i])
    return (None)
