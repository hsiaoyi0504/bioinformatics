#!/usr/local/bin/python3
uniprot_accession_biogrid_ID_mapping = {}
with open('../biogrid/biogrid-ID-uniprot-accession-mapping.txt') as f:
    for line in f:
        temp = line.split()
        uniprot_accession_biogrid_ID_mapping[ temp[1] ] = temp[0]
    f.close()

with open('human-uniprot-accession-uniprot-entry-name-mapping.txt') as f:
    with open('human-uniprot-entry-name-biogrid-ID-mapping.txt','w') as f2:
        for line in f:
#            print(line)
            temp = line.split()
            try:
                search_rseult = uniprot_accession_biogrid_ID_mapping[ temp[0] ]
                f2.write( temp[1] + '\t' + uniprot_accession_biogrid_ID_mapping[ temp[0] ] + '\n' )
            except KeyError:
                pass
        f2.close()
    f.close()
