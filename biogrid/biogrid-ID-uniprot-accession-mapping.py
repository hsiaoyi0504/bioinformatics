#!/usr/local/bin/python3
with open('BIOGRID-IDENTIFIERS-3.4.134.tab.txt') as f:
    with open('biogrid-ID-uniprot-accession-mapping.txt','w') as f2:
        for line in f:
            if 'SWISS-PROT' in line or 'UNIPROT-ACCESSION' in line:
                value = line.split()
                f2.write( value[0] + '\t' + value[1] + '\n' )
        f2.close()
    f.close()
