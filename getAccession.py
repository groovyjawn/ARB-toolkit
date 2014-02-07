###############################################################################
'''
 Program: getAccession.py                                                    
 Rev: 1.1                                                                    
 Date: 2/3/14                                                                
 Author: S. Essinger
 Description: Maps unique ID from database to each alignment
'''                                                                                                                                          
###############################################################################

inFile = raw_input('Enter name of database: ')
#inFile = open('MFS_metaData.txt','r')
outFile = open('ListAccessions_temp.txt','w')

for line in inFile:
    if line.startswith('>'):
        temp = line.split('\t',12)
        revised = temp[11].partition('_')
        if revised[1]:
            revised = revised[0]+'|A'
        else:
            revised = revised[0]
        outFile.write(str(temp[1])+'\t'+str(revised)+'\n')
               
inFile.close()
outFile.close()

#inACC = open('ListAccessions.txt','r')
#inALN = open('MFS_Align.fasta','r')
#outALN = open('MFS_UID.fasta','w')

inACC = open('ListAccessions_temp.txt','r')
inALN = open('Enter name of alignment file: ')
fooALN = open('Enter desired name for Unique IDs file: ')
outALN = open(fooALN,'w')

UID = []
ACC = []
for line in inACC:
    line = line.strip()
    line = line.partition('\t')
    hack = line[2].partition('|')
    UID.append(str(line[0]))
    ACC.append(str(hack[0]))
inACC.close()

for line in inALN:
    if line.startswith('>'):
        outALN.write('\n')
        temp = line.partition('pdb|')
        if len(temp[1]) == 0:
            temp = line.partition('sp|')
        temp = temp[2].partition('|')
        temp = temp[0].partition('.')
        try:
            key = ACC.index(temp[0])
            plug = UID[key]
            outALN.write('>'+str(plug)+'\n')
        except ValueError:
            key = 'MISSING_IN_DATABASE'
            outALN.write('>'+str(key)+'\n')
    else:
        outALN.write(line)
    
inALN.close()
outALN.close()