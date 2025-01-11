""" 
Lower Bound:

    Definition: The index of the first occurrence of an element in a sorted array (or the position where it can be inserted without breaking the order).
    If the element exists: Index of the first occurrence.
    If the element does not exist: The insertion point for the element.
    Can be found using bisect_left() in Python.

Upper Bound:

    Definition: The index of the first position after the last occurrence of an element in a sorted array (or the position where a larger element can be inserted without breaking the order).
    If the element exists: Index immediately after the last occurrence.
    If the element does not exist: The insertion point for elements greater than the target.
    Can be found using bisect_right() in Python.

"""