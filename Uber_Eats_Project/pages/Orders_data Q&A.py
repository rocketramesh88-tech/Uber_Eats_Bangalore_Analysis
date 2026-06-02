import streamlit as st
from database import run_query

st.title("Orders Data- Based Question & Answers")

# ====================================
# Q1 Total Orders
# ====================================

st.header("1. Total Orders")

query_1 = """
SELECT COUNT(*) AS total_orders
FROM orders;
"""

qus1 = run_query(query_1)

st.dataframe(qus1)

# ====================================
# Q2 Average Order Value
# ====================================

st.header("2. Average Order Value")

query_2 = """
SELECT ROUND(AVG(order_value),2) AS average_order_value
FROM orders;
"""

qus2 = run_query(query_2)

st.dataframe(qus2)

# ====================================
# Q3 Highest Order Value
# ====================================

st.header("3. Highest Order Value")

query_3 = """
SELECT restaurant_name, order_value
FROM orders
ORDER BY order_value DESC
LIMIT 5;
"""

qus3 = run_query(query_3)

st.dataframe(qus3)

# ====================================
# Q4 Payment Method Analysis
# ====================================

st.header("4. Payment Method Usage")

query_4 = """
SELECT payment_method,
COUNT(*) AS total_orders
FROM orders
GROUP BY payment_method
ORDER BY total_orders DESC;
"""

qus4 = run_query(query_4)

st.dataframe(qus4)

# ====================================
# Q5 Discount Usage
# ====================================

st.header("5. Discount Usage")

query_5 = """
SELECT discount_used,
COUNT(*) AS total_orders
FROM orders
GROUP BY discount_used;
"""

qus5 = run_query(query_5)

st.dataframe(qus5)