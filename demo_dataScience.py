import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# add title
st.title('Data Analysis Applicatiom')
st.subheader('This is my simple data analysis application created by Chandrahaas...')

# creating a dropdown list to choose the dataset
datasets_column = ['iris','titanic','tips','diamonds']
selected_dataset = st.selectbox('Select the datasets',datasets_column)

# load the specific dataset
if selected_dataset == 'iris':
    df = sns.load_dataset('iris')
elif selected_dataset == 'titanic':
    df = sns.load_dataset('titanic')
elif selected_dataset == 'tips':
    df = sns.load_dataset('tips')
elif selected_dataset == 'diamonds':
    df = sns.load_dataset('diamonds')

# button to upload a custome dataset: this is for when ever the end user need to upload any custome dataset ( csv, xlsx, etc...) for prediction
upload_file = st.file_uploader('Choose a file',type=['csv','xlsx'])   # you can also add specific file list like this.

if upload_file is not None:
    # process the uploaded file
    if upload_file.name.endswith('csv'):
        df = pd.read_csv(upload_file)
    elif upload_file.name.endswith('xlsx'):
        df = pd.read_excel(upload_file)

# display the dataset
st.write(df)

# display the number of rows and columns in selected dataset
st.write('Number of Rows :',df.shape[0])
st.write('Number of Columns :',df.shape[1])

# display the column names based on selected data
st.write("Column Names and Data type's :",df.dtypes)

# print the null values if those are > 0
if df.isnull().sum().sum() > 0:
    st.write('Null values are :',df.isnull().sum().sort_values(ascending=False))  # printing the null values in ascending order
else:
    st.write('No Null values ...')

# display the summary statistics of seleected dataset
st.write('Summary Statistics is :',df.describe())

# Select the specific columns forX and y axis from the dataset and also select the plot type to plot the data
x_axis = st.selectbox('Select X-axis',df.columns)
y_axis = st.selectbox('Select Y-axis',df.columns)
plot_type = st.selectbox('Select plot type',['line','scatter','bar','box','kde']) # you can keep : "hist" plot too.

# plot the data
if plot_type == 'line':
    st.line_chart(df[[x_axis,y_axis]])
elif plot_type == 'scatter':
    st.scatter_chart(df[[x_axis,y_axis]])
elif plot_type == 'bar':
    st.bar_chart(df[[x_axis,y_axis]])
# elif plot_type == 'hist':
#     df[x_axis].plot(kind='hist')
#     st.pyplot()
elif plot_type == 'box':
    df[[x_axis,y_axis]].plot(kind='box')
    st.pyplot()
elif plot_type == 'kde':
    df[[x_axis,y_axis]].plot(kind='kde')
    st.pyplot()

# creating a pairplot for each dataset
st.subheader('PairPlot')
pair_plot = sns.pairplot(df)
st.pyplot(pair_plot)

# creating a pairplot based upon the featres in the dataset
st.subheader('PairPlot based upon the Columns')
hue_columns = st.selectbox('Select the column to be used as hue',df.columns)  # hue, define the representation the columns in color format
pair_plot2 = sns.pairplot(df, hue=hue_columns)
st.pyplot(pair_plot2)