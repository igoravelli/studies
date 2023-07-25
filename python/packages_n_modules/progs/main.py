from sys import path
path.append('../modules/')


for p in path:
    print(p)

import module as md

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(md.suml(zeroes))
print(md.prodl(ones))