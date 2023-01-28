# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 14:32:00 2023

@author: lenovo
"""
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt




df = pd.read_csv("Billionaire.csv")
#clean the data
df["NetWorth"]= df['NetWorth'].apply(lambda x: float(x.replace('$','').replace('B','')))


#the highest rank of the person
#top_build = df[df["Rank"]== 1]
#print(top_build)

#QUESTION 01find count of billionaries by country
#count_check = df.groupby('Country')['Name'].count().sort_values(ascending= False).head(10)
#st.text(count_check)

#st.bar_chart(count_check)

#QUESTION 02find the most popular source of income
#count_check2 = df.groupby('Source')['Name'].count().sort_values(ascending= False).head(5)
#st.dataframe(count_check2)

#st.bar_chart(count_check2)
#QUESTION3GET THE COMMULATIVE WEALTH OF BILLIONARE BELONGING TO US"""


#interactivity (country wise billionaries kw dekh sakai)
#all_countries = df["Country"].unique()
#selection = st.selectbox("Select Country", all_countries)

#subset = df[df["Country"] == selection]

#st.dataframe(subset)

all_countries = sorted(df["Country"].unique())

col1, col2 = st.columns(2)

#coloumn 1
#display on streamlit
selected_country = col1.selectbox("select your country", all_countries)
#subset on selected country
subset_country = df[df["Country"] == selected_country]


#get unique sources from selected country
sources = sorted(subset_country["Source"].unique())
#display multi select option on source
selected_source = col1.multiselect("select source of income", sources)
#subset on selected source
subset_source = subset_country[subset_country["Source"].isin(selected_source)]


#coloumn 2
header_string = '{} - Billionaries'.format(selected_country)
#header_string = selected_country + ' -Billionaries'
col2.header(header_string)
col2.dataframe(subset_country)
col2.header("Source Wise Info")
col2.dataframe(subset_source)

