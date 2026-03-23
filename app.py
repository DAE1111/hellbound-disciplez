import streamlit as st
import base64
import random

def get_image_base64(filename):
    with open(filename, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return data

bg_data = get_image_base64("HBDBG.jpeg")

st.set_page_config(page_title="HELLBOUND DISCIPLEZ", page_icon="🤘", layout="wide")

st.markdown(f"""
    <style>
        .stApp {{
            background-image: url('data:image/jpeg;base64,{bg_data}');
            background-size: cover;
            background-repeat: repeat;
            background-attachment: fixed;
            color: #ff2200;
        }}
        [data-testid="stSidebar"] {{
            background-image: url('data:image/jpeg;base64,{bg_data}');
            background-size: cover;
            background-repeat: repeat;
            background-attachment: fixed;
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
    </style>
""", unsafe_allow_html=True)

# Columns for centered logo
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("HBDLOGO1.png", width=490)

# Home page content
st.subheader("Official Underground Hub")
st.markdown("---")

# Main bio
st.markdown("""
Forged in the depths of the underground, Hellbound Disciplez is a formidable trio consisting of
**Lord-K-Haos**, **Crazy8 The Snap Case**, and **Osomane**. Independent and unbothered, these three sonic
provocateurs blaze their own trail. With a sound that's equal parts gritty phonk and horrorcore,
they paint vivid portraits of America's dark underbelly - exploring themes of the occult, street
life, and true crime. Fueled by the collaborative production of Osomane and Crazy8 The Snap Case,
and the raw lyricism of the whole crew, their music is a haunting reflection of the shadows that
lurk just beyond the edge of society. Get ready to descend into the abyss with Hellbound Disciplez.
""")

st.subheader("🔥 Deep South, United States 🔥")

# --- ANNOUNCEMENT ---
st.markdown("---")  # visually separates announcement
st.subheader("⚡ Glitch Tape Vol. 2 — In Progress, Coming Soon ⚡")

# Sidebar and rest of site (unchanged)
with st.sidebar:
    st.header("THE VOID")
    menu = st.radio("Navigate:", ["The Ritual (Home)", "The Discography", "The Cult (Members)", "The Catacombs (Photos)"])

if menu == "The Discography":
    st.header("💀 THE DISCOGRAPHY 💀")
    st.markdown("---")
    st.subheader("📀 Albums")
    st.markdown("""
- **Tales From The Swamp** (2025) — 8 tracks
- **Hellbound Disciplez (Self Titled)** (2023) — 15 tracks
- **21 Grams Lighter** (2022) — 10 tracks
    """)
    st.subheader("📼 Mixtapes")
    st.markdown("""
- **The Godless Mixtape Vol. 1** (2022) — 11 tracks
- **Glitch Tape Volume 1** (2023) — 7 tracks
    """)
    st.subheader("🎵 EPs")
    st.markdown("- **Pumpkin Patch Massacre EP** (2023) — 5 tracks (with Con-Crete)")
    st.subheader("🔥 Singles")
    st.markdown("""
- **COUNTERFEIT** (2025)
- **3-D** (2024)
- **CROWBAR** (2024)
- **EVIL** (2024)
- **Get Back** (2024)
- **HorrorCrunk In My Trunk** (2024)
- **My House** (2024)
- **Out The Gate** (2024)
- **PLAY WIT BRAINZ** (2024)
- **Smoke** (2024)
- **RAGE** (2024)
- **Welcome To The South** (2024)
- **Bloodsuckers** (2023)
- **2 Pillar's** (2023)
- **Reign Terror** (2023)
- **Steppers ft. Psychologik** (2023)
    """)
    st.markdown("---")
    st.markdown("🎧 [Listen on Spotify](https://open.spotify.com/artist/5hRvzAL7q1as1y5FqKEaGZ)")

# Rest of your Cult and Catacombs sections stay the same
