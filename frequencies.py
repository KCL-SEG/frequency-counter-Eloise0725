"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for a in items:
        a = str(a)
        if a not in frequencies:
            frequencies[a] = 1
        else:
            frequencies[a] += 1
    return frequencies
