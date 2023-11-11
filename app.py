import math
from typing import Union, Tuple
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import ast
import numpy as np


def get_metrics(df: pd.DataFrame, country: str) -> Tuple[Union[int,str]]:
    result = pd.to_numeric(df[df.Country == country]["Base Salary"], errors="coerce")
    return (
        result.shape[0],
        result.mean() / 1000,
        result.median() / 1000,
        result.min() / 1000,
        result.max() / 1000,
    )


def main():
    df = pd.read_csv("data.csv").drop(columns=["Unnamed: 0"])

    df_tech_stack = df[["Tech Stack"]]
    df_tech_stack["Tech Stack"] = df_tech_stack["Tech Stack"].apply(
        lambda x: ast.literal_eval(x.lower()) if pd.notnull(x) else np.nan
    )
    df_tech_stack = df_tech_stack.explode("Tech Stack")
    df_tech_stack = df_tech_stack.value_counts().to_frame().reset_index().iloc[0:20, :]

    st.set_page_config(layout="wide")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("# Data Engineering Salary Analysis")
        st.markdown(
            """
                    Welcome to the ***Data Engineering Salary Analysis*** web app! This platform provides
                    a **comprehensive exploration** of **salary** information and relevant data for **data 
                    engineering roles worldwide**. The dataset is curated based on **searches and submissions**
                    from the Reddit community, specifically the ***"Salary on the Data Engineering"*** subreddit.
                    Whenever this app is run through the docker file, the reddit scraper and openai"s gpt crawl data
                    from subredit data engineering salary submissions and then this webapp gets deployed. In other words,
                    these results are completely dependant on the perforamnce of the LLM, Chatgpt gives a moderaltely accurate
                    results, and one can finetune an open source llm to provided a scraping that works better than the current one.
                    """
        )
        st.markdown(
            """
                    For now: Here is the scraped dataset:
                    """
        )
        st.dataframe(df, height=200)
        fig = go.Figure(
            go.Treemap(
                labels=df_tech_stack["Tech Stack"],
                parents=[""] * len(df_tech_stack),
                values=df_tech_stack["count"],
            )
        )
        fig.update_layout(title="Most relevant frameworks")
        st.plotly_chart(fig)

    df_salary_per_country = df[["Country", "Base Salary"]]
    df_salary_per_country["Base Salary"] = pd.to_numeric(
        df_salary_per_country["Base Salary"], errors="coerce"
    )
    df_salary_per_country = df_salary_per_country.groupby(
        by="Country", as_index=False
    ).agg({"Base Salary": "mean"})
    df_num = df[["Country", "Base Salary"]]
    df_num["Base Salary"] = pd.to_numeric(
        df_salary_per_country["Base Salary"], errors="coerce"
    )
    nbb = df_num.shape[0]
    mean = df_num[["Base Salary"]].mean().values[0]
    medi = df_num[["Base Salary"]].median().values[0]
    rounded_mean = round(mean / 1000, 1)
    rounded_medi = round(medi / 1000, 1)
    rounded_min = round(df_num[["Base Salary"]].min().values[0] / 1000, 1)
    rounded_max = round(df_num[["Base Salary"]].max().values[0] / 1000, 1)

    with col2:
        st.markdown(
            """
                    Now let's see what are the average salary per country:
                    """
        )
        st.bar_chart(data=df_salary_per_country, x="Country", y="Base Salary")
        st.markdown(
            """
                    Following the provided graph, these are stats regarding the newly scraped data:
                    """
        )
        coll1, coll2, coll3, coll4, coll5 = st.columns(5)
        coll1.metric("Nb of data", f"{nbb}")
        coll2.metric("Avg. Salary", f"{rounded_mean}K $")
        coll3.metric("Median Sal", f"{rounded_medi}K $")
        coll4.metric("Min Salary", f"{rounded_min}K $")
        coll5.metric("Max Salary", f"{rounded_max}K $")

        st.markdown(
            """
                    There is also a filtering option for countrues which helps see relevant stats per country: 
                    """
        )
        colll1, colll2 = st.columns([1, 3])
        with colll1:
            option = st.selectbox("Country", tuple(pd.unique(df.Country)))
        with colll2:
            st.write(f"The following metrics show {option} stats.")
        collll1, collll2, collll3, collll4, collll5 = st.columns(5)
        nb_of_sub, avgg, medd, minn, maxx = get_metrics(df, option)
        collll1.metric("Nb of data", f"{nb_of_sub}")
        collll2.metric("Avg. Salary", f"{avgg:.1f}K $")
        collll3.metric("Median Sal", f"{medd:.1f}K $")
        collll4.metric("Min Salary", f"{minn:.1f}K $")
        collll5.metric("Max Salary", f"{maxx:.1f}K $")

    st.markdown(
        """
            <style>
            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #0e1117;
                padding: 10px;
                text-align: center;
            }
            </style>
            """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="footer">Contact Information: yahia.akkazi@centrale-marseille.fr</div>',
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
