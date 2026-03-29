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
def get_font_base64(filename):
    with open(filename, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

@st.cache_data(show_spinner=False)
def get_shuffled_photos():
    photos = [
        "pic1.png","pic2.png","pic3.png","pic4.png","pic5.jpg","pic6.png","pic7.jpg","pic8.jpeg",
        "pic9.jpeg","pic10.png","pic11.jpeg","pic12.jpeg","pic13.jpeg","pic14.jpeg","pic15.jpeg",
        "pic16.jpeg","pic17.jpeg","pic18.jpeg","pic19.png","pic20.png","pic21.png","pic22.png","pic23.jpg",
        "pic24.png","pic25.jpg","pic26.jpg","pic27.jpg","pic28.jpg","pic29.jpg","pic30.jpg",
        "pic31.jpg","pic32.jpg","pic33.jpg","pic34.jpg","pic35.jpg","pic36.jpg","pic37.jpg",
        "pic39.jpg","pic40.jpg","pic41.jpg",
        "img1.jpg","img2.jpg","img3.jpg","img4.jpg","img5.jpg","img6.jpg",
        "img7.jpg","img8.jpg","img9 - Copy.jpg","img10.jpg","img11.jpg","img12.jpg",
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
web_beat      = get_audio_base64("WEB_BEAT_001.mp3")
font_baroness = get_font_base64("BaronessKuffner.ttf")
font_glitch   = get_font_base64("DoctorGlitch.otf")

# ─── Page Config ──────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="HELLBOUND DISCIPLEZ",
    page_icon="🤘",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "menu" not in st.session_state:
    st.session_state.menu = "The Ritual (Home)"

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

iframe {{
  border:none !important;
  outline:none !important;
  box-shadow:none !important;
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
  position:fixed;top:70px;left:8px;z-index:9999;
  display:flex;align-items:center;gap:6px;
  background:rgba(0,0,0,0.75);border:1px solid #ff2200;
  border-radius:4px;padding:5px 10px;
  animation:navPulse 2s ease-in-out infinite;
  box-shadow:0 0 8px rgba(255,34,0,0.4);pointer-events:none;
}}
#nav-hint .nh-text {{
  font-family:'DoctorGlitch',cursive !important;
  font-size:11px;color:#ff2200;letter-spacing:1px;
  white-space:normal;word-break:break-word;
  width:70px;text-align:center;
  -webkit-text-stroke:0.3px white;line-height:1.4;
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

[data-testid="stMain"] p,[data-testid="stMain"] li,[data-testid="stMain"] a,
[data-testid="stSidebar"] p,[data-testid="stSidebar"] li,[data-testid="stSidebar"] label {{
  font-family:'BaronessKuffner',cursive !important;
  font-size:28px !important;color:#ff2200 !important;
}}

[data-testid="stMain"] h1,[data-testid="stMain"] h2,[data-testid="stMain"] h3,
[data-testid="stMain"] h4,[data-testid="stMain"] h5,[data-testid="stMain"] h6,
[data-testid="stSidebar"] h1,[data-testid="stSidebar"] h2,[data-testid="stSidebar"] h3 {{
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
  -webkit-text-stroke:0.5px white;display:block;text-align:center;margin:10px 0;
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
  -webkit-text-stroke:0.5px white;display:block;text-align:center;margin:10px 0;
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
  background:repeating-linear-gradient(0deg,rgba(255,0,0,0.08) 0px,rgba(255,0,0,0.08) 1px,transparent 1px,transparent 3px);
}}
#vhs-overlay.active {{ display:block;animation:scanline-flash 0.5s steps(1,end) forwards; }}
#vhs-rgb-r,#vhs-rgb-b {{
  position:fixed;top:0;left:0;width:100vw;height:100vh;
  pointer-events:none;z-index:999997;display:none;
}}
#vhs-rgb-r.active,#vhs-rgb-b.active {{ display:block;animation:scanline-flash 0.5s steps(1,end) forwards; }}

/* ── Shattered Glass Crack Overlay ── */
@keyframes crack-flash {{
  0%   {{ opacity:0; }}
  3%   {{ opacity:1; }}
  60%  {{ opacity:1; }}
  100% {{ opacity:0; }}
}}
#crack-overlay {{
  position:fixed;top:0;left:0;width:100vw;height:100vh;
  pointer-events:none;z-index:999999;display:none;
}}
#crack-overlay.active {{
  display:block;
  animation:crack-flash 0.75s ease-out forwards;
}}
#crack-overlay canvas {{
  position:absolute;top:0;left:0;width:100%;height:100%;
}}

/* ── VHS Intro ── */
#vhs-intro {{
  position:fixed;top:0;left:0;width:100vw;height:100vh;
  background:#000;z-index:2147483647;
  display:flex;align-items:center;justify-content:center;
  flex-direction:column;transition:opacity 1s ease;
}}
#vhs-intro.fadeout {{ opacity:0;pointer-events:none; }}
#vhs-intro canvas {{ position:absolute;top:0;left:0;width:100%;height:100%; }}
#vhs-intro-scanlines {{
  position:absolute;top:0;left:0;width:100%;height:100%;
  background:repeating-linear-gradient(0deg,rgba(0,0,0,0.4) 0px,rgba(0,0,0,0.4) 1px,transparent 1px,transparent 4px);
  z-index:1;pointer-events:none;
}}
#vhs-intro-text {{
  position:relative;z-index:2;font-family:'DoctorGlitch',cursive;
  font-size:48px;color:#ff2200;-webkit-text-stroke:1px white;
  text-align:center;letter-spacing:6px;
  animation:introFlicker 0.15s steps(1,end) infinite;
  text-shadow:0 0 20px #ff2200,0 0 40px #ff0000;
}}
#vhs-intro-sub {{
  position:relative;z-index:2;font-family:'DoctorGlitch',cursive;
  font-size:18px;color:#ff2200;letter-spacing:4px;margin-top:16px;
  opacity:0.7;animation:introFlicker 0.3s steps(1,end) infinite;
}}
@keyframes introFlicker {{
  0%,89% {{ opacity:1; }} 90% {{ opacity:0.2; }}
  91% {{ opacity:1; }} 94% {{ opacity:0.4; }} 95% {{ opacity:1; }}
}}
@keyframes btnPulse {{
  0%,100% {{ box-shadow:0 0 10px #ff2200,0 0 20px #ff2200,0 0 40px #ff0000;letter-spacing:6px; }}
  50%      {{ box-shadow:0 0 30px #ff5500,0 0 60px #ff2200,0 0 100px #ff0000;letter-spacing:10px; }}
}}
@keyframes btnFlicker {{
  0%,90%,100% {{ opacity:1; }} 92% {{ opacity:0.3; }}
  95% {{ opacity:0.8; }} 97% {{ opacity:0.2; }}
}}
#vhs-load-btn, #vhs-enter-btn {{
  position:relative;z-index:3;margin-top:50px;
  font-family:'DoctorGlitch',cursive;font-size:26px;color:#ff2200;
  background:rgba(0,0,0,0.85);border:2px solid #ff2200;
  padding:18px 60px;letter-spacing:6px;cursor:pointer;
  -webkit-text-stroke:0.5px rgba(255,255,255,0.6);
  text-shadow:0 0 10px #ff2200,0 0 20px #ff0000;
  animation:btnPulse 1.8s ease-in-out infinite,btnFlicker 4s steps(1,end) infinite;
  clip-path:polygon(8px 0%,100% 0%,calc(100% - 8px) 100%,0% 100%);outline:none;
}}
#vhs-load-btn {{ display:none; }}
#vhs-enter-btn {{ display:none; }}
#vhs-load-btn:hover, #vhs-enter-btn:hover {{
  background:rgba(255,34,0,0.15);color:#fff;
  text-shadow:0 0 20px #fff,0 0 40px #ff2200;transition:all 0.2s ease;
}}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# ─── VHS Intro HTML ───────────────────────────────────────────────────────────

st.markdown(
    '<div id="vhs-intro">'
    '<canvas id="vhs-static-canvas"></canvas>'
    '<div id="vhs-intro-scanlines"></div>'
    '<div id="vhs-intro-text" style="display:none;">HELLBOUND DISCIPLEZ</div>'
    '<div id="vhs-intro-sub" style="display:none;">&#9654; LOADING...</div>'
    '<button id="vhs-load-btn">&#9760; CLICK TO LOAD &#9760;</button>'
    '<button id="vhs-enter-btn">&#9760; ENTER THE VOID &#9760;</button>'
    '</div>',
    unsafe_allow_html=True
)

# ─── Nav hint + overlays ──────────────────────────────────────────────────────

st.markdown(
    '<div id="nav-hint"><span class="nh-text">TAP THE ARROW TO NAVIGATE</span></div>'
    '<div id="vhs-overlay"></div>'
    '<div id="vhs-rgb-r"></div>'
    '<div id="vhs-rgb-b"></div>'
    '<div id="crack-overlay"><canvas id="crack-canvas"></canvas></div>',
    unsafe_allow_html=True
)

# ─── All JS ───────────────────────────────────────────────────────────────────

components.html(
    f"""
    <script>
    (function() {{
      var doc = window.parent.document;
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
          function(e) {{ console.warn("BG audio decode failed:", e); }}
        );
      }}

      function playReload() {{ if (!reloadAudio) return; reloadAudio.currentTime = 0; reloadAudio.play(); }}
      function playShotty() {{ if (!shottyAudio) return; shottyAudio.currentTime = 0; shottyAudio.play(); }}

      // ── Concentrated spiderweb shatter at click point ──
      function drawCracks(canvas, cx, cy) {{
        var W = window.parent.innerWidth;
        var H = window.parent.innerHeight;
        canvas.width  = W;
        canvas.height = H;
        var ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, W, H);

        // Blast radius = ~1/3 of screen — shotgun spread
        var RADIUS = Math.min(W, H) * 0.34;

        // Clip everything to the blast circle using radial gradient mask
        // We draw into a temp canvas then composite with fade at edges
        var tmp = document.createElement('canvas');
        tmp.width = W; tmp.height = H;
        var tc = tmp.getContext('2d');

        // ── 1. Voronoi seeds packed inside the blast radius ──
        var seeds = [];

        // Epicenter — ultra tight micro shards
        for (var i = 0; i < 18; i++) {{
          var a = Math.random() * Math.PI * 2;
          var d = Math.random() * RADIUS * 0.1;
          seeds.push({{ x: cx + Math.cos(a)*d, y: cy + Math.sin(a)*d }});
        }}
        // Inner zone — dense jagged shards
        for (var i = 0; i < 28; i++) {{
          var a = Math.random() * Math.PI * 2;
          var d = RADIUS * 0.08 + Math.random() * RADIUS * 0.38;
          seeds.push({{ x: cx + Math.cos(a)*d, y: cy + Math.sin(a)*d }});
        }}
        // Outer zone — larger blown-out shards at rim
        for (var i = 0; i < 18; i++) {{
          var a = Math.random() * Math.PI * 2;
          var d = RADIUS * 0.42 + Math.random() * RADIUS * 0.58;
          seeds.push({{ x: cx + Math.cos(a)*d, y: cy + Math.sin(a)*d }});
        }}

        // ── 2. Clip half-plane helper ──
        function clipPoly(poly, ax, ay, bx, by) {{
          var out = [], n = poly.length;
          for (var i = 0; i < n; i++) {{
            var c = poly[i], nx = poly[(i+1)%n];
            var d1 = (bx-ax)*(c.y-ay)  - (by-ay)*(c.x-ax);
            var d2 = (bx-ax)*(nx.y-ay) - (by-ay)*(nx.x-ax);
            if (d1 >= 0) out.push(c);
            if ((d1>0&&d2<0)||(d1<0&&d2>0)) {{
              var t = d1/(d1-d2);
              out.push({{ x: c.x+t*(nx.x-c.x), y: c.y+t*(nx.y-c.y) }});
            }}
          }}
          return out;
        }}

        // ── 3. Build Voronoi cells, clipped to blast circle boundary ──
        var PAD = RADIUS * 1.1;
        for (var si = 0; si < seeds.length; si++) {{
          var cell = [
            {{x: cx-PAD, y: cy-PAD}},
            {{x: cx+PAD, y: cy-PAD}},
            {{x: cx+PAD, y: cy+PAD}},
            {{x: cx-PAD, y: cy+PAD}}
          ];
          var sx = seeds[si].x, sy = seeds[si].y;
          for (var sj = 0; sj < seeds.length; sj++) {{
            if (si===sj) continue;
            var ox = seeds[sj].x, oy = seeds[sj].y;
            var mx = (sx+ox)/2, my = (sy+oy)/2;
            cell = clipPoly(cell, mx, my, mx+(oy-sy), my-(ox-sx));
            if (cell.length===0) break;
          }}
          if (cell.length < 3) continue;

          // Distance from center for fade
          var dist = Math.hypot(sx-cx, sy-cy);
          var t    = Math.min(dist/RADIUS, 1); // 0=center 1=edge

          // Shard fill — bright glassy blue-white, fades with distance
          var fillA   = 0.55 - t * 0.5;
          var strokeA = 1.0  - t * 0.6;
          if (fillA <= 0) continue;

          var ccx = cell.reduce(function(s,p){{return s+p.x;}},0)/cell.length;
          var ccy = cell.reduce(function(s,p){{return s+p.y;}},0)/cell.length;

          tc.beginPath();
          tc.moveTo(cell[0].x, cell[0].y);
          for (var pi=1; pi<cell.length; pi++) tc.lineTo(cell[pi].x, cell[pi].y);
          tc.closePath();

          // Glass gradient per shard — more opaque near center
          try {{
            var g = tc.createRadialGradient(ccx, ccy, 0, ccx, ccy, 55);
            g.addColorStop(0, 'rgba(235,245,255,'+(fillA+0.15)+')');
            g.addColorStop(1, 'rgba(160,195,230,'+fillA+')');
            tc.fillStyle = g;
          }} catch(e) {{
            tc.fillStyle = 'rgba(200,220,255,'+fillA+')';
          }}
          tc.fill();

          // Crack outline — bright white, glowing, thicker near center
          tc.strokeStyle = 'rgba(255,255,255,'+strokeA+')';
          tc.lineWidth   = 1.0 + (1-t) * 3.5;
          tc.shadowColor = 'rgba(255,255,255,0.9)';
          tc.shadowBlur  = 5 + (1-t) * 18;
          tc.stroke();
          tc.shadowBlur  = 0;
        }}

        // ── 4. Radial spider-web crack lines FROM center ──
        var numSpokes = 16 + Math.floor(Math.random()*8);
        for (var s=0; s<numSpokes; s++) {{
          var baseAngle = (s/numSpokes)*Math.PI*2 + (Math.random()-0.5)*0.3;
          var spokeDist = RADIUS * (0.7 + Math.random()*0.3);
          tc.beginPath();
          tc.moveTo(cx, cy);
          var px=cx, py=cy, angle=baseAngle;
          var steps = 6 + Math.floor(Math.random()*5);
          for (var k=0; k<steps; k++) {{
            angle += (Math.random()-0.5)*0.4;
            var segLen = spokeDist/steps;
            px += Math.cos(angle)*segLen;
            py += Math.sin(angle)*segLen;
            tc.lineTo(px,py);
            // aggressive branching
            if (Math.random()<0.65) {{
              var ba=angle+(Math.random()-0.5)*1.4;
              var bx=px,by=py;
              tc.moveTo(bx,by);
              var blen=(spokeDist/steps)*(0.4+Math.random()*0.6);
              bx+=Math.cos(ba)*blen; by+=Math.sin(ba)*blen;
              tc.lineTo(bx,by);
              // sub-branch
              if (Math.random()<0.4) {{
                var ba2=ba+(Math.random()-0.5)*1.0;
                var blen2=blen*0.5;
                tc.moveTo(bx,by);
                tc.lineTo(bx+Math.cos(ba2)*blen2, by+Math.sin(ba2)*blen2);
              }}
              tc.moveTo(px,py);
            }}
          }}
          var distFade = Math.min(spokeDist/RADIUS,1);
          tc.strokeStyle='rgba(255,255,255,'+(1.0-distFade*0.4)+')';
          tc.lineWidth  = 2.0 - distFade*1.2;
          tc.shadowColor='rgba(255,255,255,1)';
          tc.shadowBlur =12;
          tc.stroke();
          tc.shadowBlur=0;
        }}

        // ── 5. Concentric ring fractures ──
        var rings = [0.25, 0.5, 0.75, 1.0];
        rings.forEach(function(rf) {{
          var rr = RADIUS * rf;
          var segs = 8 + Math.floor(Math.random()*6);
          for (var s=0; s<segs; s++) {{
            var a1 = (s/segs)*Math.PI*2 + (Math.random()-0.5)*0.2;
            var a2 = ((s+0.6+Math.random()*0.3)/segs)*Math.PI*2;
            tc.beginPath();
            tc.arc(cx, cy, rr+(Math.random()-0.5)*12, a1, a2);
            tc.strokeStyle='rgba(255,255,255,'+(0.5*(1-rf)+0.15)+')';
            tc.lineWidth=0.6;
            tc.stroke();
          }}
        }});

        // ── 6. Composite with IRREGULAR jagged boundary — no perfect circle ──
        ctx.drawImage(tmp, 0, 0);

        // Build a spiky uneven polygon boundary for the blast zone
        ctx.save();
        ctx.globalCompositeOperation = 'destination-in';
        var boundaryPts = 38;
        ctx.beginPath();
        for (var bi = 0; bi < boundaryPts; bi++) {{
          var ba = (bi / boundaryPts) * Math.PI * 2;
          // Jagged radius — spikes and dips, uneven like real broken glass
          var spike = 0.55 + Math.random() * 0.55;
          // Every few points punch outward hard for a crack-tip spike
          if (Math.random() < 0.25) spike = 1.1 + Math.random() * 0.25;
          // Occasional deep inward notch
          if (Math.random() < 0.15) spike = 0.38 + Math.random() * 0.2;
          var bx = cx + Math.cos(ba) * RADIUS * spike;
          var by = cy + Math.sin(ba) * RADIUS * spike;
          if (bi === 0) ctx.moveTo(bx, by);
          else ctx.lineTo(bx, by);
        }}
        ctx.closePath();
        // Gradient fill inside the jagged shape — fades at edges
        var mask = ctx.createRadialGradient(cx, cy, RADIUS*0.3, cx, cy, RADIUS*1.1);
        mask.addColorStop(0,    'rgba(0,0,0,1)');
        mask.addColorStop(0.72, 'rgba(0,0,0,1)');
        mask.addColorStop(1,    'rgba(0,0,0,0)');
        ctx.fillStyle = mask;
        ctx.fill();
        ctx.restore();

        // ── 7. Violent shotgun starburst at click point ──
        ctx.save();
        ctx.translate(cx, cy);
        var burst = ctx.createRadialGradient(0,0,0, 0,0,60);
        burst.addColorStop(0,   'rgba(255,255,255,1)');
        burst.addColorStop(0.15,'rgba(255,255,255,0.95)');
        burst.addColorStop(0.3, 'rgba(255,160,0,0.9)');
        burst.addColorStop(0.6, 'rgba(255,30,0,0.55)');
        burst.addColorStop(1,   'rgba(255,0,0,0)');
        ctx.fillStyle = burst;
        ctx.beginPath();
        ctx.arc(0,0,60,0,Math.PI*2);
        ctx.fill();
        ctx.restore();
      }}

      function triggerCrack(clickX, clickY) {{
        var overlay = doc.getElementById('crack-overlay');
        var canvas  = doc.getElementById('crack-canvas');
        if (!overlay || !canvas) return;
        drawCracks(canvas, clickX, clickY);
        overlay.classList.remove('active');
        void overlay.offsetWidth;
        overlay.classList.add('active');
        setTimeout(function() {{ overlay.classList.remove('active'); }}, 760);
      }}

      function triggerVHS(clickX, clickY) {{
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
        triggerCrack(clickX, clickY);
      }}

      function attachHoverSounds() {{
        doc.querySelectorAll('a,button,[role="radio"],[role="button"],label').forEach(function(el) {{
          if (!el.dataset.soundAttached) {{
            el.addEventListener('mouseenter', playReload);
            el.dataset.soundAttached = 'true';
          }}
        }});
      }}

      // ── VHS Intro ──
      (function() {{
        var canvas = doc.getElementById('vhs-static-canvas');
        if (!canvas) return;
        var ctx    = canvas.getContext('2d');
        var animId = null;
        var frame  = 0;
        var lo     = document.createElement('canvas');
        var loctx  = lo.getContext('2d');
        var SCALE  = 12;
        var noiseCtx, noiseSource, noiseGain;

        function resize() {{
          canvas.width  = window.parent.innerWidth;
          canvas.height = window.parent.innerHeight;
          lo.width      = Math.ceil(canvas.width  / SCALE);
          lo.height     = Math.ceil(canvas.height / SCALE);
        }}
        resize();
        window.parent.addEventListener('resize', resize);

        function drawStatic() {{
          frame++;
          if (frame % 6 !== 0) {{
            animId = window.parent.requestAnimationFrame(drawStatic);
            return;
          }}
          var w = lo.width, h = lo.height;
          var imageData = loctx.createImageData(w, h);
          var data = imageData.data;
          for (var i = 0; i < data.length; i += 4) {{
            var v = Math.random() > 0.5 ? (Math.random() * 180)|0 : 0;
            data[i]     = v;
            data[i + 1] = (v * 0.05)|0;
            data[i + 2] = (v * 0.05)|0;
            data[i + 3] = 210;
          }}
          if (Math.random() < 0.3) {{
            var gy = (Math.random() * h)|0;
            var gi = gy * w * 4;
            for (var gx = 0; gx < w * 4; gx += 4) {{
              data[gi + gx]     = 220;
              data[gi + gx + 1] = 0;
              data[gi + gx + 2] = 0;
              data[gi + gx + 3] = 255;
            }}
          }}
          loctx.putImageData(imageData, 0, 0);
          ctx.imageSmoothingEnabled = false;
          ctx.drawImage(lo, 0, 0, canvas.width, canvas.height);
          animId = window.parent.requestAnimationFrame(drawStatic);
        }}

        function startNoise() {{
          noiseCtx = new (window.AudioContext || window.webkitAudioContext)();
          var bufSize   = noiseCtx.sampleRate * 2;
          var noiseBuf  = noiseCtx.createBuffer(1, bufSize, noiseCtx.sampleRate);
          var noiseData = noiseBuf.getChannelData(0);
          for (var n = 0; n < bufSize; n++) {{ noiseData[n] = Math.random() * 2 - 1; }}
          noiseSource          = noiseCtx.createBufferSource();
          noiseSource.buffer   = noiseBuf;
          noiseSource.loop     = true;
          noiseGain            = noiseCtx.createGain();
          noiseGain.gain.value = 0.2;
          noiseSource.connect(noiseGain);
          noiseGain.connect(noiseCtx.destination);
          noiseSource.start(0);
        }}

        function stopNoise() {{
          if (!noiseCtx || !noiseGain || !noiseSource) return;
          try {{
            noiseGain.gain.setTargetAtTime(0, noiseCtx.currentTime, 0.5);
            setTimeout(function() {{ try {{ noiseSource.stop(); }} catch(e) {{}} }}, 1500);
          }} catch(e) {{}}
        }}

        function dismissIntro() {{
          var intro = doc.getElementById('vhs-intro');
          if (!intro || intro._dismissed) return;
          intro._dismissed = true;
          window.parent.cancelAnimationFrame(animId);
          intro.style.transition    = 'opacity 1s ease';
          intro.style.opacity       = '0';
          intro.style.pointerEvents = 'none';
          setTimeout(function() {{ intro.style.display = 'none'; }}, 1000);
        }}

        drawStatic();

        var loadBtn = doc.getElementById('vhs-load-btn');
        if (loadBtn) {{
          loadBtn.addEventListener('click', function(e) {{
            e.stopPropagation();
            startNoise();
            setTimeout(function() {{
              loadBtn.style.display = 'none';
              doc.getElementById('vhs-intro-text').style.display = 'block';
              doc.getElementById('vhs-intro-sub').style.display  = 'block';
            }}, 50);

            setTimeout(function() {{
              stopNoise();
              var enterBtn = doc.getElementById('vhs-enter-btn');
              if (enterBtn) {{
                enterBtn.style.display = 'block';
                enterBtn.addEventListener('click', function(e) {{
                  e.stopPropagation();
                  initAudio();
                  dismissIntro();
                  setTimeout(function() {{
                    doc.addEventListener('click', function(e) {{
                      playShotty();
                      triggerVHS(e.clientX, e.clientY);
                    }}, {{ passive: true }});
                    attachHoverSounds();
                    setInterval(attachHoverSounds, 1500);
                  }}, 1000);
                }});
              }}
            }}, 7000);

            setTimeout(dismissIntro, 15000);
          }});
          loadBtn.style.display = 'block';
        }}
      }})();

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

with st.sidebar:
    st.header("THE VOID")
    menu = st.radio("", [
        "The Ritual (Home)",
        "The Grimoires (Discography)",
        "The Cult (Members)",
        "The Catacombs (Photos)"
    ], key="menu")

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
        st.markdown('<div style="font-family:DoctorGlitch,cursive;color:#ff2200;font-size:1.75rem;margin:0.5rem 0;">🔥 Lord-K-Haos</div>', unsafe_allow_html=True)
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
        st.markdown('<div style="font-family:DoctorGlitch,cursive;color:#ff2200;font-size:1.75rem;margin:0.5rem 0;">🔥 <a href="https://crazy8thesnapcase-site.onrender.com" target="_blank" style="color:#ff2200;text-decoration:none;font-family:DoctorGlitch,cursive;font-size:1.75rem;">Crazy8 The Snap Case</a></div>', unsafe_allow_html=True)
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
        st.markdown('<div style="font-family:DoctorGlitch,cursive;color:#ff2200;font-size:1.75rem;margin:0.5rem 0;">🔥 Osomane</div>', unsafe_allow_html=True)
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
