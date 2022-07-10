This readme file was generated on 2022-06-24 by Lorenza Gilardi 


##### GENERAL INFORMATION ##### 

Dataset of containing daily aggregates of several environmental variables (meterological and atmoshperic composition)
aggregated at ZIP-code (German PLZ) level for the Nürnberg metropolitan region.


Author/Principal Investigator Information

Name: Lorenza Gilardi

ORCID: https://orcid.org/0000-0003-4472-8530

Institution: German Aerospace Center (DLR)

Email: lorenza.gilardi@dlr.de



Author/Associate or Co-investigator Information

Name: Thilo Erbertseder

ORCID:  https://orcid.org/0000-0003-4888-1065 

Institution: German Aerospace Center (DLR)

Email: thilo.erbertseder@dlr.de




Date of data collection: 2020-01-01 to 2020-12-31 (some datasets to 2021-12-31)


Geographic location of data collection: Nürnberg metropolitan region, Germany




##### SHARING/ACCESS INFORMATION ##### 


Licenses/restrictions placed on the data: 




##### DATA & FILE OVERVIEW ##### 


File List: <list all files (or folders, as appropriate for dataset organization) contained in the dataset, with a brief description>

	-> "Nuerberg_MR_plz.geojson"	Contains the polygons and geometry information of the ZIP-code areas used for the aggregation
	
	-> "Nuerberg_metrop_plz_METEO"	Folder containing all data regarding meterological variables

		- > "2mT_df_max_daily_2020_Nuerberg.csv"		CSV file containing daily MAXIMUM TEMPERATURE values for each ZIP-code area in the year 2020 [K]
		- > "2mT_df_max_daily_2020_Nuerberg.csv"		CSV file containing daily MEAN TEMPERATURE values for each ZIP-code area in the year 2020 [K]
		- > "Tot_prec_daily_df_2020_Nuerberg.csv"		CSV file containing daily TOTAL PRECIPITATION values for each ZIP-code area in the year 2020 [m]
		- > "Nuerberg_metrop_plz_tot_prec_mean_2020.shp"	Shapefile containing daily TOTAL PRECIPITATION values for each ZIP-code area in the year 2020 [m] merged with geographical references 


	-> "Nuerberg_metrop_plz_POLL"	Folder containing all data regarding atmospheric composition (pollutants concentrations)

		- > "NO2_daily_max_df_2020_Nuerberg.csv"		CSV file containing daily MAXIMUM CONCENTRATION values of NO2 for each ZIP-code area in the year 2020 [µg/m3]
		- > "NO2_daily_mean_df_2020_Nuerberg.csv"		CSV file containing daily MEAN CONCENTRATION values od NO2 for each ZIP-code area in the year 2020 [µg/m3]
		- > "NO2_daily_std_df_2020_Nuerberg.csv"		CSV file containing daily STANDARD DEVIATION OF CONCENTRATION values od NO2 for each ZIP-code area in the year 2020 [µg/m3]
		- > "PM2_5_daily_max_df_2020_Nuerberg.csv"		CSV file containing daily MAXIMUM CONCENTRATION values of PM2.5 for each ZIP-code area in the year 2020 [µg/m3]
		- > "PM2_5_daily_mean_df_2020_Nuerberg.csv"		CSV file containing daily MEAN CONCENTRATION values od PM2.5 for each ZIP-code area in the year 2020 [µg/m3]
		- > "PM2_5_daily_std_df_2020_Nuerberg.csv"		CSV file containing daily STANDARD DEVIATION OF CONCENTRATION values od PM2.5 for each ZIP-code area in the year 2020 [µg/m3]
		- > "PM10_daily_max_df_2020_Nuerberg.csv"		CSV file containing daily MAXIMUM CONCENTRATION values of PM10 for each ZIP-code area in the year 2020 [µg/m3]
		- > "PM10_daily_mean_df_2020_Nuerberg.csv"		CSV file containing daily MEAN CONCENTRATION values od PM10 for each ZIP-code area in the year 2020 [µg/m3]
		- > "PM10_daily_std_df_2020_Nuerberg.csv"		CSV file containing daily STANDARD DEVIATION OF CONCENTRATION values od PM10 for each ZIP-code area in the year 2020 [µg/m3]
		- > "SO2_daily_max_df_2020_Nuerberg.csv"		CSV file containing daily MAXIMUM CONCENTRATION values of SO2 for each ZIP-code area in the year 2020 [µg/m3]
		- > "SO2_daily_mean_df_2020_Nuerberg.csv"		CSV file containing daily MEAN CONCENTRATION values od SO2 for each ZIP-code area in the year 2020 [µg/m3]
		- > "SO2_daily_std_df_2020_Nuerberg.csv"		CSV file containing daily STANDARD DEVIATION OF CONCENTRATION values od SO2 for each ZIP-code area in the year 2020 [µg/m3]
		- > "O3_daily_max_df_2020_Nuerberg.csv"			CSV file containing daily MAXIMUM CONCENTRATION values of O3 for each ZIP-code area in the year 2020 [µg/m3]
		- > "O3_daily_mean_df_2020_Nuerberg.csv"		CSV file containing daily MEAN CONCENTRATION values od O3 for each ZIP-code area in the year 2020 [µg/m3]
		- > "O3_daily_std_df_2020_Nuerberg.csv"			CSV file containing daily STANDARD DEVIATION OF CONCENTRATION values od O3 for each ZIP-code area in the year 2020 [µg/m3]

        ->  "ARI_daily_df_2020_Nuernberg.csv"				CSV file containing daily aggregate health risk increase from air pollution (O3, NO2, PM2.5, PM10 and SO2). Relative Values [0,1] (*100 -> %)


File dependencies: the *.csv files can be merged to the "Nuerberg_MR_plz.geojson", containing geographical information, by means of the keys in column "plz", representing the ZIP-codes (German PLZ)


##### METHODOLOGICAL INFORMATION ##### 


Description of methods used for collection/generation of data: 

	- Temperature of 2 meters above surface and total precipitation data are obtained from Climate Data Store of ECMWF, ERA5 land dataset: https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=overview

		- Native temporal resolution: 1h
		- Native spatial resolution: 0.1°N, 0.1°W

	- Pollution concentration data are obtained from POLYPHEMUS/DLR model: E. Khorsandi, F. Baier, T. Erbertseder, M. Bittner, "Air quality monitoring and simulation on urban scale over Munich," 
		Proc. SPIE 10793, #Remote Sensing Technologies and Applications in Urban Environments III, 1079303 (26 October 2018); doi: 10.1117/12.2503969
		
		- Native temporal resolution: 1h
		- Native spatial resolution: 0.125°N, 0.0625°W 

        - Aggregate health risk increase from air pollution (ARI) is derived from the pollution concentration data above: Erbertseder, Thilo; Mittelstädt, Lisa; Gilardi, Lorenza; Traidl-Hoffmann, Claudia; Hachinger, Stephan and Bittner, Michael. (2021). Bioklimatisches Informationssystem Bayern: ein Service der UFS (Schlussbericht zum Forschungsvorhaben)." 
	        The publication can be found here: https://www.researchgate.net/publication/356597905_Bioklimatisches_Informationssystem_Bayern_ein_Service_der_UFS_Schlussbericht_zum_Forschungsvorhaben 



Methods for processing the data: the data were processed with Python v3.7. Utilized packages: pandas, numpy, geopandas, xarray, collections, salem
Some examples:
	
	# Import necessary packages in python
	import pandas as pd
	import numpy as np
	import geopandas as gpd

	# Open csv file as dataframe
	path_in = '' define input path
	df_poll= pd.read_csv(f'{path_it}\PM2_5_daily_max_df_2020_Nuerberg.csv', dtype={'plz': str}, index_col= 0)

	# Select specific plz
	plz = '07366' # PLZ of interest
	df_poll[df_poll['plz'] == '07366']

	# Column names to datetime format ( excluding 'plz' column)
	time = pd.to_datetime(df_poll.columns[1:])
	
	# Read geojson file with geographical information
	shdf = gpd.read_file(f'{path_in}\Nuerberg_MR_plz.geojson')	


Instrument- or software-specific information needed to interpret the data: Suggested packages: pandas, numpy, geopandas




DATA-SPECIFIC INFORMATION FOR: all .csv files in "Nuerberg_metrop_plz_METEO" and "Nuerberg_metrop_plz_POLL" 

	- 'plz' = unique identifier for each ZIP-code (PLZ) area
	- Any other column present a column name in the format 'YYYYMMDD' that corresponds to the day-of year. 
	- Each column but 'plz' column reports the daily aggregate of the considered variable. See measure unit in section DATA & FILE OVERVIEW 


DATA-SPECIFIC INFORMATION FOR: "Nuerberg_MR_plz.geojson" 

	- 'einwohner' : 	Number of inhabitants
	-  'note' : 		PLZ + location name
	- 'NUTS_ID': 		Identification code of the NUTS3 (German Landkreis) region where the PLZ area is located
	- 'NUTS_NAME': 		Name of the NUTS3 area (German Landkreis)
	- 'geometry' : 		Multiplygon geometries


Missing data codes:  nan



