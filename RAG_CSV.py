from dotenv import find_dotenv, load_dotenv
import os
import pandas as pd
import streamlit as st
from langchain.prompts import PromptTemplate
import google.generativeai as genai
from groq import Groq

load_dotenv()

template1 = """You are a powerful data analyst. Your job is to answer questions about a dataset in a CSV format using pandas operations.
You are given a question and context regarding the CSV data. Based on the given context, generate a pandas query to answer the question.
Do not use SQL. Instead, use pandas operations like df.groupby(), df.sort_values(), df.loc[], etc. to manipulate the data.

These are the columns present in the DataFrame 'df':
{columns}

Note that 'Date' is in datetime format, and 'Time' is in string format.
Ensure to use correct column names exactly as provided, including any dots or special characters.

Understand this and provide an accurate pandas query which helps to extract the data.
Return only the pandas code, without any explanations or additional text.
Ensure that the code is a complete pandas operation that can be executed as a single statement.

### Input:
{question}

### Context:
{context}

### Response:"""


template2 = """You are a powerful data analyst. Your job is to correct the the given Pandas query and provide correct query based on the data.
You are given the query and context regarding the CSV data.

These are the columns present in the DataFrame 'df':
{columns}

Note that 'Date' is in datetime format, and 'Time' is in string format.
Ensure to use correct column names exactly as provided, including any dots or special characters.

Understand this and correct the given pandas query which helps to extract the data.
Return only the pandas code, without any explanations or additional text.
Ensure that the code is a complete pandas operation that can be executed as a single statement.

### Input:
{query}

### Context:
{context}

### Response:"""





prompt1 = PromptTemplate.from_template(template=template1)



client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

def groq_infer1(prompt):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama-3.1-70b-versatile",
)
    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content


prompt2 = PromptTemplate.from_template(template=template2)

def groq_infer2(prompt):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama3-70b-8192",
)
    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content





def execute_pandas_query(query, df):
    try:
        # Wrap the query in a function to allow for more complex operations
        exec_globals = {'pd': pd, 'df': df}
        exec(f"def query_func(df):\n    return {query}", exec_globals)
        result = exec_globals['query_func'](df)
        return result
    except Exception as e:
        print(f"Error executing pandas query: {e}")
        return None

def preprocess_dataframe(df):
    # Convert 'Date' column to datetime
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # Keep 'Time' as string for now
    return df

def main():
    st.set_page_config(page_title="Data Analyst", page_icon="📊", layout="wide")
    st.title("Pandas Data Analyst ft. Gemini")

    col1, col2 = st.columns([2, 3])

    with col1:
        uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file, encoding="latin1")
            df = preprocess_dataframe(df)
            st.write("Here's a preview of your uploaded file:")
            st.dataframe(df)

            columns = "\n".join(f"- {col}: {df[col].dtype}" for col in df.columns)
            st.write("DataFrame Columns and Types:")
            st.code(columns)

    with col2:
        if uploaded_file is not None:
            question = st.text_input("Write a question about the data", key="question")

            if st.button("Get Answer", key="get_answer"):
                if question:
                    attempt = 0
                    max_attempts = 10
                    while attempt < max_attempts:
                        try:
                            input1 = {"columns": columns, "question": question, "context": ""}
                            formatted_prompt = prompt1.invoke(input=input1).text
                            pandas_query = groq_infer1(formatted_prompt)
                            input2 = {"columns": columns, "query": pandas_query, "context": ""}
                            formatted_prompt2 = prompt2.invoke(input=input2).text
                            pandas_query2 = groq_infer2(formatted_prompt2)
                            result = execute_pandas_query(pandas_query2, df)
                            if result is not None:
                                st.write("Answer:")
                                if isinstance(result, pd.DataFrame):
                                    st.dataframe(result)
                                elif isinstance(result, pd.Series):
                                    st.dataframe(result.to_frame())
                                else:
                                    st.write(result)
                                st.write("Pandas Query Used:")
                                st.code(pandas_query)
                                break
                            else:
                                raise Exception("Invalid pandas query")
                        except Exception as e:
                            attempt += 1
                            st.error(
                                f"Attempt {attempt}/{max_attempts} failed. Error: {str(e)}. Retrying..."
                            )
                            if attempt == max_attempts:
                                st.error(
                                    "Unable to get the correct query, please try rephrasing your question."
                                )
                            continue
                else:
                    st.warning("Please enter a question before clicking 'Get Answer'.")

if __name__ == "__main__":
    main()