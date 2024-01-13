#퀵정렬 따라써보기
from typing import MutableSequence

def qsort(a:MutableSequence, left:int, right: int) -> None:

    pl = left
    pr = right
    x = a[(left + right) // 2]
    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(a, left, pr)
                                                  