import streamlit as st
import time
import psycopg2
from psycopg2 import OperationalError
import logging

# configure logging
logging.basicConfig(level=logging.INFO)

# defining connection parameters
DB_HOST = "postgres"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "passw0rd"    
DB_PORT = "5432"

def fetch_data():
    try:
        conn = psycopg2.connect(host=DB_HOST,
                                dbname=DB_NAME,
                                user=DB_USER,
                                password=DB_PASSWORD,
                                port=DB_PORT)
        curr = conn.cursor()
        curr.execute("SELECT * FROM sentences") 
        rows = curr.fetchall()
        # conn.commit()
        curr.close()
        conn.close()
        return rows
    except OperationalError as e:
        st.err(f"OperationalError : {e}")
        return []
    except Exception as e:
        return []
    
def main():
    st.title("Sentence Data Dashboard")
    st.write("Here is your sentiment analysis on sentence data:")

    unique_id = set()

    while True:
        data = fetch_data()
        if data:
            for row in data:
                id = row[0]
                if id in unique_id:
                    continue
                st.write(row)
                unique_id.add(id)
        else:
            st.write("Error in fetching data from Postgres database")
        time.sleep(5)
                    

if __name__ == "__main__":
    main()

# import streamlit as st
# import psycopg2

# def fetch_data():
#     conn = psycopg2.connect(
#         host="postgres",
#         port="5432",
#         dbname="postgres",
#         user="postgres",
#         password="passw0rd"
#     )
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM sentences;")
#     rows = cur.fetchall()
#     conn.close()
#     return rows

# st.title("PostgreSQL Data Viewer")

# if st.button("Load Data"):
#     data = fetch_data()
#     if data:
#         st.write(data)
#     else:
#         st.write("Error in fetching data from Postgres database")
# else:
#     st.write("Click the button to load data.")