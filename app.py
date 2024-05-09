import streamlit as st 
import pandas as pd 
import numpy as np
from pycaret.classification import *
from pycaret.regression import *
import io
import seaborn as sns
import pandas.api.types as pd_types
from sklearn.preprocessing import LabelEncoder

st.header("Welcome, we are happy to see you in our website <3")

st.subheader("you will be able to get algorithims prediction accuracy by 3 steps...")

st.text("1- Upload CSV or Excel file")
st.text("2- Choose target feature")
st.text("3- Remove unimportant features")

st.subheader("Are you ready? Let's go")
st.divider()
file_upload = st.file_uploader("Upload CSV or Excel file", type="CSV")



if file_upload is not None:


    if file_upload.name.endswith(".csv"):
        st.success("Your data is added successfully...Great :)")
        st.subheader("This is your data")
        df = pd.read_csv(file_upload)
        st.dataframe(df)

    elif file_upload.name.endswith((".xlsx", ".xls")):
        st.success("Your data is added successfully...Great :)")
        st.subheader("This is your data")
        df = pd.read_excel(file_upload)
        st.dataframe(df)

    else:
        st.error("Invalid file type. Please upload a CSV or Excel file.")
    
    
    
    

    
    st.divider()
    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()
    str_columns = df.select_dtypes(include=["object"]).columns.tolist()

    st.subheader("Handle missing values for categorical columns")
    if str_columns:
        cat_impute_method = st.selectbox("Choose how to handle missing values in categorical columns",
        ["Mode", "Class-based (Fill with 'Unknown')"],
    )

        if cat_impute_method == "Mode":
            for col in str_columns:
                mode_value = df[col].mode()[0]  # Most frequent value
                df[col].fillna(mode_value, inplace=True)
            st.dataframe(df)    

        elif cat_impute_method == "Class-based (Fill with 'Unknown')":
            for col in str_columns:
                df[col].fillna("Unknown", inplace=True)  # Fill with a default class
            st.dataframe(df)        
        
    
    st.divider()
    

    #st.dataframe(df)
    st.subheader("Handle missing values for continuous columns")
    if numeric_columns:
        num_impute_method = st.selectbox(
            "Choose how to handle missing values in continuous columns",
            ["Mean", "Median", "Mode"],
        )

        if num_impute_method == "Mean":
            for col in numeric_columns:
                df[col].fillna(df[col].mean(), inplace=True)
            st.dataframe(df)
        elif num_impute_method == "Median":
            for col in numeric_columns:
                df[col].fillna(df[col].median(), inplace=True)
            st.dataframe(df)
        elif num_impute_method == "Mode":
            for col in numeric_columns:
                mode_value = df[col].mode()[0]
                df[col].fillna(mode_value, inplace=True)
            st.dataframe(df)
    # Display the DataFrame after handling missing values
    st.write("DataFrame after handling missing values:")
    st.dataframe(df)

    
    
    st.divider()


    st.subheader("Some EDA on your data:")
    st.write("Summary statistics:")
    st.dataframe(df.describe())
    
    st.dataframe(df.describe(include=['object','bool']))

    


    
    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()
    str_columns = df.select_dtypes(include=["object"]).columns.tolist()
    
    st.write("Here we will do scatter graph for your data. So, please select x, y below")
    
    if numeric_columns:
        selected_column_x = st.selectbox("Select x in the scatter graph", numeric_columns)
        
        selected_column_y = st.selectbox("Select y in the scatter graph", numeric_columns)

        
        st.scatter_chart(df,x= selected_column_x , y=selected_column_y)
    else:
        st.write("You choose non numric column")


    st.divider()




    st.subheader("Now you can choose columns to delete them: ")

    col = df.columns.tolist()

    select_del = st.multiselect("Select column to delete it, if you want :" , col)
    df = df.drop(columns= select_del)
    st.dataframe(df)

    
    st.divider()
    col_1 = df.columns
    numeric_columns_1 = df.select_dtypes(include=["number"]).columns.tolist()
  
    str_columns_1 = df.select_dtypes(include=["object"]).columns.tolist()



    st.subheader("Choose target feature to build the model")
    
    
    
    
    
    
    


    st.subheader("Regression")
    st.subheader("Classification")

    select_encode = st.radio("Please choose the type of encoding to catigorical columns:",
     ["Label Encoding", "One-Hot Encoding"])

    if select_encode == "Label Encoding":
        le = LabelEncoder()
        for col in str_columns_1:
            df[col] = le.fit_transform(df[col])
        
        st.dataframe(df)
    
    elif select_encode == "One-Hot Encoding":
        df = pd.get_dummies(df, columns= str_columns_1)
        st.dataframe(df)
            
    
    
    col_2 = df.columns
    numeric_columns_1 = df.select_dtypes(include=["number"]).columns.tolist()    
    str_columns_2 = df.select_dtypes(include=["object"]).columns.tolist()
    
    select_y = st.selectbox("choose y (target) from your columns", df.columns.tolist())
    st.divider()
    st.dataframe(df)
    
    
    


    
    type1= df[select_y].dtype
    
    if type1 == "object" :
        experiment = setup(df,target= select_y, categorical_features= str_columns_2)
        st.table(experiment.pull())
        best_model = compare_models()
        results = pull()
        st.table(results)
        predict_model(best_model, df)
        st.text(best_model)

    elif type1 in ("int64","float64"):
        
        s = setup(df, target = select_y, session_id = 123)
        st.table(s.pull())
        best = compare_models()
        results1 = pull()
        st.table(results1)
        predict_model(best, df)
        st.text(best)




    
    

    
    


    
else: 
    st.write("Please upload CSV or Excel file.")
