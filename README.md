# 📝 QueryBridge-LLM (Text-to-SQL Query Generator)  

## 🚀 Overview  
This project converts natural language queries (English text) into **SQL statements** and retrieves results directly from a relational database.  
It enables non-technical users to query databases seamlessly without writing SQL.  

## 🎯 Features  
- Accepts text input and generates corresponding SQL queries.  
- Executes queries and returns results in a tabular format.  
- Supports filtering, ordering, and custom conditions.  
- Built using **Python, Pandas, Streamlit, and Google Generative AI (Gemini API)**.  

## 🛠️ Tech Stack  
- **Python** – Core programming language  
- **Streamlit** – Interactive web interface  
- **Pandas** – Data manipulation & visualization  
- **Google Generative AI (Gemini API)** – Natural language to SQL conversion  
- **SQLite** – Backend database  

## 📂 Project Structure  
├── app.py # Streamlit main application
├── sql.py # Core Text-to-SQL logic
├── dataset/ # Sample database & schema - It will be created once you run and enter natural language queries
├── requirements.txt # Dependencies
├── .env.example # Example environment file - makersuite.google.com/app/apikey [you create an google-api key from this website and paste it in this .env
└── README.md # Project documentation


## ▶️ Setup Instructions  

### 1️⃣ Clone the Repository  

git clone https://github.com/Shashank-Varidelly/QueryBridge-LLM.git

cd QueryBridge-LLM

## Creating a Virtual Environment

python -m venv venv

source venv/bin/activate   # On Mac/Linux

venv\Scripts\activate      # On Windows

## Install Dependencies

pip install -r requirements.txt

## 4️⃣ Configure Environment Variables

### Paste the Created google API key in the .env file:

GOOGLE_API_KEY="your_api_key_here"

## Run The Streamlit App

streamlit run app.py


## Demo

Input:
"Show all students in Section A"

Generated SQL:

SELECT * FROM students WHERE class = 10;


Answer will be "Krish"

## 💡 Use Cases

Business analysts extracting insights from databases.

Educational dashboards for schools/colleges.

Customer service teams accessing structured records.


