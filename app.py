import streamlit as st
import base64
import random

def get_image_base64(filename):
    with open(filename, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

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

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("HBDLOGO1.png", width=490)
    st.subheader("Official Underground Hub")
    st.markdown("---")

with st.sidebar:
    st.header("THE VOID")
    menu = st.radio("Navigate:", [
        "The Ritual (Home)",
        "The Discography",
        "The Cult (Members)",
        "The Catacombs (Photos)"
    ])

if menu == "The Ritual (Home)":
    st.header("☠️ WHO WE ARE ☠️")
    st.markdown("""
Forged in the depths of the underground, Hellbound Disciplez is a formidable trio consisting of **Lord-K-Haos**, **Crazy8 The Snap Case**, and **Osomane**. Independent and unbothered, these three sonic provocateurs blaze their own trail. With a sound that's equal parts gritty phonk and horrorcore, they paint vivid portraits of America's dark underbelly - exploring themes of the occult, street life, and true crime. Fueled by the collaborative production of Osomane and Crazy8 The Snap Case, and the raw lyricism of the whole crew, their music is a haunting reflection of the shadows that lurk just beyond the edge of society. Get ready to descend into the abyss with Hellbound Disciplez.
""")

    st.markdown("---")
    st.subheader("🔥 Deep South, United States 🔥")
    st.markdown("---")
    st.subheader("⚡ Glitch Tape Vol. 2 — Coming Soon ⚡")


elif menu == "The Discography":
    st.header("💀 THE DISCOGRAPHY 💀")
    st.markdown("---")

    st.subheader("📀 Releases")
    st.markdown("""
- [Counterfeit](https://open.spotify.com/album/1Cnug15A07CIImqFiprqVq)
- [Tales From The Swamp](https://open.spotify.com/album/03BObGWktQNHCLhoimV2lK)
- [Crowbar](https://open.spotify.com/album/5dFrLqTiyxaH6LcuIQg6z0)
- [My House](https://open.spotify.com/album/1AlunGB3eJm2YP38SP3KVj)
- [Evil](https://open.spotify.com/album/05IpSqxPS21KemQVRH0kWW)
- [Smoke](https://open.spotify.com/album/54ly6Sfv6krcsPOO1r2wMQ)
- [Play Wit Brainz](https://open.spotify.com/album/617AGfI79Jb0bhiCSIQzqf)
- [Rage](https://open.spotify.com/album/0RHUVaWHZGSaUJEoKg864j)
- [Get Back](https://open.spotify.com/album/1AlunGB3eJm2YP38SP3KVj)
- [Out The Gate](https://open.spotify.com/album/0LW0Gp5neAyHtihn5pxteR)
- [3-D](https://open.spotify.com/album/6jrlncx29wFsRc1RzAmSJ1)
- [HorrorCrunk In My Trunk](https://open.spotify.com/album/1ln4Uspsd3fzW0XxfJzNkV)
- [Welcome To The South](https://open.spotify.com/album/3ZmMnJjsN0ISEOg62KfgUO)
- [Reign Terror](https://open.spotify.com/album/2smEfqlW4Z16AUD5md7UxZ)
- [Bloodsuckers](https://open.spotify.com/album/43zuHUEggiF3ncNrcPj7s3)
- [2 Pillar's](https://open.spotify.com/album/43O3pIiiwtOhcd9VANWjga)
- [Glitch Tape Vol 1](https://open.spotify.com/album/3S8xkqGMr0Km0NlQFM7v2g)
- [Steppers](https://open.spotify.com/album/0LW0Gp5neAyHtihn5pxteR)
- [21 Grams Lighter](https://open.spotify.com/album/40pDtzpR5i9jpvhjqNnidt)
- [Godless Mixtape Vol 1](https://open.spotify.com/album/1AoyhHGiy4PE6b9HIdfWRu)
- [Hellbound Disciplez (Self Titled)](https://open.spotify.com/album/6ZOUHhIAnS532EdK1ZaLtv)
""")

    st.markdown("---")

    st.subheader("🔥 Follow Hellbound Disciplez")
    st.markdown("""
🎧 [Spotify](https://open.spotify.com/artist/5hRvzAL7q1as1y5FqKEaGZ)

📘 [Facebook](https://www.facebook.com/profile.php?id=100091797215709)
""")


elif menu == "The Cult (Members)":
    st.header("💀 THE CULT 💀")
    st.markdown("---")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("pic5.jpg", width=150)
    with col2:
        st.subheader("🔥 Lord-K-Haos")
        st.markdown("MC | Lyricist | Co-Founder — The chaos incarnate.")

    st.markdown("---")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("img12.jpg", width=150)
    with col2:
        st.subheader("🔥 Crazy8 The Snap Case")
        st.markdown("MC | Lyricist | Producer | Co-Founder")

    st.markdown("---")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("img11.jpg", width=150)
    with col2:
        st.subheader("🔥 Osomane")
        st.markdown("Producer | Member")


elif menu == "The Catacombs (Photos)":
    st.header("💀 THE CATACOMBS 💀")
    st.markdown("---")

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
