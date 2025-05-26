import streamlit as st
import pandas as pd 
import sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

'''The **Iris dataset** is a small, classic dataset in machine learning that contains **150 records of iris flowers**, each described by **4 features** (sepal length, sepal width, petal length, petal width) and classified into **3 species**: *setosa*, *versicolor*, and *virginica*.'''

def load_data():
    iris = load_iris()
    data=load_iris(as_frame=True).frame
    return data, iris.target_names

data,target_names=load_data()
print(target_names)
model=RandomForestClassifier()
model.fit(data.iloc[:,:-1],data['target'])

st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider("Sepal length", float(data['sepal length (cm)'].min()), float(data['sepal length (cm)'].max()))
sepal_width = st.sidebar.slider("Sepal width", float(data['sepal width (cm)'].min()), float(data['sepal width (cm)'].max()))
petal_length = st.sidebar.slider("Petal length", float(data['petal length (cm)'].min()), float(data['petal length (cm)'].max()))
petal_width = st.sidebar.slider("Petal width", float(data['petal width (cm)'].min()), float(data['petal width (cm)'].max()))

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

## PRediction
prediction = model.predict(input_data)
print(prediction)
predicted_species = target_names[prediction[0]]

# st.write("Prediction")
st.write(f"The predicted species is: {predicted_species}")