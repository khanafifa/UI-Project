# -*- coding: utf-8 -*-
def plotData():
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
    Xvalues=[]
    Yvalues=[]
    i=0
    clicked_items1= listbox.curselection() ##Selected numbers from the listbox 
    root = Tk()
    for item in clicked_items1:
        Xvalues.append(sheet.cell_value(int(clicked_items1[i]),int(clicked.get())))##grabs items selected from excel sheet
        i+=1                                                                       ##clicked.get grabs the number that the user selected from OptionMenu 
    i=0
    for item2 in clicked_items1:
        Yvalues.append(sheet.cell_value(int(clicked_items1[i]),int(clicked2.get())))
        i+=1
    figure = Figure(figsize=(5,4),dpi=100)
    
    ##All the stuff below is makeing the graph and putting it in a window
    plot = figure.add_subplot(1,1,1)
    plot.bar(Xvalues,Yvalues)   ### puts the x/y values onto the graph
    plot.set_ylabel(sheet.cell_value(0,int(clicked2.get())))  ##labels y values for the graph
    plot.set_xlabel(sheet.cell_value(0,int(clicked.get())))   ## labels x values for the graph
    canvas = FigureCanvasTkAgg(figure, root) ##puts the graph onto the window
    canvas.get_tk_widget().grid(row=0, column=0)
    figure.tight_layout()
    root.mainloop()
    
import xlrd
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter import *
loc = ("/Users/tjjj44/.spyder-py3/Project/utah08.xlsx") ##grabs the excel file
i = 0
wb = xlrd.open_workbook(loc) ##reading excel file
sheet = wb.sheet_by_index(0) ##reading excel file
r = Tk()
r.title('Graphing data')
notebook = ttk.Notebook(r)
notebook.pack()
frame1 = Frame(notebook,width=500,height=500)
frame1.pack(fill = "both", expand =1)
notebook.add(frame2, text = 'reg tab')
notebook.add(frame1,text='Graph')

label=Label(frame1,text = "What colunm do you want to be the X value?")
label.pack(pady=5)
colnums=[]
clicked = StringVar()
i=0
while (i < sheet.ncols):  ##This while loops gets the amount of columns and sheet.ncols tells you the amount of columns in the excel file you are reading
    colnums.append(i)
    i+=1
clicked.set(colnums[0])
drop =OptionMenu(frame1, clicked,*colnums)
drop.pack(pady=5)
i=0
label2 = Label(frame1,text= "What rows do you want to use?")
label2.pack(pady=18)
listbox=Listbox(frame1,selectmode = "multiple")
listbox.pack(pady=18)

while (i < sheet.nrows):
    listbox.insert(END,i)
    i+=1
label3 =Label(frame1,text="What column do you want to be the Y value?")
label3.pack(pady=20)
clicked2=StringVar()
clicked2.set(colnums[0])
drop2=OptionMenu(frame1,clicked2,*colnums)
drop2.pack()
button = Button(frame1,text="Plot Data",command = plotData) ## when button is pressed go to graph the data
button.pack(pady =35)
r.mainloop()