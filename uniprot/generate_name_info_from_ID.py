#!/usr/local/bin/python3
with open('uniprot_sprot_human.dat') as f:
    with open('uniprot_name_info','w') as f2:
        for line in f:
            if 'ID   ' in line and 'Reviewed' in line:
                temp = line.replace('\n','')
                temp = temp.split(';')[0]
                temp = temp.replace('ID   ','')
                temp = temp.replace('Reviewed','')
                temp = temp.split(' ')[0]
                data = []
                data.append(temp)
            elif 'DE   RecName' in line:
                temp = line.replace('\n','')
                temp = temp.split(';')[0]
                temp = temp.replace('DE   RecName: Full=','')
                if '{' in temp:
                    temp = temp.split('{')[0]
                data.append(temp)
            elif 'GN   Name=' in line:
                temp = line.replace('\n','')
                temp = temp.split(';')[0]
                temp = temp.replace('GN   Name=','')
                if '{' in temp:
                    temp = temp.split('{')[0]
                data.append(temp)
                f2.write(data[0]+'\t'+data[1]+'\t'+data[2]+'\n')

