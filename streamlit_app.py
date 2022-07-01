import streamlit
import pandas as pd
import requests as rr
import snowflake.connector
from urllib.error import URLError

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

try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
  
    if not fruit_choice:
      streamlit.error("Please select fruit to get information")
    else:
      fruitVice_response = rr.get("https://fruityvice.com/api/fruit/"+fruit_choice)
      df_normalized = pd.json_normalize(fruitVice_response.json())
      streamlit.dataframe(df_normalized) 
    
    except URLError as e:
      streamlit.error()
    
streamlit.stop()
##Lets connect to SnowFlake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.header("Fruit Load list from Snowflake:")
streamlit.dataframe(my_data_row)

fruit_choice_snowflake = streamlit.text_input('What fruit would you like to add','jackfruit')
streamlit.write('Thanks for adding ', fruit_choice_snowflake)

my_cur.execute("insert into public.FRUIT_LOAD_LIST values ('from Steamlit')")
