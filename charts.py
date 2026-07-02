import plotly.express as px


def histogram(df, column):
    return px.histogram(
        df,
        x=column,
        title=f"Distribution of {column}"
    )


def bar_chart(df, x_col, y_col):
    return px.bar(
        df,
        x=x_col,
        y=y_col,
        title=f"{y_col} vs {x_col}"
    )


def line_chart(df, x_col, y_col):
    return px.line(
        df,
        x=x_col,
        y=y_col,
        title=f"{y_col} vs {x_col}"
    )


def scatter_plot(df, x_col, y_col):
    return px.scatter(
        df,
        x=x_col,
        y=y_col,
        title=f"{y_col} vs {x_col}"
    )


def box_plot(df, column):
    return px.box(
        df,
        y=column,
        title=f"Box Plot of {column}"
    )


def pie_chart(df, column):
    counts = df[column].value_counts().reset_index()
    counts.columns = [column, "Count"]

    return px.pie(
        counts,
        names=column,
        values="Count",
        title=f"Pie Chart of {column}"
    )
def correlation_heatmap(df):

    import plotly.express as px

    numeric_df = df.select_dtypes(include=["number"])

    corr = numeric_df.corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="RdBu_r",
        title="Correlation Heatmap"
    )

    return fig