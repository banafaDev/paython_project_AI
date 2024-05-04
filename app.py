import streamlit as st 
import pandas as pd 
import numpy as np
from pycaret.classification import *
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
    
    #diabetes = get_data('diabetes')
    #predictions = predict_model(estimator=model,data=data)
    
    

    
    st.divider()


    df1 = df.dropna()
    st.subheader("This your Data after Handling missing values")
    st.dataframe(df1)
    st.divider()


    st.subheader("Some EDA on your data:")
    st.write("Summary statistics:")
    st.dataframe(df1.describe())
    
    st.dataframe(df1.describe(include=['object','bool']))

    


    numeric_columns = df1.select_dtypes(include=["number"]).columns.tolist()
    str_columns = df1.select_dtypes(include=["object"]).columns.tolist()

    
    st.write("Here we will do scatter graph for your data. So, please select x, y below")
    
    if numeric_columns:
        selected_column_x = st.selectbox("Select x in the scatter graph", numeric_columns)
        
        selected_column_y = st.selectbox("Select y in the scatter graph", numeric_columns)

        
        st.scatter_chart(df,x= selected_column_x , y=selected_column_y)
    else:
        st.write("You choose non numric column")


    st.divider()




    st.subheader("Now you can choose columns to delete them: ")

    col = df1.columns.tolist()

    select_del = st.multiselect("Select column to delete it :" , col)
    df2 = df1.drop(columns= select_del)
    st.dataframe(df2)

    
    st.divider()
    col_1 = df2.columns
    numeric_columns_1 = df2.select_dtypes(include=["number"]).columns.tolist()
  
    str_columns_1 = df2.select_dtypes(include=["object"]).columns.tolist()



    st.subheader("Choose x,y to build the model")
    st.write("*Note: you have to choose x,y from the same type.")
    
    select_x = st.selectbox("choose x from your columns", col_1)
    
    type_x = (df2[select_x].dtype)
    if type_x in ("float64", "complex128","int64"):
        select_y = st.selectbox("choose y from your columns", numeric_columns_1)
        st.subheader("Regression")
    elif type_x == "object":
        select_y = st.selectbox("choose y from your columns", str_columns_1)
        st.subheader("Classification")

        select_encode = st.radio("Please choose the type of encoding to catigorical columns:", ["Label Encoding", "One-Hot Encoding"])
        
        if select_encode == "Label Encoding":
            le = LabelEncoder()
            for col in str_columns_1:
                df2[col] = le.fit_transform(df2[col])
            
            st.dataframe(df2)
        
        elif select_encode == "One-Hot Encoding":
            pd.get_dummies(df2, columns= str_columns_1)
            st.dataframe(df2)
            
    else:
        st.write("Please choose int , float or string column")

        
    
    st.divider()
    
    

    target1 = st.selectbox("Please select your target feature:", col_1)

    experiment = setup(df2,target= target1, categorical_features= str_columns_1)

    best_model = compare_models()
    
    predict_model(best_model, df2)

    save_model(best_model, model_name='GR-model')

    load_model('GR-model')


    
    


    
else: 
    st.write("Please upload CSV or Excel file.")

#end ------------------------------------------------------------------------

    """pycaret capstone 
        1- data reading (Done)
        1- apply eda (Done)
        2- handling missing values (Done)
        3- remove cols (Done)
        4- choose x,y -> detect task type (classficatio or regression)(Done)
        5- catgorical data encoding. choose the user >> 1,0 or label (Done)
        6- pycaret 
        in streamlit app"""

