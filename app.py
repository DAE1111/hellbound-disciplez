import streamlit as st
import base64
import random

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
background-attachment: fixed;
}}

[data-testid="stSidebar"] {{
background-image:
url("data:image/png;base64,{bg_layer}"),
url("data:image/jpeg;base64,{bg_data}");
background-size: cover;
}}

h1,h2,h3,h4,h5,h6,p,div {{
color:#ff2200;
text-align:center;
}}

</style>
""", unsafe_allow_html=True)

# HEADER
col1,col2,col3 = st.columns([1,2,1])
with col2:
    st.image("HBDLOGO1.png", width=500)
    st.markdown("### Official Underground Hub")

# SIDEBAR
with st.sidebar:
    st.image("chainsawart.png")
    menu = st.radio("",[
        "The Ritual (Home)",
        "The Grimoires (Discography)",
        "The Cult (Members)",
        "The Catacombs (Photos)"
    ])

# HOME
if menu == "The Ritual (Home)":

    pistol = get_image_base64("pistol-removebg-preview.png")

    st.markdown(f"""
    <div style="font-size:30px;">
    <img src="data:image/png;base64,{pistol}" width="60">
    WHO ARE WE
    <img src="data:image/png;base64,{pistol}" width="60" style="transform:scaleX(-1);">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
Hellbound Disciplez is an underground horrorcore / phonk trio delivering dark southern energy,
gritty production, and unapologetic underground authenticity.

Operating independently, the group consists of:

Lord-K-Haos  
Crazy8 The Snap Case  
Osomane  

Forged in chaos. Built in the underground.  
No industry. No rules. No compromises.
""")

# DISCOGRAPHY
elif menu == "The Grimoires (Discography)":

    st.markdown("## 💀 THE GRIMOIRES (Discography) 💀")

    st.markdown("### 📀 Albums & Releases")

    st.markdown("""
[Tales From The Swamp (2025)](https://open.spotify.com/album/6ZOUHhIAnS532EdK1ZaLtv) — 8 tracks  
[Hellbound Disciplez (Self Titled) (2023)](https://open.spotify.com/album/43O3pIiiwtOhcd9VANWjga) — 15 tracks  
[21 Grams Lighter (2022)](https://open.spotify.com/album/2smEfqlW4Z16AUD5md7UxZ) — 10 tracks  
[The Godless Mixtape (2022)](https://open.spotify.com/album/0LW0Gp5neAyHtihn5pxteR) — 11 tracks  
[Glitch Tape Vol.1 (2023)](https://open.spotify.com/album/2jEHxL0P2uHT6SPokLnayC) — 7 tracks  
[Pumpkin Patch Massacre EP (2023)](https://open.spotify.com/album/1AoyhHGiy4PE6b9HIdfWRu)
""")

    st.markdown("### 💀 Singles")

    st.markdown("""
[COUNTERFEIT (2025)](https://open.spotify.com/album/03BObGWktQNHCLhoimV2lK)  
[CROWBAR (2024)](https://open.spotify.com/album/4EU2f7tAo6DWhERyavT37j)  
[MY HOUSE (2024)](https://open.spotify.com/album/40pDtzpR5i9jpvhjqNnidt)  
[EVIL (2024)](https://open.spotify.com/album/1Cnug15A07CIImqFiprqVq)  
[SMOKE (2024)](https://open.spotify.com/album/6jrlncx29wFsRc1RzAmSJ1)  
[PLAY WIT BRAINZ (2024)](https://open.spotify.com/album/5dFrLqTiyxaH6LcuIQg6z0)  
[RAGE (2024)](https://open.spotify.com/album/05IpSqxPS21KemQVRH0kWW)  
[GET BACK (2024)](https://open.spotify.com/album/1AlunGB3eJm2YP38SP3KVj)  
[OUT THE GATE (2024)](https://open.spotify.com/album/1ln4Uspsd3fzW0XxfJzNkV)  
[3-D (2024)](https://open.spotify.com/album/6LefUIwERGJCmAk26R463J)  
[HorrorCrunk In My Trunk (2024)](https://open.spotify.com/album/0RHUVaWHZGSaUJEoKg864j)  
[Welcome To The South (2024)](https://open.spotify.com/album/617AGfI79Jb0bhiCSIQzqf)  
[Reign Terror (2023)](https://open.spotify.com/album/3S8xkqGMr0Km0NlQFM7v2g)  
[Bloodsuckers (2023)](https://open.spotify.com/album/54ly6Sfv6krcsPOO1r2wMQ)  
[2 Pillar's (2023)](https://open.spotify.com/album/3ZmMnJjsN0ISEOg62KfgUO)  
[Steppers (2023)](https://open.spotify.com/album/43zuHUEggiF3ncNrcPj7s3)
""")

# MEMBERS
elif menu == "The Cult (Members)":

    st.markdown("## 💀 THE CULT 💀")

    col1,col2 = st.columns([1,3])
    with col1:
        st.image("pic5.jpg")
    with col2:
        st.markdown("""
### Lord-K-Haos  
MC | Lyricist | Co-Founder  

The chaos incarnate. Delivering dark southern horrorcore with raw aggression and underground authenticity.
""")

    col1,col2 = st.columns([1,3])
    with col1:
        st.image("img12.jpg")
    with col2:
        st.markdown("""
### Crazy8 The Snap Case  
MC | Producer | Co-Founder  

Unpredictable energy and gritty production. Architect of the Hellbound Disciplez sound.
""")

    col1,col2 = st.columns([1,3])
    with col1:
        st.image("img11.jpg")
    with col2:
        st.markdown("""
### Osomane  
Producer  

Dark atmospheric production and southern phonk influence shaping the group's sonic identity.
""")

# PHOTOS
elif menu == "The Catacombs (Photos)":

    st.markdown("## 💀 THE CATACOMBS 💀")

    photos = [
        "pic1.png",
        "pic2.png",
        "pic3.png",
        "pic4.png",
        "pic5.jpg",
        "pic6.png",
        "pic7.jpg",
        "pic8.jpeg",
        "pic9.jpeg",
        "pic10.png",
        "pic11.jpeg"
    ]

    for img in photos:
        st.image(img)
