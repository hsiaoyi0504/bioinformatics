#!/usr/local/bin/python3
data=[]
with open('HUMAN_9606_idmapping.dat') as f:
    for line in f:
        if 'GeneID' in line:
            data.append(line)
    f.close()
with open('human-uniprot-accession-gene-ID-mapping.txt','w') as f:
    for line in data:
        value = line.split()
        f.write( value[0] + '\t' + value[2] + '\n' )
    f.close()
