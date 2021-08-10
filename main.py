import streamlit as st
import requests

API_URL = "https://shardeaj1.herokuapp.com/"

def analyst_brandoverview(company, industry, summary):
    my_data = {"company": company,
               "industry": industry,
               "summary": summary}
    response = requests.post(API_URL + "analyst_brandoverview", json=my_data)
    return response.text

st.title("Marketing Summaries Generator")
st.markdown("""Transform forms into summaries with the power of AI.""")

st.markdown("### Analyst Brand Overview")
with st.form(key='analyst_brand_overview'):
    col1, col2 = st.beta_columns(2)
    company = col1.text_input(label="The company’s name is")
    col2.text("")
    col2.text("")
    col2.text("")
    col2.markdown(".")
    col3, col4 = st.beta_columns(2)
    industry = col3.text_input(label="Their company is in the")
    col4.text("")
    col4.text("")
    col4.text("")
    col4.markdown("industry.")
    col5, col6 = st.beta_columns(2)
    summary = col5.text_area(label="They hope to serve")
    col6.text("")
    col6.text("")
    col6.text("")
    col6.text("")
    col6.text("")
    col6.text("")
    col6.markdown(", as their ideal clients.")
    submit = st.form_submit_button(label='Submit')
    if submit:
        output = analyst_brandoverview(company, industry, summary)
        st.markdown(output)



