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
    


def clean_df(dataframe, columns_to_keep):\
    clean_columns_dataframe = datagrame[columns_to_keep].copy()
    return clean_columns_dataframe

clean_df(infrastructure)

def join_dataframes(dataframe1, dataframe2):
    dataframe1_cleaned= clean_df(dataframe1)
    #code to join the dataframes andr eturn aj oined dataframe





greenhouse_df = extract(greenhouse_file)

infrastructure_df = extract(infrastructure_file)

x = clean(greenhouse_df)
y = clean(theotherone)
    
joined_dataframe = join_dataframes(x,y)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    