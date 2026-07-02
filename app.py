import streamlit as st
from report_generator import generate_report

from agent import answer_query
from data_utils import (
    load_data,
    get_summary,
    get_numeric_columns,
    get_ai_insights,
    get_health_score,
    generate_ai_summary
)

from charts import (
    histogram,
    bar_chart,
    line_chart,
    scatter_plot,
    box_plot,
    pie_chart,
    correlation_heatmap
)

st.set_page_config(
    page_title="Autonomous Data Science Co-Pilot",
    layout="wide"
)

st.title("Autonomous Data Science Co-Pilot")

# ---------------- Sidebar ----------------

st.sidebar.title("Navigation")
st.sidebar.success("Autonomous Data Science Co-Pilot")
st.sidebar.markdown("---")
st.sidebar.write("### Features")
st.sidebar.write("• Upload CSV/Excel")
st.sidebar.write("• AI Insights")
st.sidebar.write("• Ask Questions")
st.sidebar.write("• Data Visualization")
st.sidebar.write("• Dataset Summary")

# ---------------- Upload ----------------

uploaded_file = st.file_uploader(
    "Upload a CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    df = load_data(uploaded_file)

    # Dataset Preview
    st.subheader("Dataset Preview")
    st.dataframe(df)

    # Summary
    summary = get_summary(df)
    health = get_health_score(df)

    # Metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", summary["rows"])

    with col2:
        st.metric("Columns", summary["columns"])

    with col3:
        st.metric("Health Score", f"{health}/100")

    # AI Insights
    st.subheader("AI Insights")

    insights = get_ai_insights(df)

    for insight in insights:
        st.info(insight)

    st.subheader("AI Dataset Summary")

    if st.button("Generate AI Summary"):

        with st.spinner("Analyzing dataset with Gemini..."):

            summary = generate_ai_summary(df)

        st.success(summary)

    # Ask Questions
    st.subheader("Ask a Question")

    question = st.text_input("Enter your question")

    if question:

        response = answer_query(question, df)

        if response["type"] == "text":

            st.success(response["result"])

        elif response["type"] == "histogram":

            numeric = get_numeric_columns(df)

            column = st.selectbox(
                "Select Numeric Column",
                numeric
            )

            fig = histogram(df, column)
            st.plotly_chart(fig, use_container_width=True)

        elif response["type"] == "bar":

            columns = df.columns

            x = st.selectbox("X-axis", columns)

            y = st.selectbox(
                "Y-axis",
                get_numeric_columns(df)
            )

            fig = bar_chart(df, x, y)
            st.plotly_chart(fig, use_container_width=True)

        elif response["type"] == "line":

            columns = df.columns

            x = st.selectbox("X-axis", columns)

            y = st.selectbox(
                "Y-axis",
                get_numeric_columns(df)
            )

            fig = line_chart(df, x, y)
            st.plotly_chart(fig, use_container_width=True)

        elif response["type"] == "scatter":

            numeric = get_numeric_columns(df)

            x = st.selectbox("X-axis", numeric)

            y = st.selectbox("Y-axis", numeric)

            fig = scatter_plot(df, x, y)
            st.plotly_chart(fig, use_container_width=True)

        elif response["type"] == "box":

            numeric = get_numeric_columns(df)

            column = st.selectbox("Column", numeric)

            fig = box_plot(df, column)
            st.plotly_chart(fig, use_container_width=True)

        elif response["type"] == "pie":

            column = st.selectbox(
                "Category Column",
                df.columns
            )

            fig = pie_chart(df, column)
            st.plotly_chart(fig, use_container_width=True)

        else:

            st.warning("Unknown request.")

    # Dataset Summary

    st.subheader("Dataset Summary")

    if st.button("Generate Summary"):

        st.write("### Missing Values")
        st.write(summary["missing"])

        st.write("### Statistics")
        st.write(summary["statistics"])

    st.subheader("Download AI Report")

if st.button("Generate AI Report"):

    filename = generate_report(
        summary,
        health,
        insights
    )

    with open(filename, "rb") as pdf_file:
        st.download_button(
            label="Download PDF Report",
            data=pdf_file,
            file_name=filename,
            mime="application/pdf"
        )

    # Correlation Heatmap
    st.subheader("Correlation Heatmap")

    numeric_cols = get_numeric_columns(df)

    if len(numeric_cols) >= 2:

        fig = correlation_heatmap(df)
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.info("Need at least two numeric columns to generate a correlation heatmap.")