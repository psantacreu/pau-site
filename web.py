from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Pau Santacreu", page_icon="👤", layout="centered")

# ---- LOAD ASSETS ----
lottie_coding = "https://lottie.host/56477275-3dc5-4903-aec6-7b2bdced418c/7zVciE3bcb.json" #animation
img_drink_vermu = Image.open("/Users/pau/Desktop/programing/images/Frame.png")
img_art = Image.open("/Users/pau/Desktop/programing/images/art.png")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- Use Local CSS ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("/Users/pau/Desktop/programing/style/style.css")

# ---- background color ----
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


# ---- Content ----
with st.container():
    st.subheader("hey I'm Pau Santacreu :wave:")
    st.write("##")
    st.write("Startups at [Vermú](https://vermu.com) & International Bussiness Economics student at [UPF](https://upf.edu)")
    st.write("you can email me at pau@vermu.io")
    st.write("[LinkedIn](https://www.linkedin.com/in/pausantacreu/)" " | " "[Twitter](https://twitter.com/psantacreug)")
