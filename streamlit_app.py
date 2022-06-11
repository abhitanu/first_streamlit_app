import streamlit
import pandas as pd

streamlit.title('My parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry oatmeal')
streamlit.text('🥗 Kale,Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard boiled range free brown Eggs')
streamlit.text('🐔 Hard boiled range free brown Eggs')
streamlit.text('🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

myFruitList = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
mFruitList = myFruitList.set_index('Fruit')

#streamlit.multiselect("Pick from list", list(myFruitList.index))
streamlit.dataframe(myFruitList)
#streamlit.dataframe(myFruitList)


