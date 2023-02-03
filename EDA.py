import numpy as np
import pandas as pd
import seaborn as sns
import  streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.header('Exploratory Data Analysis web App')

with st.sidebar.header('Upload your CSV file'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("[Example CSV files](https://www.google.com/search?q=Urls+of+different+dummy+data+sets&oq=Urls+of+different+dummy+data+sets&aqs=chrome..69i57.12094j0j1&sourceid=chrome&ie=UTF-8)")
    
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    
    df = load_csv()
    st.text('**Input Data of CSV file**')
    st.write(df)
    pr = ProfileReport(df, explorative= True)
    
    st.write('---')
    st.header("Profiling report with pandas")
    st_profile_report(pr)
  
else:
    st.info("Please upload Data Set")
    if st.button("Click for example Data Set"):
        @st.cache
        def load_csv():
            a = pd.DataFrame(np.random.rand(100,5), columns=['age','weight','height', 'Salary','Tax'])
            return a
        df = load_csv()
        st.header("Input Data")
        st.write(df)
        st.markdown('---')
        st.header("Pandas profiling Report")
        pr = ProfileReport(df, explorative=True)

        st_profile_report(pr)

    else:
        st.write("")