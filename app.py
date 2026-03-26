import streamlit as st
import base64
import random
from PIL import Image
import io
import wave
import struct
import streamlit.components.v1 as components

# ─── Asset Loaders (all cached) ───────────────────────────────────────────────

@st.cache_data(show_spinner=False)
def get_image_base64(filename):
    with open(filename, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

@st.cache_data(show_spinner=False)
def get_image_base64_resized_flipped(filename, size=(64, 64)):
    img = Image.open(filename).convert("RGBA")
    img = img.resize(size, Image.LANCZOS)
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode("utf-8")

@st.cache_data(show_spinner=False)
def get_image_base64_transparent(filename, opacity=0.5):
    img = Image.open(filename).convert("RGBA")
    r, g, b, a = img.split()
    a = a.point(lambda x: int(x * opacity))
    img = Image.merge("RGBA", (r, g, b, a))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode("utf-8")

@st.cache_data(show_spinner=False)
def get_audio_base64(filename):
    with open(filename, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

@st.cache_data(show_spinner=False)
def get_wav_trimmed_base64(filename):
    with wave.open(filename, "rb") as wf:
        n_channels = wf.getnchannels()
        sampwidth  = wf.getsampwidth()
        framerate  = wf.getframerate()
        n_frames   = wf.getnframes()
        raw_frames = wf.readframes(n_frames)
    fmt = {1: "b", 2: "h", 4: "i"}.get(sampwidth, "h")
    total_samples = n_frames * n_channels
    samples = list(struct.unpack(f"<{total_samples}{fmt}", raw_frames))
    threshold = 32 if sampwidth == 1 else 128
    last_nonsilent = len(samples) - 1
    while last_nonsilent > 0 and abs(samples[last_nonsilent]) < threshold:
        last_nonsilent -= 1
    trim_to     = ((last_nonsilent // n_channels) + 1) * n_channels
    trimmed_raw = struct.pack(f"<{trim_to}{fmt}", *samples[:trim_to])
    buf = io.BytesIO()
    with wave.open(buf, "wb") as out:
        out.setnchannels(n_channels)
        out.setsampwidth(sampwidth)
        out.setframerate(framerate)
        out.writeframes(trimmed_raw)
    return base64.b64encode(buf.getvalue()).decode("utf-8")

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
        "pic39.jpg","pic40.jpg","pic41.jpg",
        "img1.jpg","img2.jpg","img3.jpg","img4.jpg","img5.jpg","img6.jpg",
        "img7.jpg","img8.jpg","img9.jpg","img10.jpg","img11.jpg","img12.jpg",
    ]
    random.shuffle(photos)
    return photos

# ─── Load Assets ──────────────────────────────────────────────────────────────

bg_data       = get_image_base64("BGSKULLS.png")
skull         = get_image_base64("SKULL1.png")
shotgun       = get_image_base64_resized_flipped("shotgun.png", size=(64, 64))
pistol        = get_image_base64("pistol-removebg-preview.png")
logo          = get_image_base64_transparent("HBDLOGO1.png", opacity=0.5)
reload_snd    = get_audio_base64("reload.wav")
shotty_snd    = get_audio_base64("shottyblast.wav")
web_beat      = get_wav_trimmed_base64("WEB_BEAT_001.wav")
font_baroness = get_font_base64("BaronessKuffner.ttf")
font_glitch   = get_font_base64("DoctorGlitch.otf")

# ─── Page Config ──────────────────────────────────────────────────────────────

st.set_page_config(page_title="HELLBOUND DISCIPLEZ", page_icon="🤘", layout="wide", initial_sidebar_state="collapsed")

# ─── Prebuilt reusable strings ────────────────────────────────────────────────

BG_URL     = f'url("data:image/png;base64,{bg_data}")'
CURSOR_URL = f'url("data:image/png;base64,{shotgun}") 10 4, auto'

skull_s       = f'<img src="data:image/png;base64,{skull}" width="80" style="margin:0 8px;">'
skull_s_r     = f'<img src="data:image/png;base64,{skull}" width="80" style="margin:0 8px;transform:scaleX(-1);">'
skull_divider = f'<div class="skull-divider">{skull_s_r}{skull_s}{skull_s_r}</div>'
pistol_l      = f'<img src="data:image/png;base64,{pistol}" width="60" style="vertical-align:middle;">'
pistol_r      = f'<img src="data:image/png;base64,{pistol}" width="60" style="vertical-align:middle;transform:scaleX(-1);">'

# ─── CSS ──────────────────────────────────────────────────────────────────────

css = f"""
<style>
@import url('https://fonts.googleapis.com/icon?family=Material+Icons');

@font-face {{
  font-family:'BaronessKuffner';
  src:url("data:font/truetype;base64,{font_baroness}") format('truetype');
  font-display:swap;
}}
@font-face {{
  font-family:'DoctorGlitch';
  src:url("data:font/otf;base64,{font_glitch}") format('opentype');
  font-display:swap;
}}

*,html,body,.stApp,[data-testid="stSidebar"],.stApp * {{
  cursor:{CURSOR_URL} !important;
  -webkit-font-smoothing:antialiased;
  box-sizing:border-box;
}}

[data-testid="stSidebarCollapsedControl"] span,
[data-testid="stSidebarCollapsedControl"] button span,
[data-testid="stSidebarNavCollapseButton"] span,
[data-testid="collapsedControl"] span,
button[aria-label="Close sidebar"] span,
button[aria-label="Open sidebar"] span,
button[aria-label="collapse sidebar"] span,
button[aria-label="expand sidebar"] span,
button[aria-label="Collapse sidebar"] span,
button[aria-label="Expand sidebar"] span {{
  font-family:'Material Icons' !important;
  font-size:24px !important;
  font-style:normal !important;
  font-weight:normal !important;
  line-height:1 !important;
  letter-spacing:normal !important;
  text-transform:none !important;
  display:inline-block !important;
  white-space:nowrap !important;
  word-wrap:normal !important;
  direction:ltr !important;
  color:#ff2200 !important;
  -webkit-font-feature-settings:'liga' !important;
  font-feature-settings:'liga' !important;
  -webkit-font-smoothing:antialiased !important;
}}

@keyframes navPulse {{
  0%,100% {{ opacity:1; transform:translateX(0); }}
  50%      {{ opacity:0.6; transform:translateX(3px); }}
}}

#nav-hint {{
  position:fixed;top:80px;left:8px;z-index:9999;
  display:flex;align-items:center;gap:6px;
  background:rgba(0,0,0,0.75);border:1px solid #ff2200;
  border-radius:6px;padding:6px 12px;
  animation:navPulse 2s ease-in-out infinite;
  box-shadow:0 0 10px rgba(255,34,0,0.5);pointer-events:none;
}}
#nav-hint .nh-text {{
  font-family:'DoctorGlitch',cursive !important;
  font-size:16px;color:#ff2200;letter-spacing:1px;
  white-space:nowrap;-webkit-text-stroke:0.3px white;
}}

::-webkit-scrollbar       {{ width:8px; }}
::-webkit-scrollbar-track {{ background:#000; }}
::-webkit-scrollbar-thumb {{ background:#ff2200;border-radius:4px; }}
::-webkit-scrollbar-thumb:hover {{ background:#ff5500; }}

.stApp {{
  background-image:{BG_URL};
  background-size:cover;background-repeat:repeat;
  background-attachment:fixed;color:#ff2200;
}}
[data-testid="stSidebar"] {{
  background-image:{BG_URL};
  background-size:cover;background-repeat:repeat;
}}

img {{ transform:translateZ(0); }}

[data-testid="stMain"] p,
[data-testid="stMain"] li,
[data-testid="stMain"] a,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] li,
[data-testid="stSidebar"] label {{
  font-family:'BaronessKuffner',cursive !important;
  font-size:28px !important;color:#ff2200 !important;
}}

[data-testid="stMain"] h1,[data-testid="stMain"] h2,
[data-testid="stMain"] h3,[data-testid="stMain"] h4,
[data-testid="stMain"] h5,[data-testid="stMain"] h6,
[data-testid="stSidebar"] h1,[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {{
  font-family:'DoctorGlitch',cursive !important;color:#ff2200 !important;
}}

[data-testid="stMain"] a {{
  color:#ff2200 !important;text-decoration:none;transition:color 0.2s ease;
}}
[data-testid="stMain"] a:hover {{
  color:#ff5500 !important;text-shadow:0 0 10px #ff2200;
}}

@keyframes announcePulse {{
  0%,100% {{ text-shadow:0 0 10px #ff2200,0 0 20px #ff2200,0 0 40px #ff0000;letter-spacing:4px; }}
  50%      {{ text-shadow:0 0 20px #ff5500,0 0 40px #ff2200,0 0 80px #ff0000;letter-spacing:6px; }}
}}

.section-header {{
  font-family:'DoctorGlitch',cursive !important;
  font-size:28px !important;color:#ff2200 !important;
  -webkit-text-stroke:0.5px white;
  display:block;text-align:center;margin:10px 0;
}}
.skull-divider {{ display:block;text-align:center;margin:6px 0 18px 0; }}

.announce-text {{
  font-family:'DoctorGlitch',cursive !important;
  font-size:28px !important;color:#ff2200 !important;
  -webkit-text-stroke:0.5px white;
  animation:announcePulse 2s ease-in-out infinite;
  display:block;text-align:center;margin:10px 0;
}}

.glitch-tape-text {{
  font-family:'DoctorGlitch',cursive !important;
  font-size:28px !important;color:#ff2200 !important;
  -webkit-text-stroke:0.5px white;
  display:block;text-align:center;margin:10px 0;
}}

@keyframes vhs-shake {{
  0%   {{ transform:translate(0,0) skewX(0deg);filter:none; }}
  10%  {{ transform:translate(-6px,3px) skewX(-3deg);filter:hue-rotate(90deg) saturate(3) brightness(1.4); }}
  20%  {{ transform:translate(6px,-3px) skewX(3deg);filter:hue-rotate(180deg) saturate(4) brightness(0.8); }}
  30%  {{ transform:translate(-4px,5px) skewX(-2deg);filter:hue-rotate(270deg) saturate(5) brightness(1.6) blur(1px); }}
  40%  {{ transform:translate(8px,-2px) skewX(4deg);filter:hue-rotate(0deg) saturate(6) brightness(0.6) blur(2px); }}
  50%  {{ transform:translate(-8px,4px) skewX(-4deg);filter:hue-rotate(120deg) saturate(8) brightness(1.8) blur(1px); }}
  60%  {{ transform:translate(4px,-5px) skewX(2deg);filter:hue-rotate(240deg) saturate(5) brightness(0.7); }}
  70%  {{ transform:translate(-6px,2px) skewX(-3deg);filter:hue-rotate(60deg) saturate(3) brightness(1.3); }}
  80%  {{ transform:translate(5px,-3px) skewX(2deg);filter:hue-rotate(180deg) saturate(4) brightness(1.1) blur(1px); }}
  90%  {{ transform:translate(-3px,4px) skewX(-1deg);filter:hue-rotate(300deg) saturate(2) brightness(0.9); }}
  100% {{ transform:translate(0,0) skewX(0deg);filter:none; }}
}}

@keyframes scanline-flash {{
  0%  {{ opacity:0; }} 20% {{ opacity:0.6; }} 40% {{ opacity:0.2; }}
  60% {{ opacity:0.8; }} 80% {{ opacity:0.3; }} 100% {{ opacity:0; }}
}}

.vhs-glitch-active {{ animation:vhs-shake 0.5s steps(1,end) forwards !important; }}

#vhs-overlay {{
  position:fixed;top:0;left:0;width:100vw;height:100vh;
  pointer-events:none;z-index:999998;display:none;
  background:repeating-linear-gradient(
    0deg,rgba(255,0,0,0.08) 0px,rgba(255,0,0,0.08) 1px,
    transparent 1px,transparent 3px);
}}
#vhs-overlay.active {{ display:block;animation:scanline-flash 0.5s steps(1,end) forwards; }}

#vhs-rgb-r,#vhs-rgb-b {{
  position:fixed;top:0;left:0;width:100vw;height:100vh;
  pointer-events:none;z-index:999997;display:none;mix-blend-mode:screen;
}}
#vhs-rgb-r {{ background:rgba(255,0,0,0.15); }}
#vhs-rgb-b {{ background:rgba(0,0,255,0.15); }}
#vhs-rgb-r.active,#vhs-rgb-b.active {{
  display:block;animation:scanline-flash 0.5s steps(1,end) forwards;
}}

/* ── VHS Intro Screen ── */
#vhs-intro {{
  position:fixed;top:0;left:0;width:100vw;height:100vh;
  background:#000;z-index:9999999;
  display:flex;align-items:center;justify-content:center;
  flex-direction:column;transition:opacity 1s ease;
}}
#vhs-intro.fadeout {{ opacity:0;pointer-events:none; }}
#vhs-intro canvas {{ position:absolute;top:0;left:0;width:100%;height:100%; }}
#vhs-intro-text {{
  position:relative;z-index:2;
  font-family:'DoctorGlitch',cursive;
  font-size:48px;color:#ff2200;
  -webkit-text-stroke:1px white;
  text-align:center;letter-spacing:6px;
  animation:introFlicker 0.15s steps(1,end) infinite;
  text-shadow:0 0 20px #ff2200,0 0 40px #ff0000;
}}
#vhs-intro-sub {{
  position:relative;z-index:2;
  font-family:'DoctorGlitch',cursive;
  font-size:18px;color:#ff2200;
  letter-spacing:4px;margin-top:16px;
  opacity:0.7;animation:introFlicker 0.3s steps(1,end) infinite;
}}
#vhs-intro-scanlines {{
  position:absolute;top:0;left:0;width:100%;height:100%;
  background:repeating-linear-gradient(
    0deg,rgba(0,0,0,0.4) 0px,rgba(0,0,0,0.4) 1px,
    transparent 1px,transparent 4px);
  z-index:1;pointer-events:none;
}}
@keyframes introFlicker {{
  0%,89%  {{ opacity:1; }}
  90%     {{ opacity:0.2; }}
  91%     {{ opacity:1; }}
  94%     {{ opacity:0.4; }}
  95%     {{ opacity:1; }}
}}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# ─── VHS Intro Screen ─────────────────────────────────────────────────────────

st.markdown(
    """
    <div id="vhs-intro">
      <canvas id="vhs-static-canvas"></canvas>
      <div id="vhs-intro-scanlines"></div>
      <div id="vhs-intro-text">HELLBOUND DISCIPLEZ</div>
      <div id="vhs-intro-sub">&#9654; LOADING...</div>
    </div>
    <script>
    (function() {
      var canvas = document.getElementById('vhs-static-canvas');
      var ctx    = canvas.getContext('2d');
      var animId;

      function resize() {
        canvas.width  = window.innerWidth;
        canvas.height = window.innerHeight;
      }
      resize();
      window.addEventListener('resize', resize);

      function drawStatic() {
        var w = canvas.width, h = canvas.height;
        var imageData = ctx.createImageData(w, h);
        var data = imageData.data;
        for (var i = 0; i < data.length; i += 4) {
          var v = Math.random() > 0.5 ? Math.floor(Math.random() * 80) : 0;
          data[i]     = v + Math.floor(Math.random() * 40);
          data[i + 1] = Math.floor(v * 0.1);
          data[i + 2] = Math.floor(v * 0.1);
          data[i + 3] = 180;
        }
        for (var y = 0; y < h; y++) {
          if (Math.random() < 0.04) {
            var barH  = Math.floor(Math.random() * 6) + 1;
            var shift = Math.floor(Math.random() * 40) - 20;
            for (var by = y; by < Math.min(y + barH, h); by++) {
              for (var x = 0; x < w; x++) {
                var srcX = (x + shift + w) % w;
                var si = (by * w + srcX) * 4;
                var di = (by * w + x) * 4;
                data[di]     = data[si] + 80;
                data[di + 1] = 0;
                data[di + 2] = 0;
                data[di + 3] = 220;
              }
            }
          }
        }
        ctx.putImageData(imageData, 0, 0);
        animId = requestAnimationFrame(drawStatic);
      }

      drawStatic();
    })();
    </script>
    """,
    unsafe_allow_html=True
)

# ─── Persistent overlays & nav hint ──────────────────────────────────────────

st.markdown(
    '<div id="nav-hint"><span class="nh-text">TAP ARROW TO NAVIGATE</span></div>'
    '<div id="vhs-overlay"></div>'
    '<div id="vhs-rgb-r"></div>'
    '<div id="vhs-rgb-b"></div>',
    unsafe_allow_html=True
)

# ─── Audio + interaction JS ───────────────────────────────────────────────────

components.html(
    f"""
    <script>
    (function() {{
      var doc         = window.parent.document;
      var reloadAudio = null;
      var shottyAudio = null;
      var audioReady  = false;
      var audioCtx    = null;
      var bgBuffer    = null;
      var bgSource    = null;
      var bgGain      = null;

      function startGaplessLoop() {{
        if (!audioCtx || !bgBuffer) return;
        if (bgSource) {{ try {{ bgSource.stop(); }} catch(e) {{}} }}
        bgSource          = audioCtx.createBufferSource();
        bgSource.buffer   = bgBuffer;
        bgSource.loop     = true;
        bgGain            = audioCtx.createGain();
        bgGain.gain.value = 0.35;
        bgSource.connect(bgGain);
        bgGain.connect(audioCtx.destination);
        bgSource.start(0);
      }}

      function initAudio() {{
        if (audioReady) return;
        audioReady  = true;
        reloadAudio = new Audio("data:audio/wav;base64,{reload_snd}");
        shottyAudio = new Audio("data:audio/wav;base64,{shotty_snd}");
        reloadAudio.volume = 0.64;
        shottyAudio.volume = 0.64;
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        var b64  = "{web_beat}";
        var bin  = atob(b64);
        var arr  = new Uint8Array(bin.length);
        for (var i = 0; i < bin.length; i++) {{ arr[i] = bin.charCodeAt(i); }}
        audioCtx.decodeAudioData(arr.buffer,
          function(decoded) {{ bgBuffer = decoded; startGaplessLoop(); }},
          function(e)        {{ console.warn("BG audio decode failed:", e); }}
        );
      }}

      function playReload() {{ if (!reloadAudio) return; reloadAudio.currentTime = 0; reloadAudio.play(); }}
      function playShotty() {{ if (!shottyAudio) return; shottyAudio.currentTime = 0; shottyAudio.play(); }}

      function triggerVHS() {{
        var app     = doc.querySelector('.stApp');
        var overlay = doc.getElementById('vhs-overlay');
        var rgbR    = doc.getElementById('vhs-rgb-r');
        var rgbB    = doc.getElementById('vhs-rgb-b');
        [app, overlay, rgbR, rgbB].forEach(function(el) {{
          if (!el) return;
          el.classList.remove('vhs-glitch-active', 'active');
          void el.offsetWidth;
          el.classList.add(el === app ? 'vhs-glitch-active' : 'active');
          setTimeout(function() {{ el.classList.remove('vhs-glitch-active', 'active'); }}, 500);
        }});
      }}

      function clickCollapseArrow() {{
        var selectors = [
          '[data-testid="stSidebarCollapseButton"] button',
          '[data-testid="stSidebarNavCollapseButton"]',
          'button[aria-label="Collapse sidebar"]',
          'button[aria-label="collapse sidebar"]',
          'button[aria-label="Close sidebar"]'
        ];
        for (var i = 0; i < selectors.length; i++) {{
          var btn = doc.querySelector(selectors[i]);
          if (btn) {{ btn.click(); return; }}
        }}
      }}

      function attachHoverSounds() {{
        doc.querySelectorAll('a,button,[role="radio"],[role="button"],label').forEach(function(el) {{
          if (!el.dataset.soundAttached) {{
            el.addEventListener('mouseenter', playReload);
            el.dataset.soundAttached = 'true';
          }}
        }});
      }}

      function attachSidebarCollapse() {{
        doc.querySelectorAll('[data-testid="stSidebar"] label').forEach(function(el) {{
          if (!el.dataset.collapseAttached) {{
            el.addEventListener('mousedown', function() {{
              clickCollapseArrow();
            }});
            el.dataset.collapseAttached = 'true';
          }}
        }});
      }}

      // ── Dismiss VHS intro from parent document ──
      function dismissIntro() {{
        var intro = doc.getElementById('vhs-intro');
        if (!intro || intro._dismissed) return;
        intro._dismissed = true;
        intro.style.transition = 'opacity 1s ease';
        intro.style.opacity = '0';
        intro.style.pointerEvents = 'none';
        setTimeout(function() {{ intro.style.display = 'none'; }}, 1000);
      }}
      setTimeout(dismissIntro, 9000);

      doc.addEventListener('click', function() {{
        initAudio();
        playShotty();
        triggerVHS();
      }}, {{ passive: true }});

      attachHoverSounds();
      attachSidebarCollapse();
      setInterval(function() {{
        attachHoverSounds();
        attachSidebarCollapse();
      }}, 1500);
    }})();
    </script>
    """,
    height=0
)

# ─── Logo ─────────────────────────────────────────────────────────────────────

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(
        f'<img src="data:image/png;base64,{logo}" width="500" '
        f'style="display:block;margin:auto;" loading="lazy">',
        unsafe_allow_html=True
    )

# ─── Sidebar ──────────────────────────────────────────────────────────────────

if "menu" not in st.session_state:
    st.session_state.menu = "The Ritual (Home)"
if "prev_menu" not in st.session_state:
    st.session_state.prev_menu = "The Ritual (Home)"

with st.sidebar:
    st.header("THE VOID")
    menu = st.radio("", [
        "The Ritual (Home)",
        "The Grimoires (Discography)",
        "The Cult (Members)",
        "The Catacombs (Photos)"
    ], key="menu")

if st.session_state.menu != st.session_state.prev_menu:
    st.session_state.prev_menu = st.session_state.menu
    st.markdown(
        """<script>
        (function() {
          var tries = 0;
          function tryCollapse() {
            var btns = [
              '[data-testid="stSidebarCollapseButton"] button',
              '[data-testid="stSidebarNavCollapseButton"]',
              'button[aria-label="Collapse sidebar"]',
              'button[aria-label="collapse sidebar"]',
              'button[aria-label="Close sidebar"]'
            ];
            for (var i = 0; i < btns.length; i++) {
              var b = document.querySelector(btns[i]);
              if (b) { b.click(); return; }
            }
            if (tries++ < 20) setTimeout(tryCollapse, 50);
          }
          tryCollapse();
        })();
        </script>""",
        unsafe_allow_html=True
    )

menu = st.session_state.menu

# ─── Pages ────────────────────────────────────────────────────────────────────

if menu == "The Ritual (Home)":
    st.markdown(
        f'<div style="text-align:center;"><span class="section-header">'
        f'{pistol_l} WHO ARE WE {pistol_r}</span></div>',
        unsafe_allow_html=True
    )
    st.markdown(skull_divider, unsafe_allow_html=True)
    st.markdown(
        "<div style=\"text-align:center;font-family:'BaronessKuffner',cursive;font-size:28px;\">"
        "Forged in the depths of the underground, Hellbound Disciplez is a formidable trio consisting of "
        "<b>Lord-K-Haos</b>, <b>Crazy8 The Snap Case</b>, and <b>Osomane</b>. Independent and unbothered, "
        "these three sonic provocateurs blaze their own trail. With a sound that's equal parts gritty phonk "
        "and horrorcore, they paint vivid portraits of America's dark underbelly - exploring themes of the "
        "occult, street life, and true crime. Fueled by the collaborative production of Osomane and Crazy8 "
        "The Snap Case, and the raw lyricism of the whole crew, their music is a haunting reflection of the "
        "shadows that lurk just beyond the edge of society. Get ready to descend into the abyss with "
        "Hellbound Disciplez."
        "</div><br><br>",
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="text-align:center;"><span class="announce-text">ANNOUNCEMENTS</span></div>',
        unsafe_allow_html=True
    )
    st.markdown(skull_divider, unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align:center;"><span class="glitch-tape-text">Glitch Tape Vol. 2 — Coming Soon</span></div>',
        unsafe_allow_html=True
    )

elif menu == "The Grimoires (Discography)":
    st.markdown('<div style="text-align:center;"><span class="section-header">THE GRIMOIRES</span></div>', unsafe_allow_html=True)
    st.markdown(skull_divider, unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;"><span class="section-header">Albums / Mixtapes / EPs</span></div>', unsafe_allow_html=True)
    st.markdown(skull_divider, unsafe_allow_html=True)
    st.markdown(
        "<div style=\"text-align:center;font-family:'BaronessKuffner',cursive;font-size:28px;\">"
        "<a href='https://open.spotify.com/album/6ZOUHhIAnS532EdK1ZaLtv' target='_blank'>Tales From The Swamp</a> (2025) — 8 tracks<br>"
        "<a href='https://open.spotify.com/album/43O3pIiiwtOhcd9VANWjga' target='_blank'>Hellbound Disciplez (Self Titled)</a> (2023) — 15 tracks<br>"
        "<a href='https://open.spotify.com/album/2smEfqlW4Z16AUD5md7UxZ' target='_blank'>21 Grams Lighter</a> (2022) — 10 tracks<br>"
        "<a href='https://open.spotify.com/album/0LW0Gp5neAyHtihn5pxteR' target='_blank'>The Godless Mixtape</a> (2022) — 11 tracks<br>"
        "<a href='https://open.spotify.com/album/2jEHxL0P2uHT6SPokLnayC' target='_blank'>Glitch Tape Vol.1</a> (2023) — 7 tracks<br>"
        "<a href='https://open.spotify.com/album/1AoyhHGiy4PE6b9HIdfWRu' target='_blank'>Pumpkin Patch Massacre</a> (2023)"
        "</div>",
        unsafe_allow_html=True
    )
    st.markdown('<div style="text-align:center;margin-top:25px;"><span class="section-header">Singles</span></div>', unsafe_allow_html=True)
    st.markdown(skull_divider, unsafe_allow_html=True)
    st.markdown(
        "<div style=\"text-align:center;font-family:'BaronessKuffner',cursive;font-size:28px;\">"
        "<a href='https://open.spotify.com/album/03BObGWktQNHCLhoimV2lK' target='_blank'>COUNTERFEIT</a> (2025)<br>"
        "<a href='https://open.spotify.com/album/4EU2f7tAo6DWhERyavT37j' target='_blank'>Crowbar</a> (2024)<br>"
        "<a href='https://open.spotify.com/album/40pDtzpR5i9jpvhjqNnidt' target='_blank'>My House</a> (2024)<br>"
        "<a href='https://open.spotify.com/album/1Cnug15A07CIImqFiprqVq' target='_blank'>Evil</a> (2024)<br>"
        "<a href='https://open.spotify.com/album/6jrlncx29wFsRc1RzAmSJ1' target='_blank'>Smoke</a> (2024)<br>"
        "<a href='https://open.spotify.com/album/5dFrLqTiyxaH6LcuIQg6z0' target='_blank'>Play Wit Brainz</a> (2024)<br>"
        "<a href='https://open.spotify.com/album/05IpSqxPS21KemQVRH0kWW' target='_blank'>RAGE</a> (2024)<br>"
        "<a href='https://open.spotify.com/album/1AlunGB3eJm2YP38SP3KVj' target='_blank'>Get Back</a> (2024)<br>"
        "<a href='https://open.spotify.com/album/1ln4Uspsd3fzW0XxfJzNkV' target='_blank'>Out The Gate</a> (2024)<br>"
        "<a href='https://open.spotify.com/album/6LefUIwERGJCmAk26R463J' target='_blank'>3-D</a> (2024)<br>"
        "<a href='https://open.spotify.com/album/0RHUVaWHZGSaUJEoKg864j' target='_blank'>HorrorCrunk In My Trunk</a> (2024)<br>"
        "<a href='https://open.spotify.com/album/617AGfI79Jb0bhiCSIQzqf' target='_blank'>Welcome To The South</a> (2024)<br>"
        "<a href='https://open.spotify.com/album/3S8xkqGMr0Km0NlQFM7v2g' target='_blank'>REIGN TERROR</a> (2023)<br>"
        "<a href='https://open.spotify.com/album/54ly6Sfv6krcsPOO1r2wMQ' target='_blank'>Bloodsuckers</a> (2023)<br>"
        "<a href='https://open.spotify.com/album/3ZmMnJjsN0ISEOg62KfgUO' target='_blank'>2 Pillar's</a> (2023)<br>"
        "<a href='https://open.spotify.com/album/43zuHUEggiF3ncNrcPj7s3' target='_blank'>Steppers</a> (2023)"
        "</div>",
        unsafe_allow_html=True
    )
    st.markdown('<div style="text-align:center;margin-top:25px;"><span class="section-header">Follow / Stream Hellbound Disciplez</span></div>', unsafe_allow_html=True)
    st.markdown(skull_divider, unsafe_allow_html=True)
    st.markdown(
        "<div style=\"text-align:center;font-family:'BaronessKuffner',cursive;font-size:28px;\">"
        "<a href='https://open.spotify.com/artist/5hRvzAL7q1as1y5FqKEaGZ' target='_blank'>Spotify</a><br>"
        "<a href='https://music.apple.com/us/artist/hellbound-disciplez/1641539761' target='_blank'>Apple Music</a><br>"
        "<a href='https://music.amazon.com/artists/B0BBSJ6W1Z/hellbound-disciplez' target='_blank'>Amazon Music</a><br>"
        "<a href='https://www.facebook.com/profile.php?id=100091797215709' target='_blank'>Facebook</a><br>"
        "<a href='https://www.instagram.com/hellbound_disciplez?igsh=dmV1bjc5NmZoazh0' target='_blank'>Instagram</a>"
        "</div>",
        unsafe_allow_html=True
    )

elif menu == "The Cult (Members)":
    st.markdown('<div style="text-align:center;"><span class="section-header">THE CULT</span></div>', unsafe_allow_html=True)
    st.markdown(skull_divider, unsafe_allow_html=True)
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("pic5.jpg", width=150)
    with col2:
        st.subheader("🔥 Lord-K-Haos")
        st.markdown(
            '<p style="font-family:BaronessKuffner,cursive;font-size:28px;">'
            'MC | Lyricist | Co-Founder — The chaos incarnate. Lord-K-Haos brings the darkness '
            'with razor sharp lyricism and an iron grip on the mic.</p>',
            unsafe_allow_html=True
        )
    st.markdown(skull_divider, unsafe_allow_html=True)
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("img12.jpg", width=150)
    with col2:
        st.subheader("🔥 Crazy8 The Snap Case")
        st.markdown(
            '<p style="font-family:BaronessKuffner,cursive;font-size:28px;">'
            'MC | Lyricist | Producer | Co-Founder — Raw, unfiltered, and unpredictable. '
            'Crazy8 The Snap Case delivers horrorcore at its most visceral while helping craft '
            'the sonic backbone of the group alongside Osomane.</p>',
            unsafe_allow_html=True
        )
    st.markdown(skull_divider, unsafe_allow_html=True)
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("img11.jpg", width=150)
    with col2:
        st.subheader("🔥 Osomane")
        st.markdown(
            '<p style="font-family:BaronessKuffner,cursive;font-size:28px;">'
            'Producer | Member — The architect of the sound. Osomane works hand in hand with '
            'Crazy8 to build the dark, gritty beats that bring the Hellbound Disciplez vision to life.</p>',
            unsafe_allow_html=True
        )

elif menu == "The Catacombs (Photos)":
    st.markdown('<div style="text-align:center;"><span class="section-header">THE CATACOMBS</span></div>', unsafe_allow_html=True)
    st.markdown(skull_divider, unsafe_allow_html=True)
    photos = get_shuffled_photos()
    cols = st.columns(2)
    for i, photo_path in enumerate(photos):
        with cols[i % 2]:
            st.image(photo_path, use_container_width=True)
