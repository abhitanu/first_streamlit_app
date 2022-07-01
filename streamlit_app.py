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


def get_fruitvice_data (this_fruit_choice):
    fruitVice_response = rr.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
    df_normalized = pd.json_normalize(fruitVice_response.json())
    #streamlit.dataframe(df_normalized) 
    return df_normalized

try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
  
    if not fruit_choice:
      streamlit.error("Please select fruit to get information")
    else:
        back_from_function = get_fruitvice_data(fruit_choice)
        streamlit.dataframe(back_from_function) 
    
except URLError as e:
    streamlit.error()
    
##Lets connect to SnowFlake
def get_fruit_load_list():
    with my_cnx as my_cur:
        my_cur = my_cnx.cursor()
        my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
        return my_cur.fetchall()
    
# Add button to add a fruit
if streamlit.button('What fruit would you like information about?'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    df = get_fruit_load_list()
    streamlit.dataframe(df)
    
#streamlit.stop()    

add_my_fruit = streamlit.text_input('What fruit would you like to add','jackfruit')

def add_row_snowflake(new_fruit):
    with my_cnx as my_cur:
        my_cur = my_cnx.cursor()
        my_cur.execute("insert into public.FRUIT_LOAD_LIST values ('" + new_fruit +"'))
        streamlit.write('Thanks for adding ', new_fruit)        
                       
if streamlit.button('Add Fruit to the database'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    message_from_function = add_row_snowflake(add_my_fruit)
    
#my_cur.execute("insert into public.FRUIT_LOAD_LIST values ('from Steamlit')")
