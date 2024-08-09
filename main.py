import pandas as pd

file_path_POLMEO1 = 'Place-POL_MID-Sensor-ANT_POL_MID-To-Satellite-POLMEO1_AER.csv'
file_path_POLMEO2 = 'Place-POL_MID-Sensor-ANT_POL_MID-To-Satellite-POLMEO2_AER.csv'
file_path_POLMEO3 = 'Place-POL_MID-Sensor-ANT_POL_MID-To-Satellite-POLMEO3_AER.csv'
file_path_POLMEO4 = 'Place-POL_MID-Sensor-ANT_POL_MID-To-Satellite-POLMEO4_AER.csv'
data_polmeo1 = pd.read_csv ( file_path_POLMEO1 , on_bad_lines = 'skip' )
data_polmeo2 = pd.read_csv ( file_path_POLMEO2 , on_bad_lines = 'skip' )
data_polmeo3 = pd.read_csv ( file_path_POLMEO3 , on_bad_lines = 'skip' )
data_polmeo4 = pd.read_csv ( file_path_POLMEO4 , on_bad_lines = 'skip' )

# Convert the 'Elevation (deg)' column to numeric, forcing errors to NaN
data_polmeo1['Elevation (deg)'] = pd.to_numeric ( data_polmeo1['Elevation (deg)'] , errors='coerce' )
data_polmeo2['Elevation (deg)'] = pd.to_numeric ( data_polmeo2['Elevation (deg)'] , errors='coerce' )
data_polmeo3['Elevation (deg)'] = pd.to_numeric ( data_polmeo3['Elevation (deg)'] , errors='coerce' )
data_polmeo4['Elevation (deg)'] = pd.to_numeric ( data_polmeo4['Elevation (deg)'] , errors='coerce' )
# Drop rows where 'Elevation (deg)' is NaN
data_polmeo1 = data_polmeo1.dropna ( subset = ['Elevation (deg)'] )
data_polmeo2 = data_polmeo2.dropna ( subset = ['Elevation (deg)'] )
data_polmeo3 = data_polmeo3.dropna ( subset = ['Elevation (deg)'] )
data_polmeo4 = data_polmeo4.dropna ( subset = ['Elevation (deg)'] )

max_elevation_polmeo1 = data_polmeo1['Elevation (deg)'].max ()
max_elevation_polmeo2 = data_polmeo2['Elevation (deg)'].max ()
max_elevation_polmeo3 = data_polmeo3['Elevation (deg)'].max ()
max_elevation_polmeo4 = data_polmeo4['Elevation (deg)'].max ()
# Find the row number where the maximum elevation value is located
max_elevation_row_polmeo1 = data_polmeo1[data_polmeo1['Elevation (deg)'] == max_elevation_polmeo1].index[0]
max_elevation_row_polmeo2 = data_polmeo2[data_polmeo2['Elevation (deg)'] == max_elevation_polmeo2].index[0]
max_elevation_row_polmeo3 = data_polmeo3[data_polmeo3['Elevation (deg)'] == max_elevation_polmeo3].index[0]
max_elevation_row_polmeo4 = data_polmeo4[data_polmeo4['Elevation (deg)'] == max_elevation_polmeo4].index[0]
print ( "Maximum Elevation POLMEO1:", max_elevation_polmeo1)
print ( "Row Number POLMEO1:", max_elevation_row_polmeo1 )
print ( "Maximum Elevation POLMEO2:", max_elevation_polmeo2)
print ( "Row Number POLMEO2:", max_elevation_row_polmeo2 )
print ( "Maximum Elevation POLMEO3:", max_elevation_polmeo3)
print ( "Row Number POLMEO3:", max_elevation_row_polmeo3 )
print ( "Maximum Elevation POLMEO4:", max_elevation_polmeo4)
print ( "Row Number POLMEO4:", max_elevation_row_polmeo4 )