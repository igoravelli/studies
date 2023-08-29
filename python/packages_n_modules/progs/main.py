from sys import path
path.append('/home/igor/studies/python/packages_n_modules/modules/')

import module as md

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(md.suml(zeroes))
print(md.prodl(ones))