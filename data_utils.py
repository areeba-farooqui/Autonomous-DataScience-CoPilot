import pandas as pd
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def load_data(uploaded_file):

    if uploaded_file.name.endswith(".csv"):
        return pd.read_csv(uploaded_file)

    elif uploaded_file.name.endswith(".xlsx"):
        return pd.read_excel(uploaded_file)


def get_summary(df):

    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing": df.isnull().sum(),
        "statistics": df.describe()
    }


def get_numeric_columns(df):

    return df.select_dtypes(include=["number"]).columns


def get_ai_insights(df):

    insights = []

    rows = df.shape[0]
    cols = df.shape[1]

    insights.append(f"Dataset contains {rows} rows and {cols} columns.")

    missing = df.isnull().sum().sum()

    if missing == 0:
        insights.append("No missing values detected.")
    else:
        insights.append(f"Dataset contains {missing} missing values.")

    duplicates = df.duplicated().sum()

    if duplicates == 0:
        insights.append("No duplicate rows found.")
    else:
        insights.append(f"Dataset contains {duplicates} duplicate rows.")

    numeric = len(df.select_dtypes(include=["number"]).columns)
    categorical = len(df.select_dtypes(include=["object", "category"]).columns)

    insights.append(f"Numeric columns: {numeric}")
    insights.append(f"Categorical columns: {categorical}")

    if missing > 0:
        insights.append("Recommendation: Handle missing values before model training.")

    if categorical > 0:
        insights.append("Recommendation: Encode categorical columns.")

    if numeric > 0:
        insights.append("Recommendation: Scale numerical features if required.")

    if numeric >= 2:
        insights.append("Recommended visualization: Correlation Heatmap or Scatter Plot.")
    elif numeric == 1:
        insights.append("Recommended visualization: Histogram or Box Plot.")
    else:
        insights.append("Recommended visualization: Bar Chart or Pie Chart.")

    return insights

def get_health_score(df):

    score = 100

    # Penalize missing values
    missing = df.isnull().sum().sum()
    score -= min(missing, 30)

    # Penalize duplicate rows
    duplicates = df.duplicated().sum()
    score -= min(duplicates * 2, 20)

    if score < 0:
        score = 0

    return score

def generate_ai_summary(df):

    prompt = f"""
You are an expert Data Scientist.

Analyze the following dataset and provide:

1. A short overview of the dataset.
2. Possible machine learning task (classification, regression, clustering, etc.).
3. Data quality observations.
4. Recommended preprocessing steps.
5. Recommended visualizations.

Dataset Information:

Rows: {df.shape[0]}
Columns: {df.shape[1]}

Column Names:
{list(df.columns)}

Data Types:
{df.dtypes.to_string()}

First Five Rows:
{df.head().to_string()}
"""

    response = model.generate_content(prompt)

    return response.text