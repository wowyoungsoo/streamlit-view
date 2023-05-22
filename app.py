import streamlit as st

st.write('# Youtube view')
st.write('## raw')
st.write('### raw')
st.write('#### raw')
st.write('##### raw')
st.write('###### raw')

view=[100,150,30]
view
st.write('### bar chart')
st.bar_chart(view)

import pandas as pd

sview=pd.Series(view)
sview
