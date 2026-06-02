import streamlit as st
from database import run_query

st.title('Dashboard Page')

st.write('Reataurants Filter& Data Table')

#===================================
#Load filter data
#===================================

location_query='''SELECT DISTINCT location
 FROM restaurants ORDER BY location;'''

cuisine_query='''SELECT DISTINCT cuisines
 FROM restaurants ORDER BY cuisines;'''

locations=run_query(location_query)
cuisines=run_query(cuisine_query)

#===================================
#sidebar filters
#===================================

st.sidebar.header('Filters')
selected_location=st.sidebar.selectbox('select location',
                    ['ALL']+locations['location'].dropna().tolist())

selected_online_order=st.sidebar.selectbox('Online Order',['ALL','YES','NO'])

selected_book_table=st.sidebar.selectbox('Booking Table',['ALL','YES','NO'])

min_rating=st.sidebar.slider('Minimum Rating',
                          min_value=0.0,
                          max_value=5.0,
                          value=3.0)

max_cost=st.sidebar.slider('maximum cost for two people',
                           min_value=100,
                           max_value=5000,
                           value=1000)

#===================================
#SQL Query
#===================================

query = f'''SELECT 
    name,
    location,
    cuisines,
    rate,
    approx_cost,
    online_order,
    book_table
    FROM restaurants
    WHERE rate >= {min_rating}
    AND approx_cost <= {max_cost}
   '''

if selected_location!='ALL':
    query+=f" AND location='{selected_location}'"

if selected_online_order!='ALL':
    query+=f" AND online_order='{selected_online_order}'"

if selected_book_table!='ALL':
    query+=f" AND book_table='{selected_book_table}'"

query+= "LIMIT 100"

#===================================
#Show Results
#===================================

df=run_query(query)
st.subheader('Filtered Restaurants')
st.dataframe(df)
