# Autonomous Data Science Co-Pilot

## Project Overview

Autonomous Data Science Co-Pilot is an AI-powered data analysis application built using Python, Streamlit, Google Gemini AI, and Retrieval-Augmented Generation (RAG). The application enables users to upload datasets, perform exploratory data analysis, visualize data through interactive charts, ask natural language questions, and generate AI-powered PDF reports.

The project combines traditional data science techniques with Generative AI to create an intelligent assistant capable of answering both dataset-specific and general data science questions.

---

## Features

* Upload CSV and Excel datasets
* Interactive dataset preview
* Dataset summary and descriptive statistics
* AI-generated dataset insights
* Dataset Health Score
* Natural Language Question Answering
* Retrieval-Augmented Generation (RAG)
* Google Gemini AI Integration
* Interactive Data Visualizations

  * Histogram
  * Bar Chart
  * Line Chart
  * Scatter Plot
  * Box Plot
  * Pie Chart
  * Correlation Heatmap
* AI-generated PDF Report
* Knowledge Base for Data Science Concepts
* Modular project architecture

---

## Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Plotly
* Scikit-learn
* Google Gemini API
* Sentence Transformers
* FAISS
* ReportLab
* python-dotenv

---

## Project Architecture

```text
User
   │
   ▼
Streamlit Interface
   │
   ▼
User Query
   │
   ▼
Agent
   │
   ├── Rule-Based Answers
   │
   └── RAG Pipeline
         │
         ├── Sentence Transformer
         ├── FAISS Vector Search
         ├── Knowledge Base Retrieval
         └── Google Gemini AI
                    │
                    ▼
             Final Response
```

---

## Folder Structure

```text
Autonomous_DataScience_CoPilot/
│
├── app.py
├── agent.py
├── rag.py
├── knowledge_base.py
├── charts.py
├── data_utils.py
├── report_generator.py
├── requirements.txt
├── README.md
├── .env
│
├── docs/
├── data/
└── venv/
```

---

## Installation

Clone the repository.

Install the required packages.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application.

```bash
streamlit run app.py
```

---

## How It Works

1. Upload a CSV or Excel dataset.
2. Explore the dataset using interactive visualizations.
3. View AI-generated insights and health score.
4. Ask questions in natural language.
5. The system first checks rule-based responses.
6. If needed, the RAG pipeline retrieves relevant knowledge using FAISS.
7. Google Gemini generates a context-aware answer.
8. Generate and download an AI-powered PDF report.

---

## Future Enhancements

* Support for multiple file uploads
* SQL database connectivity
* Automatic machine learning (AutoML)
* Predictive analytics
* Interactive dashboards
* Voice-based AI assistant
* Cloud deployment
* User authentication

---

## Author

**Areeba Farooqui**

Project developed as part of an AI/Data Science internship.

---

## License

This project is intended for educational and internship purposes.
