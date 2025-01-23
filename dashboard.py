import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the Dashboard
st.title("My Streamlit Dashboard")

# Sidebar for Navigation
st.sidebar.title("Sidebar")
option = st.sidebar.selectbox("Select an option:", ["Home", "Data Analysis", "Visualization"])

# Generate Random Data
data = pd.DataFrame({
    "Category": np.random.choice(["A", "B", "C", "D"], size=100),
    "Value": np.random.randn(100)
})

# Display the first few rows of the data
if option == "Data Analysis":
    st.write("Sample Data", data.head())

# Create a bar plot
if option == "Visualization":
    fig, ax = plt.subplots()
    sns.countplot(x='Category', data=data, ax=ax)
    ax.set_title('Category Count')
    st.pyplot(fig)

# Filter Data with Slider
if option == "Data Analysis":
    min_value = st.slider('Select the minimum value for data filtering', -2.0, 2.0, -1.0)
    filtered_data = data[data["Value"] > min_value]
    st.write("Filtered Data", filtered_data)
