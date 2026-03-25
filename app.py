import streamlit as st
import base64
import random
from PIL import Image
import io
import streamlit.components.v1 as components

@st.cache_data(show_spinner=False)
def get_image_base64(filename):
    with open(filename, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

@st.cache_data(show_spinner=False)
def get_image_base64_resized(filename, size=(64, 64)):
    img = Image.open(filename).convert("RGBA")
    img = img.resize(size, Image.LANCZOS)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

@st.cache_data(show_spinner=False)
def get_image_base64_resized_flipped(filename, size=(64, 64)):
    img = Image.open(filename).convert("RGBA")
    img = img.resize(size, Image.LANCZOS)
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

@st.cache_data(show_spinner=False)
def get_image_base64_transparent(filename, opacity=0.5):
    img = Image.open(filename).convert("RGBA")
    r, g, b, a = img.split()
    a = a.point(lambda x: int(x * opacity))
    img = Image.merge("RGBA", (r, g, b, a))
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

@st.cache_data(show_spinner=False)
def get_audio_base64(filename):
    with open(filename, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

@st.cache_data(show_spinner=False)
def get_font_base64(filename):
    with open(filename, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

@st.cache_data(show_spinner=False)
def get_shuffled_photos():
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
    return photos

bg_data = get_image_base64("BGSKULLS.png")
skull = get_image_base64("SKULL1.png")
shotgun = get_image_base64_resized_flipped("shotgun.png", size=(64, 64))
pistol = get_image_base64("pistol-removebg-preview.png")
logo = get_image_base64_transparent("HBDLOGO1.png", opacity=0.5)
reload_snd = get_audio_base64("reload.wav")
shotty_snd = get_audio_base64("shottyblast.wav")
font_baroness = get_font_base64("BaronessKuffner.ttf")
font_glitch = get_font_base64("DoctorGlitch.otf")

st.set_page_config(page_title="HELLBOUND DISCIPLEZ", page_icon="🤘", layout="wide")

st.markdown(f"""
<style>
@font-face {{
    font-family: 'BaronessKuffner';
    src: url("data:font/truetype;base64,{font_baroness}") format('truetype');
    font-weight: normal;
    font-style: normal;
    font-display: swap;
}}

@font-face {{
    font-family: 'DoctorGlitch';
    src: url("data:font/otf;base64,{font_glitch}") format('opentype');
    font-weight: normal;
    font-style: normal;
    font-display: swap;
}}

*, html, body, .stApp, [data-testid="stSidebar"], .stApp * {{
    cursor: url("data:image/png;base64,{shotgun}") 10 4, auto !important;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    box-sizing: border-box;
}}

.main *, [data-testid="stSidebar"] label {{
    font-family: 'BaronessKuffner', cursive !important;
}}

h1, h2, h3, h4, h5, h6,
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {{
    font-family: 'DoctorGlitch', cursive !important;
}}

::-webkit-scrollbar {{ width: 8px; }}
::-webkit-scrollbar-track {{ background: #000000; }}
::-webkit-scrollbar-thumb {{ background: #ff2200; border-radius: 4px; }}
::-webkit-scrollbar-thumb:hover {{ background: #ff5500; }}

.stApp {{
    background-image: url("data:image/png;base64,{bg_data}");
    background-size: cover;
    background-repeat: repeat;
    background-attachment: fixed;
    color: #ff2200;
    will-change: transform;
}}

[data-testid="stSidebar"] {{
    background-image: url("data:image/png;base64,{bg_data}");
    background-size: cover;
    background-repeat: repeat;
    will-change: transform;
}}

h1,h2,h3,h4,h5,h6,p,label {{
    color: #ff2200 !important;
}}

a {{
    color: #ff2200 !important;
    text-decoration: none;
    transition: color 0.2s ease, text-shadow 0.2s ease;
    will-change: color;
    font-family: 'BaronessKuffner', cursive !important;
}}
a:hover {{
    color: #ff5500 !important;
    text-shadow: 0 0 10px #ff2200;
}}

p, div, span, li {{
    font-family: 'BaronessKuffner', cursive !important;
}}

img {{
    image-rendering: -webkit-optimize-contrast;
    transform: translateZ(0);
}}

@keyframes navPulse {{
    0%, 100% {{ opacity: 1; transform: translateX(0); }}
    50% {{ opacity: 0.6; transform: translateX(3px); }}
}}

#nav-hint {{
    position: fixed;
    top: 80px;
    left: 8px;
    z-index: 9999;
    display: flex;
    align-items: center;
    gap: 6px;
    background: rgba(0,0,0,0.75);
    border: 1px solid #ff2200;
    border-radius: 6px;
    padding: 6px 12px;
    animation: navPulse 2s ease-in-out infinite;
    box-shadow: 0 0 10px rgba(255,34,0,0.5);
}}

#nav-hint span.arrow {{
    font-size: 20px;
    color: #ff2200;
    font-weight: bold;
    line-height: 1;
}}

#nav-hint span.text {{
    font-family: 'DoctorGlitch', cursive !important;
    font-size: 16px;
    color: #ff2200;
    letter-spacing: 1px;
    white-space: nowrap;
    -webkit-text-stroke: 0.3px white;
}}

@keyframes vhs-shake {{
    0%   {{ transform: translate(0,0) skewX(0deg); filter: none; }}
    10%  {{ transform: translate(-6px,3px) skewX(-3deg); filter: hue-rotate(90deg) saturate(3) brightness(1.4); }}
    20%  {{ transform: translate(6px,-3px) skewX(3deg); filter: hue-rotate(180deg) saturate(4) brightness(0.8); }}
    30%  {{ transform: translate(-4px,5px) skewX(-2deg); filter: hue-rotate(270deg) saturate(5) brightness(1.6) blur(1px); }}
    40%  {{ transform: translate(8px,-2px) skewX(4deg); filter: hue-rotate(0deg) saturate(6) brightness(0.6) blur(2px); }}
    50%  {{ transform: translate(-8px,4px) skewX(-4deg); filter: hue-rotate(120deg) saturate(8) brightness(1.8) blur(1px); }}
    60%  {{ transform: translate(4px,-5px) skewX(2deg); filter: hue-rotate(240deg) saturate(5) brightness(0.7); }}
    70%  {{ transform: translate(-6px,2px) skewX(-3deg); filter: hue-rotate(60deg) saturate(3) brightness(1.3); }}
    80%  {{ transform: translate(5px,-3px) skewX(2deg); filter: hue-rotate(180deg) saturate(4) brightness(1.1) blur(1px); }}
    90%  {{ transform: translate(-3px,4px) skewX(-1deg); filter: hue-rotate(300deg) saturate(2) brightness(0.9); }}
    100% {{ transform: translate(0,0) skewX(0deg); filter: none; }}
}}

@keyframes scanline-flash {{
    0%   {{ opacity: 0; }}
    20%  {{ opacity: 0.6; }}
    40%  {{ opacity: 0.2; }}
    60%  {{ opacity: 0.8; }}
    80%  {{ opacity: 0.3; }}
    100% {{ opacity: 0; }}
}}

.vhs-glitch-active {{
    animation: vhs-shake 0.5s steps(1, end) forwards !important;
}}

#vhs-overlay {{
    position: fixed; top: 0; left: 0;
    width: 100vw; height: 100vh;
    pointer-events: none; z-index: 999998;
    display: none;
    background: repeating-linear-gradient(
        0deg,
        rgba(255,0,0,0.08) 0px, rgba(255,0,0,0.08) 1px,
        transparent 1px, transparent 3px
    );
    will-change: opacity;
}}
#vhs-overlay.active {{
    display: block;
    animation: scanline-flash 0.5s steps(1, end) forwards;
}}

#vhs-rgb-r, #vhs-rgb-b {{
    position: fixed; top: 0; left: 0;
    width: 100vw; height: 100vh;
    pointer-events: none; z-index: 999997;
    display: none; mix-blend-mode: screen;
    will-change: opacity;
}}
#vhs-rgb-r {{ background: rgba(255,0,0,0.15); }}
#vhs-rgb-b {{ background: rgba(0,0,255,0.15); }}
#vhs-rgb-r.active, #vhs-rgb-b.active {{
    display: block;
    animation: scanline-flash 0.5s steps(1, end) forwards;
}}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div id="nav-hint">
    <span class="arrow">☰</span>
    <span class="text">TAP ARROW TO NAVIGATE</span>
</div>
<div id="vhs-overlay"></div>
<div id="vhs-rgb-r"></div>
<div id="vhs-rgb-b"></div>
""", unsafe_allow_html=True)

components.html(f"""
<script>
var reloadAudio = new Audio("data:audio/wav;base64,{reload_snd}");
var shottyAudio = new Audio("data:audio/wav;base64,{shotty_snd}");
reloadAudio.volume = 0.64;
shottyAudio.volume = 0.64;

function playReload() {{ reloadAudio.currentTime = 0; reloadAudio.play(); }}
function playShotty() {{ shottyAudio.currentTime = 0; shottyAudio.play(); }}

function triggerVHS() {{
    var doc = window.parent.document;
    var app = doc.querySelector(".stApp");
    var overlay = doc.getElementById("vhs-overlay");
    var rgbR = doc.getElementById("vhs-rgb-r");
    var rgbB = doc.getElementById("vhs-rgb-b");

    [app, overlay, rgbR, rgbB].forEach(function(el) {{
        if (!el) return;
        el.classList.remove("vhs-glitch-active", "active");
        void el.offsetWidth;
        el.classList.add(el === app ? "vhs-glitch-active" : "active");
        setTimeout(function() {{
            el.classList.remove("vhs-glitch-active", "active");
        }}, 500);
    }});
}}

var doc = window.parent.document;
doc.addEventListener("click", function() {{ playShotty(); triggerVHS(); }});

function attachHoverSounds() {{
    var clickables = doc.querySelectorAll("a, button, [role='radio'], [role='button'], label");
    clickables.forEach(function(el) {{
        if (!el.dataset.soundAttached) {{
            el.addEventListener("mouseenter", playReload);
            el.dataset.soundAttached = "true";
        }}
    }});
}}

attachHoverSounds();
setInterval(attachHoverSounds, 1500);
</script>
""", height=0)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(f'<img src="data:image/png;base64,{logo}" width="500" style="display:block;margin:auto;transform:translateZ(0);">', unsafe_allow_html=True)

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
    st.markdown(f"""
    <div style="text-align:center;font-size:28px;font-family:'DoctorGlitch',cursive;">
    <img src="data:image/png;base64,{pistol}" width="60">
    <b> WHO ARE WE </b>
    <img src="data:image/png;base64,{pistol}" width="60" style="transform:scaleX(-1);">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
<div style="text-align:center;font-family:'BaronessKuffner',cursive;">
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
<div style="text-align:center;font-size:28px;font-family:'DoctorGlitch',cursive;">
<img src="data:image/png;base64,{skull}" width="78" style="vertical-align:middle;margin-right:-4px;"><b> THE GRIMOIRES (Discography) </b><img src="data:image/png;base64,{skull}" width="78" style="vertical-align:middle;margin-left:-4px;transform:scaleX(-1);">
</div>
<div style="text-align:center;margin-top:20px;font-family:'DoctorGlitch',cursive;">📀 Albums / Mixtapes / EPs</div>
<div style="text-align:center;font-family:'BaronessKuffner',cursive;">
<a href="https://open.spotify.com/album/6ZOUHhIAnS532EdK1ZaLtv" target="_blank">Tales From The Swamp</a> (2025) — 8 tracks<br>
<a href="https://open.spotify.com/album/43O3pIiiwtOhcd9VANWjga" target="_blank">Hellbound Disciplez (Self Titled)</a> (2023) — 15 tracks<br>
<a href="https://open.spotify.com/album/2smEfqlW4Z16AUD5md7UxZ" target="_blank">21 Grams Lighter</a> (2022) — 10 tracks<br>
<a href="https://open.spotify.com/album/0LW0Gp5neAyHtihn5pxteR" target="_blank">The Godless Mixtape</a> (2022) — 11 tracks<br>
<a href="https://open.spotify.com/album/2jEHxL0P2uHT6SPokLnayC" target="_blank">Glitch Tape Vol.1</a> (2023) — 7 tracks<br>
<a href="https://open.spotify.com/album/1AoyhHGiy4PE6b9HIdfWRu" target="_blank">Pumpkin Patch Massacre</a> (2023)
</div>
<div style="text-align:center;margin-top:25px;font-family:'DoctorGlitch',cursive;">
<img src="data:image/png;base64,{skull}" width="78" style="vertical-align:middle;margin-right:-4px;"><b> Singles </b><img src="data:image/png;base64,{skull}" width="78" style="vertical-align:middle;margin-left:-4px;transform:scaleX(-1);">
</div>
<div style="text-align:center;font-family:'BaronessKuffner',cursive;">
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
<div style="text-align:center;margin-top:25px;font-family:'BaronessKuffner',cursive;">
🔥 Follow / Stream Hellbound Disciplez<br><br>
<a href="https://open.spotify.com/artist/5hRvzAL7q1as1y5FqKEaGZ" target="_blank">Spotify</a><br>
<a href="https://music.apple.com/us/artist/hellbound-disciplez/1641539761" target="_blank">Apple Music</a><br>
<a href="https://music.amazon.com/artists/B0BBSJ6W1Z/hellbound-disciplez" target="_blank">Amazon Music</a><br>
<a href="https://www.facebook.com/profile.php?id=100091797215709" target="_blank">Facebook</a><br>
<a href="https://www.instagram.com/hellbound_disciplez?igsh=dmV1bjc5NmZoazh0" target="_blank">Instagram</a>
</div>
""", unsafe_allow_html=True)

elif menu == "The Cult (Members)":
    st.markdown(f'<div style="text-align:center;font-size:28px;font-family:\'DoctorGlitch\',cursive;"><img src="data:image/png;base64,{skull}" width="78" style="vertical-align:middle;margin-right:-4px;"><b> THE CULT </b><img src="data:image/png;base64,{skull}" width="78" style="vertical-align:middle;margin-left:-4px;transform:scaleX(-1);"></div>', unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("pic5.jpg", width=150)
    with col2:
        st.subheader("🔥 Lord-K-Haos")
        st.markdown('<p style="font-family:\'BaronessKuffner\',cursive;">MC | Lyricist | Co-Founder — The chaos incarnate. Lord-K-Haos brings the darkness with razor sharp lyricism and an iron grip on the mic.</p>', unsafe_allow_html=True)

    st.markdown("---")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("img12.jpg", width=150)
    with col2:
        st.subheader("🔥 Crazy8 The Snap Case")
        st.markdown('<p style="font-family:\'BaronessKuffner\',cursive;">MC | Lyricist | Producer | Co-Founder — Raw, unfiltered, and unpredictable. Crazy8 The Snap Case delivers horrorcore at its most visceral while helping craft the sonic backbone of the group alongside Osomane.</p>', unsafe_allow_html=True)

    st.markdown("---")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("img11.jpg", width=150)
    with col2:
        st.subheader("🔥 Osomane")
        st.markdown('<p style="font-family:\'BaronessKuffner\',cursive;">Producer | Member — The architect of the sound. Osomane works hand in hand with Crazy8 to build the dark, gritty beats that bring the Hellbound Disciplez vision to life.</p>', unsafe_allow_html=True)

elif menu == "The Catacombs (Photos)":
    st.markdown(f'<div style="text-align:center;font-size:28px;font-family:\'DoctorGlitch\',cursive;"><img src="data:image/png;base64,{skull}" width="78" style="vertical-align:middle;margin-right:-4px;"><b> THE CATACOMBS </b><img src="data:image/png;base64,{skull}" width="78" style="vertical-align:middle;margin-left:-4px;transform:scaleX(-1);"></div>', unsafe_allow_html=True)
    st.markdown("---")

    photos = get_shuffled_photos()
    cols = st.columns(2)
    for i, photo_path in enumerate(photos):
        with cols[i % 2]:
            st.image(photo_path, use_container_width=True)
