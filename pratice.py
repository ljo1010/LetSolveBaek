from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    a= copy.deepcopy(seq)
    a.append(key)

    i = 0
    while True:
        if a[i] == key