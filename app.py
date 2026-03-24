import streamlit as st
import base64
import random
from PIL import Image

def get_image_base64(filename):
    with open(filename, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

bg_data = get_image_base64("HBDBG.jpeg")
bg_layer = get_image_base64("BGLAYER1.png")

st.set_page_config(page_title="HELLBOUND DISCIPLEZ", page_icon="🤘", layout="wide")

st.markdown(f"""
<style>

.stApp {{
background-image:
url("data:image/png;base64,{bg_layer}"),
url("data:image/jpeg;base64,{bg_data}");
background-size: cover, cover;
background-repeat: repeat, repeat;
background-attachment: fixed, fixed;
color:#ff2200;
}}

[data-testid="stSidebar"] {{
background-image:
url("data:image/png;base64,{bg_layer}"),
url("data:image/jpeg;base64,{bg_data}");
background-size: cover, cover;
}}

h1,h2,h3,h4,h5,h6,p,label {{
color:#ff2200 !important;
font-family: Georgia, serif;
}}

</style>
""", unsafe_allow_html=True)


# HEADER
col1,col2,col3 = st.columns([1,2,1])
with col2:
    st.image("HBDLOGO1.png", width=500)
    st.markdown(
        '<div style="text-align:center;font-size:24px;">Official Underground Hub</div>',
        unsafe_allow_html=True
    )


# SIDEBAR
with st.sidebar:
    st.image("chainsawart.png", use_column_width=True)

    menu = st.radio(
        "",
        [
            "The Ritual (Home)",
            "The Grimoires (Discography)",
            "The Cult (Members)",
            "The Catacombs (Photos)"
        ]
    )


# HOME
if menu == "The Ritual (Home)":

    pistol = get_image_base64("pistol-removebg-preview.png")

    st.markdown(f"""
    <div style="text-align:center;font-size:28px;">
    <img src="data:image/png;base64,{pistol}" width="60">
    <b> WHO ARE WE </b>
    <img src="data:image/png;base64,{pistol}" width="60" style="transform:scaleX(-1);">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
<div style="text-align:center">

Forged in the depths of the underground, Hellbound Disciplez is a formidable trio consisting of Lord-K-Haos, Crazy8 The Snap Case, and Osomane.

Independent and unbothered, these three sonic provocateurs blaze their own trail. With a sound that's equal parts gritty phonk and horrorcore, they paint vivid portraits of America's dark underbelly.

🔥 Deep South, United States 🔥

⚡ Glitch Tape Vol. 2 — Coming Soon ⚡

</div>
""", unsafe_allow_html=True)


# DISCOGRAPHY
elif menu == "The Grimoires (Discography)":

    st.markdown("""
<div style="text-align:center;font-size:28px;">
💀 THE GRIMOIRES (Discography) 💀
</div>
""", unsafe_allow_html=True)

    st.markdown("""<div style="text-align:center">DISCOGRAPHY CONTENT HERE (unchanged)</div>""", unsafe_allow_html=True)


# MEMBERS
elif menu == "The Cult (Members)":

    st.markdown('<div style="text-align:center;font-size:28px;">💀 THE CULT 💀</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # MEMBER 1
    col1, col2 = st.columns([1,3])

    with col1:
        st.image("pic5.jpg", width=220)

    with col2:
        st.markdown("""
### 🔥 Lord-K-Haos
MC | Lyricist | Co-Founder  

The chaos incarnate. Lord-K-Haos brings the darkness with razor sharp lyricism and an iron grip on the mic.
""")

    st.markdown("<br><br>", unsafe_allow_html=True)

    # MEMBER 2
    col1, col2 = st.columns([1,3])

    with col1:
        st.image("img12.jpg", width=220)

    with col2:
        st.markdown("""
### 🔥 Crazy8 The Snap Case
MC | Lyricist | Producer | Co-Founder  

Raw, unfiltered, and unpredictable. Crazy8 The Snap Case delivers horrorcore at its most visceral while helping craft the sonic backbone of the group alongside Osomane.
""")

    st.markdown("<br><br>", unsafe_allow_html=True)

    # MEMBER 3
    col1, col2 = st.columns([1,3])

    with col1:
        st.image("img11.jpg", width=220)

    with col2:
        st.markdown("""
### 🔥 Osomane
Producer | Member  

The architect of the sound. Osomane works hand in hand with Crazy8 to build the dark, gritty beats that bring the Hellbound Disciplez vision to life.
""")


# PHOTOS
elif menu == "The Catacombs (Photos)":

    st.markdown('<div style="text-align:center;font-size:28px;">💀 THE CATACOMBS 💀</div>', unsafe_allow_html=True)

    photos = [
        "pic1.png","pic2.png","pic3.png","pic4.png",
        "pic5.jpg","pic6.png","pic7.jpg","pic8.jpeg",
        "pic9.jpeg","pic10.png","pic11.jpeg"
    ]

    random.shuffle(photos)

    for p in photos:
        st.image(p, use_container_width=True)
