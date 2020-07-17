import pandas as pd
from tkinter import filedialog
import geopandas as gpd
import matplotlib.pyplot as plt
from tkinter import *
import tkinter

#root = tkinter.Tk()
#root.withdraw()

#asks user to select csv to convert
file_name = filedialog.askopenfilename(initialdir = "/", title = (("CSV files","*.csv"),("all files",".")))
#root.update()
#root.destroy()
#reads csv and saves as dataframe
geo_data = pd.read_csv(file_name)

#creates a geoDataFrome from the DataFrame. the column names are specific to SWNewMexico BHT Geothermal data. need to find a way to automate selecting columns
#have the user select cross refference lookup table not all datasets will have headers so having set variables will be more secure
geo_gdf = gpd.GeoDataFrame(geo_data, geometry = gpd.points_from_xy(geo_data['Long_dd83'],geo_data['Lat_dd83']))


geo_gdf.plot()

ESRI_WKT = 'PROJCS["NAD83_HARN_New_Mexico_West",GEOGCS["GCS_NAD83(HARN)",DATUM["D_North_American_1983_HARN",SPHEROID["GRS_1980",6378137,298.257222101]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]],PROJECTION["Transverse_Mercator"],PARAMETER["latitude_of_origin",31],PARAMETER["central_meridian",-107.8333333333333],PARAMETER["scale_factor",0.999916667],PARAMETER["false_easting",830000],PARAMETER["false_northing",0],UNIT["Meter",1]]'
#needs to incorporate projection file. epsg code or WKT well known text code espg.io
geo_gdf.to_file(filename ='sampleOutput.shp', driver = 'ESRI Shapefile', crs_wkt = ESRI_WKT )

print("Made it here!!")







