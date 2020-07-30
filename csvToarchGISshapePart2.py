import pandas as pd
from tkinter import filedialog
import geopandas as gpd
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
from tkinter import ttk
#root = tkinter.Tk()
#root.withdraw()
X_COLUMN = ""
Y_COLUMN = ""
X_COLUMNY_COLUMN = []
#asks user to select csv to convert
file_name = filedialog.askopenfilename(initialdir = "/", title = (("CSV files","*.csv"),("all files",".")))
#root.update()
#root.destroy()
#reads csv and saves as dataframe
geo_data = pd.read_csv(file_name)
print("file loaded all: ")
geo_data.shape
root = tk.Tk()
root.maxsize(width = 800,height=600)

def get_columns_from(ent1,ent2,ret,frame):
    X_COLUMN = ent1.get()
    Y_COLUMN = ent2.get()
    ret.append( X_COLUMN)
    ret.append(Y_COLUMN)
    frame.quit()

def exportShapeFile(geo_data , frame,frame1):
#creates a geoDataFrome from the DataFrame. the column names are specific to SWNewMexico BHT Geothermal data. need to find a way to automate selecting columns
#have the user select cross refference lookup table not all datasets will have headers so having set variables will be more secure
    frame1.destroy()
    #frame.geometry("600x400")
    
    
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
    bttn = tk.Button(frame3, text = 'Enter', command = lambda : get_columns_from(ent1,ent2,X_COLUMNY_COLUMN,frame)) 
    bttn.grid(row = 6,column = 0)
    frame.mainloop()
    latHold = int(X_COLUMNY_COLUMN[1])
    latHold = latHold -1
    longHold = int(X_COLUMNY_COLUMN[0])
    longHold = longHold - 1
    geo_gdf = gpd.GeoDataFrame(geo_data, geometry = gpd.points_from_xy(geo_data.iloc[:,int(latHold)],geo_data.iloc[:,int(longHold)]))
   
   # scale = Scale(frame, label = "dataset brief",from = 0, to = 100, command = getValue, orient="horizontal" )
    #scale.pack(fill = "x")
    geo_gdf.plot()
    
    ESRI_WKT = 'PROJCS["NAD83_HARN_New_Mexico_West",GEOGCS["GCS_NAD83(HARN)",DATUM["D_North_American_1983_HARN",SPHEROID["GRS_1980",6378137,298.257222101]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]],PROJECTION["Transverse_Mercator"],PARAMETER["latitude_of_origin",31],PARAMETER["central_meridian",-107.8333333333333],PARAMETER["scale_factor",0.999916667],PARAMETER["false_easting",830000],PARAMETER["false_northing",0],UNIT["Meter",1]]'
#needs to incorporate projection file. epsg code or WKT well known text code espg.io
    file_save = filedialog.asksaveasfilename(initialdir = '/')
    geo_gdf.to_file(filename =file_save, driver = 'ESRI Shapefile', crs_wkt = ESRI_WKT )

    print("Made it here!!")
    frame.quit()
    
def exportCSV(data,frame,frame1):
            frame1.destroy()
            file_save = filedialog.asksaveasfilename(initialdir = '/', filetypes = (("CSV files","*.csv"),("All Files","*.*")))
            data.to_csv(file_save+".csv")
            frame.quit()
            
            
def exportJSON(data,frame,frame1):
        frame1.destroy()
        file_save = filedialog.asksaveasfilename(initialdir = '/', filetypes = (('JSON files','*.json'),('All Files','*.*')))
        data.to_json(file_save+".json")
        frame.quit()


#root.propagate(0)
frame = Frame(root,width=800, height=600)
#frame.pack_propagate(0)
frame.pack()
frame1 = Frame(frame,width=600,height=400)
frame1.pack()

btn = tk.Button(frame1, text = 'Export shapefile', command = lambda : exportShapeFile(geo_data,frame,frame1)) 
btn.pack(side = TOP, pady = 20)

btn2 = tk.Button(frame1, text = 'Export CSV', command = lambda : exportCSV(geo_data,frame,frame1)) 
btn2.pack(side = RIGHT, pady = 20)

btn3 = tk.Button(frame1, text = 'Export JSON', command = lambda : exportJSON(geo_data,frame,frame1)) 
btn3.pack(side = BOTTOM, pady = 20)

root.mainloop()


#def exportShapeFile(geo_data):
#creates a geoDataFrome from the DataFrame. the column names are specific to SWNewMexico BHT Geothermal data. need to find a way to automate selecting columns
#have the user select cross refference lookup table not all datasets will have headers so having set variables will be more secure
 #   geo_gdf = gpd.GeoDataFrame(geo_data, geometry = gpd.points_from_xy(geo_data['Long_dd83'],geo_data['Lat_dd83']))



  
#  geo_gdf.plot()

 #   ESRI_WKT = 'PROJCS["NAD83_HARN_New_Mexico_West",GEOGCS["GCS_NAD83(HARN)",DATUM["D_North_American_1983_HARN",SPHEROID["GRS_1980",6378137,298.257222101]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]],PROJECTION["Transverse_Mercator"],PARAMETER["latitude_of_origin",31],PARAMETER["central_meridian",-107.8333333333333],PARAMETER["scale_factor",0.999916667],PARAMETER["false_easting",830000],PARAMETER["false_northing",0],UNIT["Meter",1]]'
#needs to incorporate projection file. epsg code or WKT well known text code espg.io
  #  geo_gdf.to_file(filename ='sampleOutput.shp', driver = 'ESRI Shapefile', crs_wkt = ESRI_WKT )

   # print("Made it here!!")

#def exportCSV(data):
 #           file_save = filedialog.asksaveasfilename(initialdir = '/', filetypes = (('CSV files','*.csv')('All Files','*.*')))
  #          data.to_csv(file_save)
            
#def exportJSON(data):
 #       file_save = filedialog.asksaveasfilename(initialdir = '/', filetypes = (('JSON files','*.json')('All Files','*.*')))
  #      data.to_csv(file_save)
        





