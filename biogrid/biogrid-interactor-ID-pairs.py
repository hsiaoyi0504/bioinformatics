#!/usr/local/bin/python3
from itertools import islice
with open('BIOGRID-MV-Physical-3.4.134.tab2.txt') as f:
    with open('biogrid-interactor-ID-pairs.txt','w') as f2:
        for line in islice(f,1,None):
            temp = line.split('\t')
            if int(temp[3]) > int(temp[4]):
                f2.write(temp[4]+'\t'+temp[3]+'\n')
            else:
                f2.write(temp[3]+'\t'+temp[4]+'\n')

