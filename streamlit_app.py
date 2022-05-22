import streamlit

streamlit.title('My Parent New Healty Dinner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')   
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avacado Toast')



streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')

fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

#new section to display frity api resource 
streamlit.header('Fruitvice Fuit Advice!')
fruit_choice=streamlit.text_input('what fruit you like information about ?','Kiwi')
streamlit.write('the user entered' , fruit_choice)




import requests
fruityvice_response=requests.get("https://www.fruityvice.com/api/fruit/"+fruit_choice)


#take the json version and normalize it 
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
#output is the screen as a  table 
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The Fruit Load List contains:")
streamlit.dataframe(my_data_row)

import pandas
add_my_list=my_data_row
add_my_list=add_my_list.set_index('Fruitn')
fruits_selected_n=streamlit.multiselect("Pick some fruits:",list(add_my_list.index),['Avocado','Strawberries'])
fruits_to_show_n = add_my_list.loc[fruits_selected_n]

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
