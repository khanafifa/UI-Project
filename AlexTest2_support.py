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

def readCSV(p1, fname, sep, com, head):
    tic = time.perf_counter()
    w.data = pd.read_csv(fname, sep=sep, comment=com, header = head)
    toc = time.perf_counter()
    showDataSize()
    if w.ft != None:
        w.ft.destroy()
        w.ft = None
    tk.messagebox.showinfo("Information", 'Elapsed Time (seconds) {}'.format(toc - tic))
    
def readExcel(p1, fname, sheets, cols, head, numrows):
    tic = time.perf_counter()
    w.data = pd.read_excel(fname, sheet_name=sheets, usecols=cols, nrows = numrows, header = head)
    toc = time.perf_counter()
    showDataSize()
    if w.ft != None:
        w.ft.destroy()
        w.ft = None
    tk.messagebox.showinfo("Information", 'Elapsed Time (seconds) {}'.format(toc - tic))

def on_closing():
    return
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

def showWorking():
    w.ft = tk.Toplevel()
    w.ft.protocol("WM_DELETE_WINDOW", on_closing) 
    pb_hD = ttk.Progressbar(w.ft, orient='horizontal', mode='indeterminate')
    pb_hD.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
    pb_hD.start(50)
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
        try:
            w.data = pd.read_csv(fname, sep=sep, comment=com, header=head, nrows=MaxRows)
        except Exception as e:
            tk.messagebox.showerror("Error", 'Exception {}'.format(e))
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
        return
        
    elif d.result[0] == 2:
        sheets = d.result[1]
        cols = d.result[2] if d.result[2] else None
        head = d.result[3]
        numrows = d.result[4]
        fname = tk.filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("excel files","*.xls"),("all files","*.*")))
        try:
            w.data = pd.read_excel(fname, sheet_name=sheets, usecols=cols, nrows = MaxRows, header = head)
        except Exception as e:
            tk.messagebox.showerror("Error", 'Exception {}'.format(e))
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





