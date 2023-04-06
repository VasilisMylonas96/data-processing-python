#ksaderfakiom taglar 2828 ?
#eisagogi bibliothikis pou tha xreisimopoihthei gia to read 
import csv 
#  gia to anigma tou arxeiou R_sorted
fileR  = "./R_sorted.tsv"
fR=open(fileR)
FR=csv.reader(fR,delimiter="\t")
#  gia to anigma tou arxeiou S_sorted
fileS="./S_sorted.tsv"
fs=open(fileS,encoding='utf-8')#to encoding xreiazete giati mou ebgaze problima gia decode error ean sta linux yparxei thema apla mporeite na to sbisete ean kai den tha xreiastei
FS=csv.reader(fs,delimiter="\t")
output = "RjoinS.tsv"
out=open(output,"w",encoding='utf-8')
colcheck1=[0,0]
colcheck2=[0,0]
flag=0
flag2=0
flag2=0
Sarray=[]
##out.write("primaryTitle"+"\t\t\t\t\t"+"directors" +"\n")#tha mporouse na ginei kai automata mesa stin for apla epeleksa na to kanw xeirokinita egw .
for colfr in FR:#gia kathe col sto arxeio fdirectors 
    
    if (colcheck1[0]==colfr[0] and colcheck1[1]!=colfr[1]):
        for number in Sarray:
            out.write(colfr[0]+"\t\t"+colfr[1]+"\t\t"+number+"\n")
            flag2=1

    if (flag==1):
        if (colfr[0]==colfs[0]):
            out.write(colfr[0]+"\t\t"+colfr[1]+"\t\t"+colfs[1]+"\n")
                
            Sarray.append(colfs[1])
    if (colcheck1[0]!=colfr[0] and colcheck1[1]!=colfr[1] and flag2==0):  
        for colfs in FS:#gia kathe col sto arxeio fdirectors 
                if (colcheck2[0]==colfs[0] and colcheck2[1]==colfs[1]):
                    break
                elif (flag==0):
                    flag=1
                if (colcheck2[0]==colfs[0] and colcheck2[1]==colfs[1]): 
                    break
                elif (colfr[0]!=colfs[0]):
                    break
                elif (colfr[0]==colfs[0]):
                    out.write(colfr[0]+"\t\t"+colfr[1]+"\t\t"+colfs[1]+"\n")
                    Sarray.append(colfs[1])
    colcheck1[0]=colfr[0]
    colcheck1[1]=colfr[1]
    colcheck2[0]=colfs[0]
    colcheck2[1]=colfs[1]
out.close()
