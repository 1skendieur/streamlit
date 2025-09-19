import streamlit as st
import pandas as pd
import numpy as np
from numpy.random import default_rng as rng

st.title("Hellow world!")

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

df = rng(0).standard_normal((10, 1))

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

tab1.subheader("A tab with a chart")
tab1.line_chart(df)

tab2.subheader("A tab with the data")
tab2.write(df)
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')


title = st.text_input("Please write your name", "John John")
st.write("Your name is ", title)

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")


df = pd.DataFrame(
    rng(0).standard_normal((1000, 2)) / [50, 50] + [51.169392, 71.449074],
    columns=["lat", "lon"],
)

st.map(df)

func_name = st.selectbox(
    "function",
    ["sin", "cos", "tan"]
)
func_dict = {"sin": np.sin, "cos": np.cos, "tan": np.tan}

if st.checkbox("Show Line chart"):
    y = func_dict[func_name](x * t + x0)
    df = pd.DataFrame({
        f"{func_name}(x*t+x0)": y
    })
    st.line_chart(df)