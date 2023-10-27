import pandas as pd
import streamlit as st





df = pd.read_csv("data.csv")

st.set_page_config(layout = "wide")
col1, col2 = st.columns(2)

with col1:
    st.markdown("# Data Engineering Salary Analysis")
    st.markdown("""
                Welcome to the ***Data Engineering Salary Analysis*** web app! This platform provides
                a **comprehensive exploration** of **salary** information and relevant data for **data 
                engineering roles worldwide**. The dataset is curated based on **searches and submissions**
                from the Reddit community, specifically the ***"Salary on the Data Engineering"*** subreddit.
                Whenever this app is run through the docker file, the reddit scraper and openai"s gpt crawl data
                from subredit data engineering salary submissions and then this webapp gets deployed. In other words,
                these results are completely """)
    # st.markdown('''
    #     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    #     :gray[pretty] :rainbow[colors].''')
    # st.markdown("Here's a bouquet &mdash;\
    #             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
    

df_salary_per_country = df[["Country","Base Salary"]]
df_salary_per_country["Base Salary"] = pd.to_numeric(df_salary_per_country["Base Salary"], errors="coerce")
df_salary_per_country = df_salary_per_country.groupby(by="Country",as_index=False).agg({"Base Salary":"mean"})
df_num = df[["Country","Base Salary"]]
df_num["Base Salary"] = pd.to_numeric(df_salary_per_country["Base Salary"], errors="coerce")
mean = df_num[["Base Salary"]].mean().values[0]
medi = df_num[["Base Salary"]].median().values[0]
rounded_mean = round(mean/1000,1)
rounded_medi = round(medi/1000,1)
rounded_min = round(df_num[["Base Salary"]].min().values[0]/1000,1)
rounded_max = round(df_num[["Base Salary"]].max().values[0]/1000,1)
with col2:
    st.bar_chart(data=df_salary_per_country, x="Country", y="Base Salary")
    coll1, coll2, coll3 ,coll4 = st.columns(4)
    coll1.metric("Avg. Salary", f'{rounded_mean}K $', "1.2 °F")
    coll2.metric("Median Sal", f'{rounded_medi}K $', "-8%")
    coll3.metric("Min Salary", f'{rounded_min}K $', "4%")
    coll4.metric("Max Salary", f'{rounded_max}K $', "4%")

st.sidebar.header("Contact Information")
st.sidebar.markdown("- Email: [yahia.akkazi@centrale-marseille.fr](mailto:yahia.akkazi@centrale-marseille.fr)")
st.sidebar.markdown("- Phone: +33 7 50 58 50 55")
st.sidebar.markdown("- Portfolio: [My Portfolio](http://akkazi-portfolio.ddnsgeek.com:3000/)")



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
st.markdown('<div class="footer">Contact Information: yahia.akkazi@centrale-marseille.fr</div>', unsafe_allow_html=True)

