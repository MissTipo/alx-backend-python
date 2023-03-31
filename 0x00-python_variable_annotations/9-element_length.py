#!/usr/bin/env python3
'''Let's duck type an iterable object'''


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''duck type an iterable object'''
    return [(i, len(i)) for i in lst]
