# User Interface for Large Data Set Files
 -The GUI provides assistance to visualize ,reproduce and export large dataset files used for geological surveying.
-Provides statistics on the dataset - (Min, max, count, average mean, standard deviation and KMean  Analytics)
-Files can be exported as CSV, JSON and ARCGIS shape files for geological surveying .
-Generates a 2D graph for required dataset points .

# Requirements
- Python 2.7 and above

# Recommended modules

- Python tKinter 8.6 (other versions not tested)
- Numpy library
- Pandas Library

To export data as shape file "Geopandas" module is required

# Configuration and Running the project

Run AlexTest2.py file which launches the interface
	# Read Button
	Click on "Read" button to import the file
	Check the "Header checkbox" if the file contains header
	For Delimited Text files, select the delimiter and comment specifier
	For excel, set the Sheet name (which page in excel to read, the importer can only read one page at a time),
	the column range (excel style column selections should work, e.g. A:Z), and the number of rows

	# Reset Button
	Clears the table displaying imported data
  
	# Statistics Button
	To view the statistics of the imported data 
	
	# Export Button
	Exports the file as CSV or JSON and save to your local directory
	To export as Shape file, Select the Latitude and Longitude columns 
	Note - Geopandas module is required to export as Shape file
	
	# Graph Button
	Select the desired columns to view the data as a 2D graph
	
	# Kmean Button
	Select the desired columns and input the number of cluster to view the clustered data
	





