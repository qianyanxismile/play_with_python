from __future__ import print_function
from collections import deque


def search(lines, pattern, history=3):
    historys = deque(maxlen=history)

    for line in lines:
        if pattern in line:
            yield line, historys
        historys.append(line)


if __name__ == "__main__":
    with open("somefile.txt") as f:
        for current_line, historys in search(f, "python"):
            for history in historys:
                print(history, end="")
            print(current_line, end="")
            print("-"*20)
