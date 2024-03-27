import pandas as pd
import numpy as np

class DataPrepKit:
    def __init__(self):
        pass

    def read_data(self, file_path, file_format='csv'):
        if file_format == 'csv':
            return pd.read_csv(file_path)
        elif file_format == 'excel':
            return pd.read_excel(file_path)
        elif file_format == 'json':
            return pd.read_json(file_path)

    def generate_summary(self, data):
        summary = {}
        summary['mean'] = np.mean(data)
        summary['median'] = np.median(data)
        summary['max'] = np.max(data)
        summary['min'] = np.min(data)
        summary['most_frequent'] = pd.Series(data).mode()[0]
        return summary

    def handle_missing_values(self, data, strategy='mean'):
        if strategy == 'mean':
            return data.fillna(data.mean())
        elif strategy == 'median':
            return data.fillna(data.median())
        elif strategy == 'mode':
            return data.fillna(data.mode()[0])
        elif strategy == 'drop':
            return data.dropna()

    def encode_categorical_data(self, data):
        return pd.get_dummies(data)

# Usage Example:
data_prep = DataPrepKit()

# Reading Data
data = data_prep.read_data('data.csv')

# Generating Summary
summary = data_prep.generate_summary(data)

# Handling Missing Values
data_cleaned = data_prep.handle_missing_values(data)

# Encoding Categorical Data
encoded_data = data_prep.encode_categorical_data(data_cleaned)

print("Summary:", summary)
print("Cleaned Data:")
print(data_cleaned)
print("Encoded Data:")
print(encoded_data)



