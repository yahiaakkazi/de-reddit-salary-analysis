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
                from the Reddit community, specifically the ***"Salary on the Data Engineering"*** subreddit.""")
    # st.markdown('''
    #     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    #     :gray[pretty] :rainbow[colors].''')
    # st.markdown("Here's a bouquet &mdash;\
    #             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
    

df_salary_per_country = df[["Country","Base Salary"]]
df_salary_per_country["Base Salary"] = pd.to_numeric(df_salary_per_country["Base Salary"], errors="coerce")
df_salary_per_country = df_salary_per_country.groupby(by="Country",as_index=False).agg({"Base Salary":"mean"})

with col2:
    st.bar_chart(data=df_salary_per_country, x="Country", y="Base Salary")

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

