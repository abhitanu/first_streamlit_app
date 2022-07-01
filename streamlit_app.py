import streamlit
import pandas as pd
import requests as rr
import snowflake.connector

streamlit.title('My parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry oatmeal')
streamlit.text('🥗 Kale,Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard boiled range free brown Eggs')
streamlit.text('🐔 Hard boiled range free brown Eggs')
streamlit.text('🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

myFruitList = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_selected = streamlit.multiselect("Pick from list", list(myFruitList.Fruit),['Avocado','Strawberries'])
streamlit.dataframe(fruits_selected)

## Lets get data via API
streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruitVice_response = rr.get("https://fruityvice.com/api/fruit/"+fruit_choice)
df_normalized = pd.json_normalize(fruitVice_response.json())

streamlit.dataframe(df_normalized) 


