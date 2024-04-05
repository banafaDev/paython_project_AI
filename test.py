import pandas as pd
import numpy as np
class DataPrepKit:
    
    def __init__(self):
        pass
        
    
    

    def read_data(self, *file_path):
        file_path = input("Enter file path: ")
        print("")
        print("")
        print("--------- Data Frame ---------")
        if 'csv' in file_path:
            return pd.read_csv(file_path)
        elif 'excel' in file_path:
            return pd.read_excel(file_path)
        elif 'json' in file_path:
            return pd.read_json(file_path)

    
    def generate_summary(self, df):
        print("")
        print("")
        print("----- Stats -----")
        stats = df.describe()
        return stats
    

    def handle_missing_values(self, df):
        print("")
        print("")
        print("----- Data Cleand -----")
        return df.dropna()
       
       
    def encode_categorical_data(self, data):
        print("")
        print("")
        print("----- Encoded Data -----")
        return pd.get_dummies(data)
        
        

        
# Usage Example:
data_prep = DataPrepKit()

# Reading Data
data = data_prep.read_data()
df=pd.DataFrame(data)
print(df)

# Generating Summary
summary = data_prep.generate_summary(df)
print(summary)


 #Handling Missing Values
data_cleaned = data_prep.handle_missing_values(df)
print(data_cleaned)


# Encoding Categorical Data
encoded_data = data_prep.encode_categorical_data(data_cleaned)
print(encoded_data)



