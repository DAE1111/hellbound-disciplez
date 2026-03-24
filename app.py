import streamlit as st
import base64
import random
from PIL import Image

def get_image_base64(filename):
    with open(filename, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

# Load background images
bg_data = get_image_base64("HBDBG.jpeg")
bg_layer = get_image_base64("BGLAYER1.png")

# Page config
st.set_page_config(page_title="HELLBOUND DISCIPLEZ", page_icon="🤘", layout="wide")

# CSS for background, fonts, sidebar toggle
st.markdown(f"""
<style>
.stApp {{
background-image: 
url('data:image/png;base64,{bg_layer}'),
url('data:image/jpeg;base64,{bg_data}');
background-size: cover, cover;
background-repeat: repeat, repeat;
background-attachment: fixed, fixed;
color: #ff2200;
}}

[data-testid="stSidebar"] {{
background-image: 
url('data:image/png;base64,{bg_layer}'),
url('data:image/jpeg;base64,{bg_data}');
background-size: cover, cover;
background-repeat: repeat, repeat;
background-attachment: fixed, fixed;
border-right: 2px solid #ff2200;
}}

h1, h2, h3, h4, h5, h6, p, label, .stRadio label {{
color: #ff2200 !important;
font-family: 'Georgia', serif;
}}

.stRadio > div {{
color: #ff2200;
}}

hr {{
border-color: #ff2200;
}}

img {{
display: block;
margin: auto;
}}

/* Highlight sidebar toggle */
[data-testid="collapsedControl"] {{
    width: 40px !important;
    height: 40px !important;
    background-color: #ff2200 !important;
    border-radius: 8px !important;
    top: 15px !important;
    right: 15px !important;
    z-index: 999 !important;
}}
</style>
""", unsafe_allow_html=True)

# Instruction on main page about sidebar
st.markdown("""
<div style="font-size:18px; color:#ff2200; text-align:center; margin-top:20px;">
⬅️ <b>Click the arrow at the edge of the sidebar to expand/collapse the menu</b> ⬅️
</div>
""", unsafe_allow_html=True)

# Main header logo
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("HBDLOGO1.png", width=490)
    st.markdown('<div style="text-align:center; font-family:Georgia, serif; font-size:24px; color:#ff2200; margin-top:-10px;">Official Underground Hub</div>', unsafe_allow_html=True)
    st.markdown("---")

# Load images for sidebar
top_img = Image.open("chainsawart.png")
pistol_img_file = "pistol-removebg-preview.png"

# Sidebar
with st.sidebar:
    st.image(top_img, use_column_width=True)
    st.header("THE VOID")
    menu = st.radio("Navigate:", ["The Ritual (Home)", "The Grimoires (Discography)", "The Cult (Members)", "The Catacombs (Photos)"])

# Ritual / Home page
if menu == "The Ritual (Home)":
    st.markdown(f"""
    <div style="text-align:center; color:#ff2200; font-family:Georgia, serif; font-size:28px; margin-top:20px;">
    <span style="display:inline-block; vertical-align:middle;">
        <img src="data:image/png;base64,{get_image_base64(pistol_img_file)}" style="height:32px;">
    </span>
    <span style="display:inline-block; vertical-align:middle; margin: 0 12px;">
        <b>WHO WE ARE</b>
    </span>
    <span style="display:inline-block; vertical-align:middle;">
        <img src="data:image/png;base64,{get_image_base64(pistol_img_file)}" style="height:32px; transform: scaleX(-1);">
    </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
<div style="text-align:center; font-family:Georgia, serif; color:#ff2200; margin-top:20px;">
Forged in the depths of the underground, Hellbound Disciplez is a formidable trio consisting of <b>Lord-K-Haos</b>, <b>Crazy8 The Snap Case</b>, and <b>Osomane</b>. Independent and unbothered, these three sonic provocateurs blaze their own trail. With a sound that's equal parts gritty phonk and horrorcore, they paint vivid portraits of America's dark underbelly - exploring themes of the occult, street life, and true crime. Fueled by the collaborative production of Osomane and Crazy8 The Snap Case, and the raw lyricism of the whole crew, their music is a haunting reflection of the shadows that lurk just beyond the edge of society. Get ready to descend into the abyss with Hellbound Disciplez.
</div>
<div style="text-align:center; margin-top:20px;"><b>🔥 Deep South, United States 🔥</b></div>
<div style="text-align:center; margin-top:10px;"><b>⚡ Glitch Tape Vol. 2 — Coming Soon ⚡</b></div>
""", unsafe_allow_html=True)

# Grimoires page (formerly Discography)
elif menu == "The Grimoires (Discography)":
    st.markdown("""
<div style="text-align:center; color:#ff2200; font-family:Georgia, serif; font-size:28px; margin-top:20px;">
💀 THE GRIMOIRES 💀
</div>
<div style="text-align:center; margin-top:20px;">
📀 Albums & Releases
</div>
<div style="text-align:center; font-family:Georgia, serif; color:#ff2200; margin-top:10px;">
Tales From The Swamp (2025) — 8 tracks<br>
Hellbound Disciplez (Self Titled) (2023) — 15 tracks<br>
21 Grams Lighter (2022) — 10 tracks<br>
The Godless Mixtape Vol. 1 (2022) — 11 tracks<br>
Glitch Tape Volume 1 (2023) — 7 tracks<br>
Pumpkin Patch Massacre EP (2023) — 5 tracks (with Con-Crete)<br>
COUNTERFEIT (2025)<br>
3-D (2024)<br>
CROWBAR (2024)<br>
EVIL (2024)<br>
Get Back (2024)<br>
HorrorCrunk In My Trunk (2024)<br>
My House (2024)<br>
Out The Gate (2024)<br>
PLAY WIT BRAINZ (2024)<br>
Smoke (2024)<br>
RAGE (2024)<br>
Welcome To The South (2024)<br>
Bloodsuckers (2023)<br>
2 Pillar's (2023)<br>
Reign Terror (2023)<br>
Steppers ft. Psychologik (2023)
</div>
<div style="text-align:center; margin-top:20px;">
🔥 Follow / Stream Hellbound Disciplez<br>
🎧 Spotify<br>
🍎 Apple Music<br>
📦 Amazon Music<br>
📘 Facebook<br>
📸 Instagram
</div>
""", unsafe_allow_html=True)

# Cult / Members page
elif menu == "The Cult (Members)":
    st.markdown("""
<div style="text-align:center; color:#ff2200; font-family:Georgia, serif; font-size:28px; margin-top:20px;">
💀 THE CULT 💀
</div>
""", unsafe_allow_html=True)

    members = [
        ("pic5.jpg", "🔥 Lord-K-Haos", "MC | Lyricist | Co-Founder — The chaos incarnate. Lord-K-Haos brings the darkness with razor sharp lyricism and an iron grip on the mic."),
        ("img12.jpg", "🔥 Crazy8 The Snap Case", "MC | Lyricist | Producer | Co-Founder — Raw, unfiltered, and unpredictable. Crazy8 The Snap Case delivers horrorcore at its most visceral while helping craft the sonic backbone of the group alongside Osomane."),
        ("img11.jpg", "🔥 Osomane", "Producer | Member — The architect of the sound. Osomane works hand in hand with Crazy8 to build the dark, gritty beats that bring the Hellbound Disciplez vision to life."),
    ]

    for img_file, name, desc in members:
        st.image(img_file, width=150)
        st.markdown(f'<div style="text-align:center; color:#ff2200; font-family:Georgia, serif; margin-top:10px;"><b>{name}</b></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align:center; color:#ff2200; font-family:Georgia, serif; margin-bottom:20px;">{desc}</div>', unsafe_allow_html=True)

# Catacombs / Photos page
elif menu == "The Catacombs (Photos)":
    st.markdown("""
<div style="text-align:center; color:#ff2200; font-family:Georgia, serif; font-size:28px; margin-top:20px;">
💀 THE CATACOMBS 💀
</div>
""", unsafe_allow_html=True)

    photos = [
        "pic1.png","pic2.png","pic3.png","pic4.png","pic5.jpg","pic6.png","pic7.jpg","pic8.jpeg",
        "pic9.jpeg","pic10.png","pic11.jpeg","pic12.jpeg","pic13.jpeg","pic14.jpeg","pic15.jpeg",
        "pic16.jpeg","pic17.jpeg","pic18.jpeg","pic20.png","pic21.png","pic22.png","pic23.jpg",
        "pic24.png","pic25.jpg","pic26.jpg","pic27.jpg","pic28.jpg","pic29.jpg","pic30.jpg",
        "pic31.jpg","pic32.jpg","pic33.jpg","pic34.jpg","pic35.jpg","pic36.jpg","pic37.jpg",
        "pic39.jpg","pic40.jpg","pic41.jpg","img1.jpg","img2.jpg","img3.jpg","img4.jpg",
        "img5.jpg","img6.jpg","img7.jpg","img8.jpg","img9.jpg","img10.jpg","img11.jpg",
    ]

    random.shuffle(photos)

    cols = st.columns(2)
    for i, photo_path in enumerate(photos):
        with cols[i % 2]:
            st.image(photo_path, use_container_width=True)
