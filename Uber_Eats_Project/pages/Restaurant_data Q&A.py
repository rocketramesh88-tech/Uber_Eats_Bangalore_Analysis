import streamlit as st
from database import run_query

st.title("Restaurant Data-Based Questions & Answers")

# =========================================
# Question 1
# =========================================

st.header("1. Highest Rated Locations")

query1 = """
SELECT
    location,
    ROUND(AVG(rate),2) AS avg_rating
FROM restaurants
GROUP BY location
ORDER BY avg_rating DESC
LIMIT 10;
"""

df1 = run_query(query1)

st.dataframe(df1)

# =========================================
# Question 2
# =========================================

st.header("2. Restaurant Saturation by Location")

query2 = """
SELECT
    location,
    COUNT(*) AS total_restaurants
FROM restaurants
GROUP BY location
ORDER BY total_restaurants DESC
LIMIT 10;
"""

df2 = run_query(query2)

st.dataframe(df2)

# =========================================
# Question 3
# =========================================

st.header("3. Online Ordering vs Ratings")

query3 = """
SELECT
    online_order,
    ROUND(AVG(rate),2) AS avg_rating
FROM restaurants
GROUP BY online_order;
"""

df3 = run_query(query3)

st.dataframe(df3)

# =========================================
# Question 4
# =========================================

st.header("4. Table Booking vs Ratings")

query4 = """
SELECT
    book_table,
    ROUND(AVG(rate),2) AS avg_rating
FROM restaurants
GROUP BY book_table;
"""

df4 = run_query(query4)

st.dataframe(df4)

# =========================================
# Question 5
# =========================================

st.header("5. Best Price Segment")

query5 = """
SELECT
CASE
    WHEN approx_cost < 400 THEN 'Low Price'
    WHEN approx_cost BETWEEN 400 AND 800 THEN 'Medium Price'
    ELSE 'Premium'
END AS price_segment,

ROUND(AVG(rate),2) AS avg_rating

FROM restaurants

GROUP BY price_segment;
"""

df5 = run_query(query5)

st.dataframe(df5)

# =========================================
# Question 6
# =========================================

st.header("6. Most Common Cuisines")

query6 = """
SELECT
    cuisines,
    COUNT(*) AS total_restaurants
FROM restaurants
GROUP BY cuisines
ORDER BY total_restaurants DESC
LIMIT 10;
"""

df6 = run_query(query6)

st.dataframe(df6)

# =========================================
# Question 7
# =========================================

st.header("7. Highest Rated Cuisines")

query7 = """
SELECT
    cuisines,
    ROUND(AVG(rate),2) AS avg_rating
FROM restaurants
GROUP BY cuisines
ORDER BY avg_rating DESC
LIMIT 10;
"""

df7 = run_query(query7)

st.dataframe(df7)

# =========================================
# Question 8
# =========================================

st.header("8. Cost vs Rating")

query8 = """
SELECT
    approx_cost,
    ROUND(AVG(rate),2) AS avg_rating
FROM restaurants
GROUP BY approx_cost
ORDER BY approx_cost;
"""

df8 = run_query(query8)

st.dataframe(df8)

# =========================================
# Question 9
# =========================================

st.header("9. Top Restaurants by Votes")

query9 = """
SELECT
    name,
    votes,
    rate
FROM restaurants
ORDER BY votes DESC
LIMIT 10;
"""

df9 = run_query(query9)

st.dataframe(df9)

# =========================================
# Question 10
# =========================================

st.header("10. Premium Restaurants")

query10 = """
SELECT
    name,
    location,
    cuisines,
    approx_cost,
    rate
FROM restaurants
WHERE approx_cost > 1500
ORDER BY rate DESC
LIMIT 10;
"""

df10 = run_query(query10)

st.dataframe(df10)