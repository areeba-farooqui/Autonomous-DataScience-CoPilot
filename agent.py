import os
from dotenv import load_dotenv
import google.generativeai as genai
from rag import retrieve_documents, knowledge_base, index

# Load API key
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def answer_query(question, df):

    q = question.lower()

    # ---------- Rule Based ----------

    if "rows" in q:
        return {
            "type": "text",
            "result": f"The dataset has {df.shape[0]} rows."
        }

    elif "columns" in q:
        return {
            "type": "text",
            "result": f"The dataset has {df.shape[1]} columns."
        }

    elif "column names" in q:
        return {
            "type": "text",
            "result": ", ".join(df.columns)
        }

    elif "average" in q:
        return {
            "type": "text",
            "result": str(df.mean(numeric_only=True))
        }

    elif "maximum" in q or "max" in q:
        return {
            "type": "text",
            "result": str(df.max(numeric_only=True))
        }

    elif "minimum" in q or "min" in q:
        return {
            "type": "text",
            "result": str(df.min(numeric_only=True))
        }

    elif "missing" in q:
        return {
            "type": "text",
            "result": str(df.isnull().sum())
        }

    elif "histogram" in q:
        return {"type": "histogram"}

    elif "bar" in q:
        return {"type": "bar"}

    elif "line" in q:
        return {"type": "line"}

    elif "scatter" in q:
        return {"type": "scatter"}

    elif "box" in q:
        return {"type": "box"}

    elif "pie" in q:
        return {"type": "pie"}

    # ---------- Gemini + RAG ----------

    retrieved_docs = retrieve_documents(
        question,
        knowledge_base,
        index
    )

    context = "\n".join(retrieved_docs)

    prompt = f"""
You are an expert Data Science assistant.

Use the retrieved knowledge below to answer the user's question.

Retrieved Knowledge:
{context}

Dataset Information:
Rows: {df.shape[0]}
Columns: {df.shape[1]}

Column Names:
{list(df.columns)}

First Five Rows:
{df.head().to_string()}

User Question:
{question}

Give a clear, accurate, and concise answer.
"""

    response = model.generate_content(prompt)

    return {
        "type": "text",
        "result": response.text
    }