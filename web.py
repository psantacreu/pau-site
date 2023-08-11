import streamlit as st

st.set_page_config(page_title="Pau Santacreu", page_icon="👤", layout="centered")

# ---- CSS ----
background_color = "#fbfaf6"
css = f"""
    <style>
    body {{
        background-color: {background_color};
        text-align: center;
    }}
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

# ---- Page content ----
with st.container():
    st.subheader("Hey I'm Pau Santacreu :wave:")
    st.write("##")
    st.write("Startups at [Vermú](https://vermu.com) & International Bussiness Economics student at [UPF](https://upf.edu)")
    st.write("you can email me at pau@vermu.io")
    st.write("[LinkedIn](https://www.linkedin.com/in/pausantacreu/)" " | " "[Twitter](https://twitter.com/psantacreug)")
