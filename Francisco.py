# -*- coding: utf-8 -*-
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def checkVar(var):
    if is_integer(var)==True:
        return True
    else:
        return False
def getTheRightInput(var1):
    while checkVar(var1) ==False or int(var1) > sheet.ncols:
        var1 =input("please put a valid input: ")
    return var1
import xlrd
import matplotlib.pyplot as plt
loc = ("/Users/tjjj44/.spyder-py3/Project/mainedata.xlsm") ##grabs the excel file
i = 0
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(1)
print(sheet.ncols)
col = input("What colunm do you want to be the x value: ") 
if checkVar(col)==False or (int(col) > sheet.ncols):
    col=getTheRightInput(col)
           
inputs=[]
input1 = input("Enter a row: ")
if checkVar(input1)==False:
    input1=getTheRightInput(input1)
while input1 != "":
        inputs.append(input1)    ##stores all the input for the rows that they want
        input1 = input("Enter Another row if not just press enter: ") 
        if checkVar(input1)==False:
            if input1!="":
                input1=getTheRightInput(input1)

Xvalues=[]
Yvalues = []
#print(inputs[1])
for x in inputs:
    Xvalues.append(sheet.cell_value(int(inputs[i]),int(col))) ##grab from the excel
                                                              ##and stores the rows that they wanted
    i+=1
                  

col2 = input("what columns do you want to be the y value: ")
if checkVar(col2)==False or int(col2) > sheet.ncols:
    col2=getTheRightInput(col2)

i = 0
for x in inputs:
    Yvalues.append(sheet.cell_value(int(inputs[i]),int(col2))) 
    i+=1   
    

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
Xgraph = Xvalues
Ygraph = Yvalues
ax.bar(Xvalues,Yvalues)
ax.set_ylabel(sheet.cell_value(0,int(col2)))   
ax.set_xlabel(sheet.cell_value(0,int(col)))
plt.show()



##print(sheet.cell_value(int(row),int(col)))
##print(sheet.nrows)
##print(sheet.row_values(1)) 



