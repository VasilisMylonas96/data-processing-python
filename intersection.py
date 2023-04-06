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
output = "intersection.tsv"
out=open(output,"w",encoding='utf-8')
flag=0
for colfr in FR:
    if flag==1:
        flag=2
        print("panw"+colfr[1],colfs[1])
        if colfr[0]==colfs[0] :
            if colfr[1]==colfs[1]:
                    out.write(colfr[0]+"\t\t"+colfr[1]+"\n")
            elif colfr[1]<colfs[1]:
                flag=1
        elif colfr[0]!=colfs[0]:
             if colfr[0]<colfs[0]:
                flag=1   
    else:
        for colfs in FS:
            print(colfr[1],colfs[1])
            if colfr[0]==colfs[0]:
                if colfr[1]==colfs[1]:
                    out.write(colfr[0]+"\t\t"+colfr[1]+"\n")
                    break
                elif colfr[1]<colfs[1]:
                    break

            if colfr[0]!=colfs[0]:
                if colfr[0]<colfs[0]:
                    flag=1
                    break
            
out.close()
