#!/usr/local/bin/python3
with open('BIOGRID-IDENTIFIERS-3.4.134.tab.txt') as f:
    with open('official-symbol-biogrid-ID-mapping.txt','w') as f2:
        for line in f:
            if 'OFFICIAL SYMBOL' in line:
                value = line.split()
                f2.write( value[1] + '\t' + value[0] + '\n' )
        f2.close()
    f.close()

