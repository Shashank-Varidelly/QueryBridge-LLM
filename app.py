from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import pandas as pd
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

DB_FILE = "STUDENT.db"

# Initialize database and table
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    
    # Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS STUDENT (
            NAME TEXT,
            CLASS TEXT,
            SECTION TEXT
        )
    """)
    
    # Insert sample data if table empty
    cur.execute("SELECT COUNT(*) FROM STUDENT")
    if cur.fetchone()[0] == 0:
        sample_data = [
            ('Krish', 'Data Science', 'A'),
            ('Darius', 'Data Science', 'B'),
            ('Sudhanshu', 'DevOps', 'C'),
            ('Vikash', 'Data Science', 'C')
        ]
        cur.executemany("INSERT INTO STUDENT VALUES (?, ?, ?)", sample_data)
    
    conn.commit()
    conn.close()

# Generate SQL from AI
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('models/gemini-2.5-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Execute SQL safely with dynamic column handling
def read_sql_query(sql):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
        # Get column names from cursor description
        col_names = [desc[0] for desc in cur.description] if cur.description else []
        return rows, col_names
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return [], []
    finally:
        conn.close()

# Gemini prompt for generating SQL
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The database is STUDENT with columns NAME, CLASS, SECTION.
    
    - Example 1: How many records are present?
      SQL: SELECT COUNT(*) FROM STUDENT;
    
    - Example 2: Get all students in Data Science class
      SQL: SELECT * FROM STUDENT WHERE CLASS="Data Science";
    
    Only provide valid SQL code. Quote string values, do not include ``` or extra text.
    """
]

# Initialize database
init_db()

# Streamlit app
st.set_page_config(page_title="SQL Gemini App")
st.header("Gemini App: Retrieve SQL Data from STUDENT DB")

question = st.text_input("Ask a question about the STUDENT database:")
submit = st.button("Ask")

if submit:
    sql_query = get_gemini_response(question, prompt)
    st.subheader("Generated SQL Query")
    st.code(sql_query, language="sql")
    
    # Execute query safely
    response, columns = read_sql_query(sql_query)
    
    st.subheader("Query Results")
    if response:
        st.table(pd.DataFrame(response, columns=columns))
    else:
        st.write("No results found or invalid SQL query.")
