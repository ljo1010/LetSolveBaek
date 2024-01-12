from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    
    num = 9  # Fixed: Set the number of elements to 9
    x = [0] * num

    for i in range(num):
        x[i] = int(input(""))

    print(max_of(x))
    print(x.index(max_of(x))+1)
