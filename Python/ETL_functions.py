import os
import csv
import pandas as pd

# Path to collect data from the Resources folder
greenhouse_file = "../Resources/GreenhouseEmissions.csv"
infrastructure_file = "../Resources/InfrastructureDevelopment.csv"

# Define the function and have it accept the 'infrastructure_file' and 'greenhouse_file' as its parameters
def extract(file):
    
     #Read CSV files 
     df = pd.read_csv(file)
     print("Converting CSV to DataFrame for"+file+" successful")
     return df
    
 def transformations(df):
     greenhouse_df = extract(greenhouse_file)
     infrastructure_df = extract(infrastructure_file)
     # set index for dataframes
     df.set_index("id_no", inplace=True)
     # remove duplicates
     df.drop_duplicates("id_no", inplace=True)
     # drop null values
     df.dropna()
     return df

 def clean_columns_greenhouse(greenhouse_df, greenhouse_columns):
     greenhouse_df = transformations(df)
     greenhouse_columns = ["GHG ID No. / No d'identification de GES", "Reference Year / Année de référence", "Facility City or District or Municipality / Ville ou District ou Municipalité de l'installation", "Facility Province or Territory / Province ou territoire de l'installation", "Latitude", "Longitude", "Total Emissions (tonnes CO2e) / Émissions totales (tonnes éq. CO2)"]
     greenhouse_transformed= greenhouse_df[greenhouse_columns].copy()
     greenhouse_transformed = greenhouse_transformed.rename(columns={"GHG ID No. / No d'identification de GES": "id_no",
                                                          "Reference Year / Année de référence": "year",
                                                          "Facility City or District or Municipality / Ville ou District ou Municipalité de l'installation": "area",
                                                            "Facility Province or Territory / Province ou territoire de l'installation":"province",
                                                               "Total Emissions (tonnes CO2e) / Émissions totales (tonnes éq. CO2)":"total_emissions",
                                                               "Latitude": "latitude",
                                                               "Longitude": "longitude"})
    greenhouse_transformed_fil = greenhouse_transformed.loc[greenhouse_transformed["province"] == "Ontario"]
    ghg = ghg.round({'latitude': 2, 'longitude': 2, 'total_emissions': 2})
    return ghg
    
 def clean_columns_infrastructure(infrastructure_df, infratructure_columns):
     infrastructure_df = transformations(df)
     infratructure_columns = ["_id", "Project", "Status", "Result", "Area", "Estimated Total Budget", "Latitude", "Longitude"]
     infrastructure_transformed = infrastructure_df[infratructure_columns].copy()

     infrastructure_transformed = infrastructure_transformed.rename(columns={"_id": "id_no",
                                                                       "Estimated Total Budget": "total_budget",
                                                                       "Area": "area",
                                                                       "Project": "project",
                                                                       "Status": "status",
                                                                       "Result": "result",
                                                                       "Latitude": "latitude",
                                                                        "Longitude": "longitude"})

    infrastructure_transformed['province'] = 'Ontario'

    inf = inf.round({'latitude': 2, 'longitude': 2})

     return inf

db_engines = { ... }

def load():
    ghg = clean_columns_greenhouse(ghg)
    inf = clean_columns_infrastructure(inf)


db_engines = { ... } # Needs to be configured

# def etl():
# 	# Extract
# 	film_df = extract_table_to_df("film", db_engines["store"])
# 	# Transform
# 	film_df = split_columns_transform(film_df, "rental_rate", ".", ["_dollar", "_cents"])
# 	# Load
# 	load_df_into_dwh(film_df, "film", "store", db_engines["dwh"])

# # def clean_df(dataframe, columns_to_keep):\
# #     clean_columns_dataframe = datagrame[columns_to_keep].copy()
# #     return clean_columns_dataframe

# # clean_df(infrastructure)

# # def join_dataframes(dataframe1, dataframe2):
# #     dataframe1_cleaned= clean_df(dataframe1)
#     #code to join the dataframes andr eturn aj oined dataframe

# # greenhouse_df = extract(greenhouse_file)

# # infrastructure_df = extract(infrastructure_file)

# # x = clean(greenhouse_df)
# # y = clean(theotherone)
    
# # joined_dataframe = join_dataframes(x,y)


    
    
    
    
    
    
    
    