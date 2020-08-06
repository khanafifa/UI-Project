#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.3
#  in conjunction with Tcl version 8.6
#    Jul 04, 2020 04:08:09 PM CDT  platform: Windows NT
#    Jul 07, 2020 12:40:33 PM CDT  platform: Windows NT
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#needed for the arcGIS shapefile
import geopandas as gpd

from tkinter import *

import sys

import time
import threading
#from DialogTest1 import *


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
    import tkinter.filedialog
    import tkinter.messagebox
    from tkinter import simpledialog
    from tkinter import Radiobutton

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


X_COLUMN = ""
Y_COLUMN = ""
X_COLUMNY_COLUMN = []

class MyDialog(simpledialog.Dialog):

    """def body(self, master):

        tk.Label(master, text="First:").grid(row=0)
        tk.Label(master, text="Second:").grid(row=1)

        self.e1 = tk.Entry(master)
        self.e2 = tk.Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1 # initial focus"""
    def draw_csv_options(self):
        self.lbl1.grid(row=0, sticky=tk.W)
        self.lbl2.grid(row=1, sticky=tk.W)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        
    def forget_csv_options(self):
        self.e1.grid_forget()
        self.e2.grid_forget()
        self.lbl1.grid_forget()
        self.lbl2.grid_forget()
        
        
    def draw_excel_options(self):
        self.lbl3.grid(row=0, sticky=tk.W)
        self.lbl4.grid(row=1, sticky=tk.W)
        self.e3.grid(row=0, column=1)
        self.e4.grid(row=1, column=1)
        self.cb1.grid(row=3, column=0)
        self.checkNumRows()
        
    def forget_excel_options(self):
        self.e3.grid_forget()
        self.e4.grid_forget()
        self.lbl3.grid_forget()
        self.lbl4.grid_forget()
        self.cb1.grid_forget()
        self.eNumRows.grid_forget()

    def sel(p1):
        print(p1.var.get())
        if p1.var.get() == 1:
            p1.forget_excel_options()
            p1.draw_csv_options()
        else:
            p1.forget_csv_options()
            p1.draw_excel_options()
        return
    
    def checkNumRows(p1):
        if p1.cb1Var.get():
            p1.eNumRows.grid_forget()
        else:
            p1.eNumRows.grid(row=3, column=1)
            
    
    def body(self, master):

        self.lbl1 = tk.Label(master, text="Delim:")
        self.lbl2 = tk.Label(master, text="Comment:")

        self.e1 = tk.Entry(master)
        self.e2 = tk.Entry(master)
        self.e1.insert(0, ',')

        #self.e1.grid(row=0, column=1)
        #self.e2.grid(row=1, column=1)
        
        self.lbl3 = tk.Label(master, text="Sheet:")
        self.lbl4 = tk.Label(master, text="Columns:")

        self.e3 = tk.Entry(master)
        self.e4 = tk.Entry(master)
        
        self.headerVar = tk.IntVar()
        self.cb = tk.Checkbutton(master, text="Header", variable=self.headerVar)
        self.cb.grid(row=2, columnspan=2, sticky=tk.W)
        self.var = tk.IntVar()
        tk.Radiobutton(master, text="Deliminated Text", variable=self.var, value=1, command=self.sel).grid(row=10, column=0, sticky=tk.W)
        tk.Radiobutton(master, text="Excel", variable=self.var, value=2, command=self.sel).grid(row=10, column=1, sticky=tk.W)

        self.cb1Var = tk.IntVar()        
        self.cb1 = tk.Checkbutton(master, text="Number of Rows (All):", variable=self.cb1Var, command=self.checkNumRows)
        self.cb1.select()
        self.eNumRows = tk.Entry(master)
        
        
        self.result=None
        self.var.set(1)
        self.sel()
        
    

    def apply(self):
        if self.var.get() == 1:
            first = self.e1.get()
            if first != None:
                first = str(first)
            second = self.e2.get()
            if second != None:
                second = str(second)
            header = 0 if self.headerVar.get() else None
            self.result = self.var.get(), first, second, header
        elif self.var.get() == 2:
            first = self.e3.get()
            if first != None:
                first = str(first)
            second = self.e4.get()
            if second != None:
                second = str(second)
            third = None if self.cb1Var.get() else self.eNumRows.get()
            if third != None:
                third = int(third)
            header = 0 if self.headerVar.get() else None
            self.result = self.var.get(), first, second, header, third









def previewTable(p1):
    MaxRows = 5
    inner_frame = w.Scrolledwindow1_f
    clearTable(p1)
    indx = -1;
    indx = indx + 1
    w.ents[indx] = ttk.Entry(inner_frame, width=20, font=('Arial',16,'bold'))
    w.ents[indx].grid(row=0, column=0)
    w.ents[indx].insert(tk.END, 'Row Num')
    for i in range(0, w.data.shape[1]):
        indx = indx + 1
        w.ents[indx] = ttk.Entry(inner_frame, width=20, font=('Arial',16,'bold'))
        w.ents[indx].grid(row=0, column=i+1)
        w.ents[indx].insert(tk.END, w.data.columns[i])
    for i in range(0, min(w.data.shape[0], MaxRows)):
        indx = indx + 1
        w.ents[indx] = ttk.Entry(inner_frame, width=20, font=('Arial',16,'bold'))
        try:
            w.ents[indx].grid(row=i+1, column=0)
            w.ents[indx].insert(tk.END, i)
        except Exception as e:
            print(e)
            print('Problem index {} row {}'.format(indx, i))
            break
            
        for j in range(0, w.data.shape[1]):
            indx = indx + 1
            w.ents[indx] = ttk.Entry(inner_frame, width=20, font=('Arial',16,'bold'))
            w.ents[indx].grid(row=i+1, column=j+1)
            inner_frame.rowconfigure(i+1, weight = 1)
            inner_frame.columnconfigure(j+1, weight = 1)
            w.ents[indx].insert(tk.END, w.data.iloc[i, j])
            
    w.ents[0].wait_visibility()
    inner_frame.bbox()
    bbox = inner_frame.bbox()
    w.Scrolledwindow1.configure(scrollregion=bbox)
    root.update()


def showDataSize():
    inner_frame = w.Scrolledwindow1_f
    indx = len(w.ents)
    w.ents[indx] = ttk.Entry(inner_frame, width=20, font=('Arial',16,'bold'))
    w.ents[indx].grid(row=6, column=0)
    w.ents[indx].insert(tk.END, 'Rows = {}'.format(w.data.shape[0]))
    indx = indx + 1
    w.ents[indx] = ttk.Entry(inner_frame, width=20, font=('Arial',16,'bold'))
    w.ents[indx].grid(row=7, column=0)
    w.ents[indx].insert(tk.END, 'Cols = {}'.format(w.data.shape[1]))
    indx = indx + 1
    w.ents[indx] = ttk.Entry(inner_frame, width=20, font=('Arial',16,'bold'))
    w.ents[indx].grid(row=8, column=0)
    w.ents[indx].insert(tk.END, 'Entries = {}'.format(w.data.size))

def closeWorkingMessage():
    if w.ft != None:
        w.ft.destroy()
        w.ft = None
        if w.thread_message:
            tk.messagebox.showinfo("Information", w.thread_message)
            w.thread_message = None

def readCSV(p1, fname, sep, com, head):
    tic = time.perf_counter()
    w.data = pd.read_csv(fname, sep=sep, comment=com, header = head)
    toc = time.perf_counter()
    showDataSize()
    #closeWorkingMessage()
    w.thread_message='Elapsed Time (seconds) {}'.format(toc - tic)
    
def readExcel(p1, fname, sheets, cols, head, numrows):
    tic = time.perf_counter()
    w.data = pd.read_excel(fname, sheet_name=sheets, usecols=cols, nrows = numrows, header = head)
    toc = time.perf_counter()
    showDataSize()
    #closeWorkingMessage()
    w.thread_message='Elapsed Time (seconds) {}'.format(toc - tic)

def on_closing():
    return
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

def showWorking():
    w.ft = tk.Toplevel(w.Frame1)
    w.ft.title('Work in progress, please be patient...')
    w.ft.geometry("%dx%d%+d%+d" % (400, 50, 250, 125))
    
    pb_hD = ttk.Progressbar(w.ft, orient='horizontal', mode='indeterminate')
    pb_hD.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
    pb_hD.start(50)
    w.ft.protocol("WM_DELETE_WINDOW", on_closing)
    w.ft.grab_set()
    root.update()

def readButtonPressed(p1):
    MaxRows = 5
    inner_frame = w.Scrolledwindow1_f
    print('AlexTest2_support.readButtonPressed', type(p1))
    sys.stdout.flush()
    wid = p1.widget
    tl = wid.nametowidget(wid.winfo_parent())
    print(tl.children)
    sys.stdout.flush()
    tf = tl.children['!frame'].children['!scrolledwindow']#.children['!scrolledentry']#.children['!frame']
    print(tf.children)
    sys.stdout.flush()

    
    d = MyDialog(root)
    print(d.result)
    if d.result == None:
        return
    elif d.result[0] == 1:
        sep = ',' if d.result[1] == None else d.result[1]
        com = d.result[2] if d.result[2] else None
        head = d.result[3]
        fname = tk.filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("text files","*.csv"),("all files","*.*")))
        if fname:
            try:
                w.data = pd.read_csv(fname, sep=sep, comment=com, header=head, nrows=MaxRows)
            except Exception as e:
                tk.messagebox.showerror("Error", 'Exception {}'.format(e))
                return
        else:
            return
        
        previewTable(p1)
        answer = tk.messagebox.askquestion("Previewing Data", "Do you wish to continue importing?", icon='warning')
        if answer == 'no':
            return
        
        
        #readCSV(p1, fname, sep, com, head)
        
        w.thread = threading.Thread(target=readCSV, args=(p1, fname, sep, com, head))
        w.thread.daemon = True # Allow the program to terminate without waiting for the thread to finish.
        w.thread.start()
        
        
        
        
        showWorking()
        checkWorkingMessage()
        return
        
    elif d.result[0] == 2:
        sheets = d.result[1]
        cols = d.result[2] if d.result[2] else None
        head = d.result[3]
        numrows = d.result[4]
        fname = tk.filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("excel files","*.xls"),("all files","*.*")))
        if fname:
            try:
                w.data = pd.read_excel(fname, sheet_name=sheets, usecols=cols, nrows = MaxRows, header = head)
            except Exception as e:
                tk.messagebox.showerror("Error", 'Exception {}'.format(e))
                return
        else:
            return
        
        previewTable(p1)
        answer = tk.messagebox.askquestion("Previewing Data", "Do you wish to continue importing?", icon='warning')
        if answer == 'no':
            return
        

        #readExcel(p1, fname, sheets, cols, head, numrows)
        w.thread = threading.Thread(target=readExcel, args=(p1, fname, sheets, cols, head, numrows))
        w.thread.daemon = True # Allow the program to terminate without waiting for the thread to finish.
        w.thread.start()
        
        
        
        
        showWorking()
        checkWorkingMessage()
        return
    


def bob():
    print('AlexTest2_support.{}')
    sys.stdout.flush()

def clearTable(p1):
    print('AlexTest2_support.clearTable')
    sys.stdout.flush()
    for i in reversed(list(range(len(w.ents)))):
        try:
            w.ents[i].destroy()
        except:
            pass
    w.ents = {}


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import AlexTest2
    AlexTest2.vp_start_gui()

def summarize(p1):
    inner_frame = w.Scrolledwindow1_f
    print('AlexTest2_support.readButtonPressed', type(p1))
    sys.stdout.flush()
    wid = p1.widget
    tl = wid.nametowidget(wid.winfo_parent())
    #tf = tl.nametowidget('TFrame1')
    print(tl.children)
    sys.stdout.flush()
    tf = tl.children['!frame'].children['!scrolledwindow']#.children['!scrolledentry']#.children['!frame']
    print(tf.children)
    sys.stdout.flush()
    #return
    #te = tf.children['!entry']
    #te.grid(row=1, column=1)
    #te.delete(0, tk.END)
    #te.insert(tk.END, 'Hello')
    #fname = 'C:\\Users\\Afifa Shareef\\Desktop\\UTSA Assignments\\Summer_2020\\UI_project\\OneDrive_1_7-6-2020\\Earthquake.csv'
    #data = pd.read_csv(fname)
    statistics = w.data.describe(include = 'all')
    lstf = statistics.values.tolist() 
    columnNames = []
    for col in statistics:
        columnNames.append(col)
    rowNames = ['count','unique','top','frequency','mean','std','min','25%','50%','75%','max']
    indx = indx = len(w.ents) -1;
    for i in range(len(rowNames)):
            indx = indx + 1
            w.ents[indx] = ttk.Entry(inner_frame, width=20, font=('Arial',16,'bold'))
            w.ents[indx].grid(row=i+9, column=0)
            #te.delete(0, tk.END)
            w.ents[indx].insert(tk.END, rowNames[i])
    #indx = -1;
    for j in range(len(columnNames)):
            indx = indx + 1
            w.ents[indx] = ttk.Entry(inner_frame, width=20, font=('Arial',16,'bold'))
            w.ents[indx].grid(row=9, column=j+1)
            #te.delete(0, tk.END)
            w.ents[indx].insert(tk.END, columnNames[j])
    #indx = -1;
    for i in range(len(lstf)):
        for j in range(len(lstf[0])):
            indx = indx + 1
            w.ents[indx] = ttk.Entry(inner_frame, width=20, font=('Arial',16,'bold'))
            w.ents[indx].grid(row=i+9, column=j+1)
            #te.delete(0, tk.END)
            w.ents[indx].insert(tk.END, lstf[i][j])
    w.ents[0].wait_visibility()
    bbox = inner_frame.bbox()
    w.Scrolledwindow1.configure(scrollregion=bbox)

def get_columns_from(ent1,ent2,ret,frame,frame2,frame3):
    X_COLUMN = ent1.get()
    Y_COLUMN = ent2.get()
    ret.append( X_COLUMN)
    ret.append(Y_COLUMN)
    
    frame.quit()
    

def checkWorkingMessage():
    if w.thread.isAlive():
        root.after(100, checkWorkingMessage)
    else:
        closeWorkingMessage()

def exportShapeFileWorker(geo_gdf, fname):
    tic = time.perf_counter()
    ESRI_WKT = 'PROJCS["NAD83_HARN_New_Mexico_West",GEOGCS["GCS_NAD83(HARN)",DATUM["D_North_American_1983_HARN",SPHEROID["GRS_1980",6378137,298.257222101]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]],PROJECTION["Transverse_Mercator"],PARAMETER["latitude_of_origin",31],PARAMETER["central_meridian",-107.8333333333333],PARAMETER["scale_factor",0.999916667],PARAMETER["false_easting",830000],PARAMETER["false_northing",0],UNIT["Meter",1]]'
#needs to incorporate projection file. epsg code or WKT well known text code espg.io
    geo_gdf.to_file(filename=fname, driver = 'ESRI Shapefile', crs_wkt = ESRI_WKT )
    toc = time.perf_counter()
    #closeWorkingMessage()
    w.thread_message='File {} saved.\nElapsed Time (seconds) {}'.format(fname, toc - tic)

def exportShapeFile(geo_data , frame,frame1,root2):
#creates a geoDataFrome from the DataFrame. the column names are specific to SWNewMexico BHT Geothermal data. need to find a way to automate selecting columns
#have the user select cross refference lookup table not all datasets will have headers so having set variables will be more secure
    #frame1.destroy()
    #frame.geometry("600x400")
    
    frame.geometry("%dx%d%+d%+d" % (700, 800, 250, 125))
    frame2 = Frame(frame)
    #frame2.pack_propagate(False)
    frame2.pack()
    frame3 = Frame(frame,width = 800)
    #frame3.pack_propagate(0)
    frame3.pack()
    
    scroll = Scrollbar(frame2,orient="horizontal")
    scroll.pack(side=TOP,pady=20,fill = X)
    
    hold = []
    lab = ttk.Treeview(frame2)
    lab.pack(side = TOP,pady=20)
    for i in range(len(geo_data.columns)):
        hold.append(i+1)
    lab["columns"] = (hold)
    
    for i in range(len(geo_data.columns)):
        lab.column(str(i+1),minwidth=100, anchor = 'c')
        lab.heading(str(hold[i]), text = str(hold[i]))
    
    for i in range(0,10):
        lab.insert("",tk.END ,values = list(geo_data.iloc[i,:]))
    
    scroll.config(command=lab.xview)
    lab.config(xscrollcommand = scroll.set)
   
    
    entlab1= Label(frame3, text = "please enter the column # for latitude")
    entlab1.grid(row=2,column=0)
    ent1 = Entry(frame3)
    ent1.grid(row=3,column=0)
    entlab2= Label(frame3, text = "please enter the column # for longitude")
    entlab2.grid(row=4,column=0)
    ent2 = Entry(frame3)
    ent2.grid(row=5,column=0)
    bttn = tk.Button(frame3, text = 'Enter', command = lambda : get_columns_from(ent1,ent2,X_COLUMNY_COLUMN,frame,frame2,frame3)) 
    bttn.grid(row = 6,column = 0)
    frame.mainloop()
    latHold = int(X_COLUMNY_COLUMN[1])
    print(latHold);
    latHold = latHold - 1
    longHold = int(X_COLUMNY_COLUMN[0])
    longHold = longHold - 1   
    geo_gdf = gpd.GeoDataFrame(geo_data, geometry = gpd.points_from_xy(geo_data.iloc[:,latHold].astype('float32'),geo_data.iloc[:,longHold].astype('float32')))
   
   # scale = Scale(frame, label = "dataset brief",from = 0, to = 100, command = getValue, orient="horizontal" )
    #scale.pack(fill = "x")
    #geo_gdf.plot()
    
    
    file_save = tk.filedialog.asksaveasfilename(initialdir = '/')
    w.thread = threading.Thread(target=exportShapeFileWorker, args=(geo_gdf, file_save))
    w.thread.daemon = True # Allow the program to terminate without waiting for the thread to finish.
   
    #showWorking()
    frame2.destroy()#quit()
    frame3.destroy()#quit()
    #root2.quit()
    showWorking()
    w.thread.start()
    print("Made it here!!")
    checkWorkingMessage()
    
    

def exportCSVWorker(data, fname):
    tic = time.perf_counter()
    data.to_csv(fname)
    toc = time.perf_counter()
    #closeWorkingMessage()
    w.thread_message='File {} saved.\nElapsed Time (seconds) {}'.format(fname, toc - tic)
    
def exportCSV(data,frame,frame1,root2):
    file_save = filedialog.asksaveasfilename(initialdir = '/', filetypes = (("CSV files","*.csv"),("All Files","*.*")))
    w.thread = threading.Thread(target=exportCSVWorker, args=(data, file_save+".csv"))
    w.thread.daemon = True # Allow the program to terminate without waiting for the thread to finish.
    w.thread.start()
    showWorking()
    checkWorkingMessage()

def exportJSONWorker(data, fname):
    tic = time.perf_counter()
    data.to_json(fname+".json")
    toc = time.perf_counter()
    #closeWorkingMessage()
    w.thread_message = 'File {} saved.\nElapsed Time (seconds) {}'.format(fname+".json", toc - tic)
            
            
def exportJSON(data,frame,frame1,root2):
    file_save = filedialog.asksaveasfilename(initialdir = '/', filetypes = (('JSON files','*.json'),('All Files','*.*')))
    w.thread = threading.Thread(target=exportJSONWorker, args=(data, file_save))
    w.thread.daemon = True # Allow the program to terminate without waiting for the thread to finish.
    w.thread.start()
    showWorking()
    checkWorkingMessage()

        
def exportSelect():
    if type(w.data) == type(None) or w.data.size == 0:
        tk.messagebox.showwarning("Warning", "Please import data before trying to export.")
        return
   
    #asks user to select csv to convert
    #file_name = filedialog.askopenfilename(initialdir = "/", title = (("CSV files","*.csv"),("all files",".")))
    #root.update()
    #root.destroy()
    #reads csv and saves as dataframe
    #geo_data = pd.read_csv(file_name)
    #print("file loaded all: ")
    # geo_data.shape
    #root2 = tk.Tk()
    w.data.columns = [str(i) for i in w.data.columns]
    geo_data = w.data;
    #root2.maxsize(width = 800,height=600)
    #root.propagate(0)
    frame = tk.Toplevel(root,width=800, height=600)
    #frame.pack_propagate(0)
    #frame.pack()
    frame1 = Frame(frame,width=600,height=400)
    frame1.pack()
    frame.geometry("%dx%d%+d%+d" % (400, 200, 250, 125))

    btn = tk.Button(frame1, text = 'Export shapefile', command = lambda : exportShapeFile(geo_data,frame,frame1,root)) 
    btn.pack(side = TOP, pady = 20)

    btn2 = tk.Button(frame1, text = 'Export CSV', command = lambda : exportCSV(geo_data,frame,frame1,root)) 
    btn2.pack(side = RIGHT, pady = 20)

    btn3 = tk.Button(frame1, text = 'Export JSON', command = lambda : exportJSON(geo_data,frame,frame1,root)) 
    btn3.pack(side = BOTTOM, pady = 20)

    
    
def graphSelected():
    print(w.data)
    i = 0
    r = tk.Tk()
    frame1 = Frame(r,width=2000,height=1000)
    frame1.pack(fill = "both", expand =1)
    label=Label(frame1,text = "What colunm do you want to be the X value?")
    label.pack(pady=5)
    colnums=[]
    clicked = StringVar()
    while (i < (w.data.shape[1])): 
        ##This while loops gets the amount of columns from the dataframe
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
    while (i < len(w.data)):
        listbox.insert(END,i)
        i+=1
    label3 =Label(frame1,text="What column do you want to be the Y value?")
    label3.pack(pady=20)
    clicked2=StringVar()
    clicked2.set(colnums[0])
    drop2=OptionMenu(frame1,clicked2,*colnums)
    drop2.pack()
    button = Button(frame1,text="Plot Data") ## when button is pressed go to graph the data
    button.bind("<Button-1>",plotData)
    button.pack(pady =35)
    r.mainloop()

def plotData():
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
    Xvalues=[]
    Yvalues=[]
    i=0

    # clicked_items1= items ##Selected numbers from the listbox 
    root = tk.Tk()
    # for item in clicked_items1:
    #     Xvalues.append(w.data.get_value(int(clicked_items1[i]),int(xselected),takeable = True))##grabs  selected from excel sheet
    #     i+=1                                                                       ##clicked.get grabs the number that the user selected from OptionMenu 
    # i=0
    # for item2 in clicked_items1:
    #     Yvalues.append(w.data.get_value(int(clicked_items1[i]),int(yselected),takeable= True))
    #     i+=1
    figure = Figure(figsize=(5,4),dpi=100)
    
    ##All the stuff below is makeing the graph and putting it in a window
    # plot = figure.add_subplot(1,1,1)
    # plot.bar(Xvalues,Yvalues)   ### puts the x/y values onto the graph
    # # plot.set_ylabel(w.data.columns.values[int(yselected)])  ##labels y values for the graph
    # # plot.set_xlabel(w.data.columns.values[int(xselected)])# labels x values for the graph
    # canvas = FigureCanvasTkAgg(figure, root) ##puts the graph onto the window
    # canvas.get_tk_widget().grid(row=0, column=0)
    # figure.tight_layout()
    # root.mainloop()



def aboutButtonPressed(p1):
    aboutTop = tk.Toplevel(root,width=800, height=600)
    #frame.pack_propagate(0)
    #frame.pack()
    frame1 = Frame(aboutTop,width=600,height=400)
    frame1.pack()
    aboutTop.geometry("%dx%d%+d%+d" % (800, 800, 250, 125))
    lbl1 = tk.Label(frame1, text="Created by Team Hydra 2020\nMany heads, one team!\nHeads as of August 2020\n"
                    "Alexander Downey\n"
                    "Mark Dziuk\n"
                    "Afifa Khan\n"
                    "Francisco Perez\n"
                    )
    lbl1.grid(row=0, sticky=tk.N)
    #img = tk.PhotoImage(data=open('HYDRA.png', encoding='ANSI').read(), format='png')
    img = tk.PhotoImage(file='HYDRA.png', format='png')
    lblImg = tk.Label(frame1, compound='top')
    lblImg['text'] = "HYDRA.png"
    lblImg['image'] = img
    lblImg.image = img
    lblImg.grid(row=10, sticky=tk.W)


    
    
    
    
    
    
    
    
    
    
    