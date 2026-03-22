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

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("HBDLOGO1.png", width=490)

st.subheader("Official Underground Hub")
st.markdown("---")

with st.sidebar:
    st.header("THE VOID")
    menu = st.radio("Navigate:", ["The Ritual (Home)", "The Discography", "The Cult (Members)", "The Catacombs (Photos)"])

if menu == "The Ritual (Home)":
    st.header("☠️ WHO WE ARE ☠️")
    st.markdown("""
    Forged in the depths of the underground, Hellbound Disciplez is a formidable trio consisting of
    **Lord-K-Haos**, **Crazy8 The Snap Case**, and **Osomane**. Independent and unbothered, these three sonic
    provocateurs blaze their own trail. With a sound that's equal parts gritty phonk and horrorcore,
    they paint vivid portraits of America's dark underbelly - exploring themes of the occult, street
    life, and true crime. Fueled by the collaborative production of Osomane and Crazy8 The Snap Case,
    and the raw lyricism of the whole crew, their music is a haunting reflection of the shadows that
    lurk just beyond the edge of society. Get ready to descend into the abyss with Hellbound Disciplez.
    """)
    st.markdown("---")
    st.subheader("🔥 Deep South, United States 🔥")

elif menu == "The Discography":
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
    st.markdown("""
- **Pumpkin Patch Massacre EP** (2023) — 5 tracks (with Con-Crete)
    """)

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

elif menu == "The Cult (Members)":
    st.header("💀 THE CULT 💀")
    st.markdown("---")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("New folder/pic5.jpg", width=150)
    with col2:
        st.subheader("🔥 Lord-K-Haos")
        st.markdown("MC | Lyricist | Co-Founder — The chaos incarnate. Lord-K-Haos brings the darkness with razor sharp lyricism and an iron grip on the mic.")

    st.markdown("---")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("New folder/img12.jpg", width=150)
    with col2:
        st.subheader("🔥 Crazy8 The Snap Case")
        st.markdown("MC | Lyricist | Producer | Co-Founder — Raw, unfiltered, and unpredictable. Crazy8 The Snap Case delivers horrorcore at its most visceral while helping craft the sonic backbone of the group alongside Osomane.")

    st.markdown("---")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("New folder/img11.jpg", width=150)
    with col2:
        st.subheader("🔥 Osomane")
        st.markdown("Producer | Member — The architect of the sound. Osomane works hand in hand with Crazy8 to build the dark, gritty beats that bring the Hellbound Disciplez vision to life.")

elif menu == "The Catacombs (Photos)":
    st.header("💀 THE CATACOMBS 💀")
    st.markdown("---")

    photos = [
        "New folder/pic1.png",
        "New folder/pic2.png",
        "New folder/pic3.png",
        "New folder/pic4.png",
        "New folder/pic5.jpg",
        "New folder/pic6.png",
        "New folder/pic7.jpg",
        "New folder/pic8.jpeg",
        "New folder/pic9.jpeg",
        "New folder/pic10.png",
        "New folder/pic11.jpeg",
        "New folder/pic12.jpeg",
        "New folder/pic13.jpeg",
        "New folder/pic14.jpeg",
        "New folder/pic15.jpeg",
        "New folder/pic16.jpeg",
        "New folder/pic17.jpeg",
        "New folder/pic18.jpeg",
        "New folder/pic20.png",
        "New folder/pic21.png",
        "New folder/pic22.png",
        "New folder/pic23.jpg",
        "New folder/pic24.png",
        "New folder/pic25.jpg",
        "New folder/pic26.jpg",
        "New folder/pic27.jpg",
        "New folder/pic28.jpg",
        "New folder/pic29.jpg",
        "New folder/pic30.jpg",
        "New folder/pic31.jpg",
        "New folder/pic32.jpg",
        "New folder/pic33.jpg",
        "New folder/pic34.jpg",
        "New folder/pic35.jpg",
        "New folder/pic36.jpg",
        "New folder/pic37.jpg",
        "New folder/pic39.jpg",
        "New folder/pic40.jpg",
        "New folder/pic41.jpg",
        "New folder/img1.jpg",
        "New folder/img2.jpg",
        "New folder/img3.jpg",
        "New folder/img4.jpg",
        "New folder/img5.jpg",
        "New folder/img6.jpg",
        "New folder/img7.jpg",
        "New folder/img8.jpg",
        "New folder/img9.jpg",
        "New folder/img10.jpg",
        "New folder/img11.jpg",
    ]

    random.shuffle(photos)

    cols = st.columns(2)
    for i, photo_path in enumerate(photos):
        with cols[i % 2]:
            st.image(photo_path, use_container_width=True)
