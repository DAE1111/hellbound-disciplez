import streamlit as st
import base64
import random
from PIL import Image
import io

def get_image_base64(filename):
    with open(filename, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def get_image_base64_resized(filename, size=(64, 64)):
    img = Image.open(filename).convert("RGBA")
    img = img.resize(size, Image.LANCZOS)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

bg_data = get_image_base64("BGSKULLS.png")
skull = get_image_base64("SKULL1.png")
knife = get_image_base64_resized("KNIFE1.png", size=(64, 64))

st.set_page_config(page_title="HELLBOUND DISCIPLEZ", page_icon="🤘", layout="wide")

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Creepster&display=swap');

*, html, body, .stApp, [data-testid="stSidebar"], .stApp * {{
    cursor: url("data:image/png;base64,{knife}") 0 16, auto !important;
}}

.main *, [data-testid="stSidebar"] h1, [data-testid="stSidebar"] label {{
    font-family: 'Creepster', cursive !important;
}}

::-webkit-scrollbar {{
    width: 8px;
}}
::-webkit-scrollbar-track {{
    background: #000000;
}}
::-webkit-scrollbar-thumb {{
    background: #ff2200;
    border-radius: 4px;
}}
::-webkit-scrollbar-thumb:hover {{
    background: #ff5500;
}}

.stApp {{
    background-image: url("data:image/png;base64,{bg_data}");
    background-size: cover;
    background-repeat: repeat;
    background-attachment: fixed;
    color:#ff2200;
}}
[data-testid="stSidebar"] {{
    background-image: url("data:image/png;base64,{bg_data}");
    background-size: cover;
    background-repeat: repeat;
}}
h1,h2,h3,h4,h5,h6,p,label {{
    color:#ff2200 !important;
    font-family: 'Creepster', cursive !important;
}}
a {{
    color: #ff2200 !important;
    text-decoration: none;
    transition: all 0.3s ease;
}}
a:hover {{
    color: #ff5500 !important;
    text-shadow: 0 0 10px #ff2200;
}}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div style="position:fixed;top:60px;left:10px;font-family:Georgia,serif;color:#4a90d9;font-size:12px;z-index:9999;">☰ Tap arrow to navigate</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("HBDLOGO1.png", width=500)

with st.sidebar:
    st.header("THE VOID")
    menu = st.radio(
        "",
        [
            "The Ritual (Home)",
            "The Grimoires (Discography)",
            "The Cult (Members)",
            "The Catacombs (Photos)"
        ]
    )

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

Forged in the depths of the underground, Hellbound Disciplez is a formidable trio consisting of
<b>Lord-K-Haos</b>, <b>Crazy8 The Snap Case</b>, and <b>Osomane</b>. Independent and unbothered,
these three sonic provocateurs blaze their own trail. With a sound that's equal parts gritty phonk
and horrorcore, they paint vivid portraits of America's dark underbelly - exploring themes of the
occult, street life, and true crime. Fueled by the collaborative production of Osomane and Crazy8
The Snap Case, and the raw lyricism of the whole crew, their music is a haunting reflection of the
shadows that lurk just beyond the edge of society. Get ready to descend into the abyss with
Hellbound Disciplez.
<br><br>
🔥 Deep South, United States 🔥
<br><br>
⚡ Glitch Tape Vol. 2 — Coming Soon ⚡

</div>
""", unsafe_allow_html=True)

elif menu == "The Grimoires (Discography)":

    st.markdown(f"""
<div style="text-align:center;font-size:28px;">
<img src="data:image/png;base64,{skull}" width="78" style="vertical-align:middle;margin-right:-4px;"><b> THE GRIMOIRES (Discography) </b><img src="data:image/png;base64,{skull}" width="78" style="vertical-align:middle;margin-left:-4px;transform:scaleX(-1);">
</div>

<div style="text-align:center;margin-top:20px;">
📀 Albums / Mixtapes / EPs
</div>

<div style="text-align:center;">

<a href="https://open.spotify.com/album/6ZOUHhIAnS532EdK1ZaLtv" target="_blank">Tales From The Swamp</a> (2025) — 8 tracks<br>
<a href="https://open.spotify.com/album/43O3pIiiwtOhcd9VANWjga" target="_blank">Hellbound Disciplez (Self Titled)</a> (2023) — 15 tracks<br>
<a href="https://open.spotify.com/album/2smEfqlW4Z16AUD5md7UxZ" target="_blank">21 Grams Lighter</a> (2022) — 10 tracks<br>
<a href="https://open.spotify.com/album/0LW0Gp5neAyHtihn5pxteR" target="_blank">The Godless Mixtape</a> (2022) — 11 tracks<br>
<a href="https://open.spotify.com/album/2jEHxL0P2uHT6SPokLnayC" target="_blank">Glitch Tape Vol.1</a> (2023) — 7 tracks<br>
<a href="https://open.spotify.com/album/1AoyhHGiy4PE6b9HIdfWRu" target="_blank">Pumpkin Patch Massacre</a> (2023)

</div>

<div style="text-align:center;margin-top:25px;">
<img src="data:image/png;base64,{skull}" width="78" style="vertical-align:middle;margin-right:-4px;"><b> Singles </b><img src="data:image/png;base64,{skull}" width="78" style="vertical-align:middle;margin-left:-4px;transform:scaleX(-1);">
</div>

<div style="text-align:center;">

<a href="https://open.spotify.com/album/03BObGWktQNHCLhoimV2lK" target="_blank">COUNTERFEIT</a> (2025)<br>
<a href="https://open.spotify.com/album/4EU2f7tAo6DWhERyavT37j" target="_blank">Crowbar</a> (2024)<br>
<a href="https://open.spotify.com/album/40pDtzpR5i9jpvhjqNnidt" target="_blank">My House</a> (2024)<br>
<a href="https://open.spotify.com/album/1Cnug15A07CIImqFiprqVq" target="_blank">Evil</a> (2024)<br>
<a href="https://open.spotify.com/album/6jrlncx29wFsRc1RzAmSJ1" target="_blank">Smoke</a> (2024)<br>
<a href="https://open.spotify.com/album/5dFrLqTiyxaH6LcuIQg6z0" target="_blank">Play Wit Brainz</a> (2024)<br>
<a href="https://open.spotify.com/album/05IpSqxPS21KemQVRH0kWW" target="_blank">RAGE</a> (2024)<br>
<a href="https://open.spotify.com/album/1AlunGB3eJm2YP38SP3KVj" target="_blank">Get Back</a> (2024)<br>
<a href="https://open.spotify.com/album/1ln4Uspsd3fzW0XxfJzNkV" target="_blank">Out The Gate</a> (2024)<br>
<a href="https://open.spotify.com/album/6LefUIwERGJCmAk26R463J" target="_blank">3-D</a> (2024)<br>
<a href="https://open.spotify.com/album/0RHUVaWHZGSaUJEoKg864j" target="_blank">HorrorCrunk In My Trunk</a> (2024)<br>
<a href="https://open.spotify.com/album/617AGfI79Jb0bhiCSIQzqf" target="_blank">Welcome To The South</a> (2024)<br>
<a href="https://open.spotify.com/album/3S8xkqGMr0Km0NlQFM7v2g" target="_blank">REIGN TERROR</a> (2023)<br>
<a href="https://open.spotify.com/album/54ly6Sfv6krcsPOO1r2wMQ" target="_blank">Bloodsuckers</a> (2023)<br>
<a href="https://open.spotify.com/album/3ZmMnJjsN0ISEOg62KfgUO" target="_blank">2 Pillar's</a> (2023)<br>
<a href="https://open.spotify.com/album/43zuHUEggiF3ncNrcPj7s3" target="_blank">Steppers</a> (2023)

</div>

<div style="text-align:center;margin-top:25px;">

🔥 Follow / Stream Hellbound Disciplez<br><br>

<a href="https://open.spotify.com/artist/5hRvzAL7q1as1y5FqKEaGZ" target="_blank">Spotify</a><br>
<a href="https://music.apple.com/us/artist/hellbound-disciplez/1641539761" target="_blank">Apple Music</a><br>
<a href="https://music.amazon.com/artists/B0BBSJ6W1Z/hellbound-disciplez" target="_blank">Amazon Music</a><br>
<a href="https://www.facebook.com/profile.php?id=100091797215709" target="_blank">Facebook</a><br>
<a href="https://www.instagram.com/hellbound_disciplez?igsh=dmV1bjc5NmZoazh0" target="_blank">Instagram</a>

</div>
""", unsafe_allow_html=True)

elif menu == "The Cult (Members)":

    st.markdown(f'<div style="text-align:center;font-size:28px;"><img src="data:image/png;base64,{skull}" width="78" style="vertical-align:middle;margin-right:-4px;"><b> THE CULT </b><img src="data:image/png;base64,{skull}" width="78" style="vertical-align:middle;margin-left:-4px;transform:scaleX(-1);"></div>', unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("pic5.jpg", width=150)
    with col2:
        st.subheader("🔥 Lord-K-Haos")
        st.markdown("MC | Lyricist | Co-Founder — The chaos incarnate. Lord-K-Haos brings the darkness with razor sharp lyricism and an iron grip on the mic.")

    st.markdown("---")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("img12.jpg", width=150)
    with col2:
        st.subheader("🔥 Crazy8 The Snap Case")
        st.markdown("MC | Lyricist | Producer | Co-Founder — Raw, unfiltered, and unpredictable. Crazy8 The Snap Case delivers horrorcore at its most visceral while helping craft the sonic backbone of the group alongside Osomane.")

    st.markdown("---")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("img11.jpg", width=150)
    with col2:
        st.subheader("🔥 Osomane")
        st.markdown("Producer | Member — The architect of the sound. Osomane works hand in hand with Crazy8 to build the dark, gritty beats that bring the Hellbound Disciplez vision to life.")

elif menu == "The Catacombs (Photos)":

    st.markdown(f'<div style="text-align:center;font-size:28px;"><img src="data:image/png;base64,{skull}" width="78" style="vertical-align:middle;margin-right:-4px;"><b> THE CATACOMBS </b><img src="data:image/png;base64,{skull}" width="78" style="vertical-align:middle;margin-left:-4px;transform:scaleX(-1);"></div>', unsafe_allow_html=True)
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
