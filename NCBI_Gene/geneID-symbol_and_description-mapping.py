#!/usr/local/bin/python3
from itertools import islice
with open('gene_info') as f:
    with open('geneID-symbol_and_description-mapping.txt','w') as f2:
        for line in islice(f,1,None):
            temp = line.split()
            f2.write(temp[1]+'\t'+temp[2]+'\t'+temp[8]+'\n')
