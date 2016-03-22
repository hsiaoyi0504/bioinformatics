#!/usr/local/bin/python3
with open('BIOGRID-IDENTIFIERS-3.4.134.tab.txt') as f:
    with open('biogrid-ID-uniprot-ID-mapping.txt','w') as f2:
        for line in f:
            if 'SWISS-PROT' in line:
                f2.write(line)
        f2.close()
    f.close()

