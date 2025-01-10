from logging import exception

import pandas as pd
from sklearn.datasets import load_iris
import numpy as np
import os
def read_parquet(file):
    try:
        table = pa.read_table(file)
        return table
    except:
        print("file {} not found...!".format(file))
        return "error"

def read_csv(file):
    try:

        csvfile = pd.read_csv(file)
        print("reading file")
        print(csvfile.values)
        print(csvfile.shape[0])
        csvfile.drop_duplicates(keep =False, inplace=True)
        print(csvfile.values)
        print(csvfile.shape[0])
        return csvfile
    except Exception as e:
        print(e)


file_name=os.path.dirname(__file__)
final_path=os.path.join(file_name,'..','Dataset','dota_kaggle','dota2_versions.csv')
final_path2=os.path.abspath(final_path)
#file_parquet = "C:\\Users\\harir\\PycharmProjects\\PythonProject\\git\\Python\\Dataset\\dota_kaggle\\dota2_matches.parquet"
file_csv = final_path2

#table = read_parquet(file_parquet)
csv_df = read_csv(file_csv)


