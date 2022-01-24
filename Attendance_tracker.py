##@Author: Sourav Ganguly (211011002)
##This script finds the attendance of a student with the help of the master sheet sent.
##I have renamed the book as sheet.xlsx and the name of the respective files as the corresponding dates
## Professor Koteswararao Kondepu TA: Gudepu Venkateswarlu, Abhishek Bhattacharyya
import pandas as pd
data2=pd.read_excel("D://datasets//Attendance//sheet.xlsx")
data2["Roll No"][0]=0
data2.head()
roll=data2['Roll No']; #column for roll number
roll=[str(int(i)) for i in roll] #converting from float to string format
import os
path="D://datasets//Attendance"; #path of file in local drive
fol=os.listdir(path);
fol.remove('sheet.xlsx')#removing the previous file
for l in fol:
    n_path=os.path.join(path,l); #joining the file names to the parent path
    data=pd.read_csv(n_path); #reading file in csv format
    predefined=data["Email"];
    pred_roll=[i.split('@')[0] for i in predefined]#splitting email to obtain roll-number only
    b=[];
    for i in range(len(roll)):
        a=roll[i];
        if(a in pred_roll):
            b.append(1);
        else:
            b.append(0)
    l=l.split('.')[0]#filename.csv is l and droopping the extension to make file name my column
    data2[l]=b
data2.to_excel('Final_sheet.xlsx')#name of the final sheet
