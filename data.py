import streamlit as st
import pandas as pd
import numpy as np

a = [1,2,3,4,5,6,7,8]
n = np.array(a)
np = n.reshape((2,4))

dic = {
    "name" : ["Nitu" ,"Yadav"],
    "age" : [21],
    "City" : [ "New Delhi"]
}

data = pd.read_csv(".\data\\Salary_Data.csv")  # Double backward slash
print(data)


