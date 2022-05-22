import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title('My Parent New Healty Dinner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')   
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avacado Toast')



streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')

fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)













# creeate a fucntion
def get_fruityvice_data(this_friut_choice):
      fruityvice_response=requests.get("https://www.fruityvice.com/api/fruit/"+fruit_choice)
      fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
      return fruityvice_normalized
  
  

streamlit.header('Fruitvice Fuit Advice!')
try:
  fruit_choice=streamlit.text_input('what fruit you like information about ?','Kiwi')
  if not fruit_choice:
    streamlit.error("pelease enter a fruit to get information")
  else:
    back_from_function=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
      
except URLError as e:
  streamlit.error()

  
#dont run 
#streamlit.stop()

















streamlit.header("The Fruit Load List contains:")
#snowflake related funcs
def get_fruit_load_list():
      with my_cnx.cursor() as my_cur:
            my_cur.execute("select * from fruit_load_list")
            return  my_cur.fetchall()
#add a button to load the fruit 
if streamlit.button('Get Fruit Load List'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      my_data_rows=get_fruit_load_list()
      streamlit.dataframe(my_data_rows)
      
                  











  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
