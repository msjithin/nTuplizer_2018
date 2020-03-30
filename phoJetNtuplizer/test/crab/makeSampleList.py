
import os

fileIn = open('mc_sample_dict', 'r') 
count = 0
fileOut=open('mc_sample_list', 'w')  
sampleName=""
sampleList=[]
for line in fileIn:
    count += 1
    sampleName=line.split(' ')[0]
    #print(sampleName)
    sampleName = sampleName[1:-1]
    sampleList.append(sampleName)
    
#print(sampleList)
#fileOut.write(str(sampleList))
sampleList=sorted(sampleList)
for i in sampleList:
    fileOut.write(str(i)+'\n')
fileOut.close()
fileIn.close()
