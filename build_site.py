# -*- coding: utf-8 -*-
import math

def star_points(n=14, outer=48, inner=39, cx=50, cy=50):
    pts = []
    for i in range(2 * n):
        r = outer if i % 2 == 0 else inner
        ang = math.pi * i / n - math.pi / 2
        x = cx + r * math.cos(ang)
        y = cy + r * math.sin(ang)
        pts.append(f"{x:.1f},{y:.1f}")
    return " ".join(pts)

STAR = star_points()

# Shell icon path pieces (reused as our "mascot" mark)
SHELL_RAYS = "M50,80 L94.4,68.1 M50,80 L85.2,50.4 M50,80 L69.4,38.3 M50,80 L50,34 M50,80 L30.6,38.3 M50,80 L14.8,50.4 M50,80 L5.6,68.1"
SHELL_FAN = "M5.6,68.1 L14.8,50.4 L30.6,38.3 L50,34 L69.4,38.3 L85.2,50.4 L94.4,68.1"
SHELL_HINGE = "M5.6,68.1 Q50,95 94.4,68.1"

def shell_icon(cls="", extra=""):
    return f'''<svg class="{cls}" {extra} viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="{SHELL_HINGE}" stroke="currentColor" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="{SHELL_FAN}" stroke="currentColor" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="{SHELL_RAYS}" stroke="currentColor" stroke-width="4" stroke-linecap="round"/>
    </svg>'''

def star_svg(cls="", extra=""):
    return f'<svg class="{cls}" {extra} viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><polygon points="{STAR}" fill="currentColor"/></svg>'

def placeholder(label="Foto på vej", ratio="4/3", cls=""):
    return f'''<div class="ph {cls}" style="aspect-ratio:{ratio};">
      {shell_icon("ph-icon")}
      <span class="ph-label">{label}</span>
    </div>'''

def stamp_badge(text="HJEMMELAVET &#9679; AALBORG &#9679; ", cls="about-stamp-ring"):
    r = 42
    d = f"M 50,50 m -{r},0 a {r},{r} 0 1,1 {2*r},0 a {r},{r} 0 1,1 -{2*r},0"
    star_small = star_points(n=10, outer=13, inner=9, cx=50, cy=50)
    return f'''<svg class="{cls}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path id="aboutStampRing" d="{d}" fill="none"/>
      <circle cx="50" cy="50" r="21" fill="#f7efe0" stroke="currentColor" stroke-width="1.4"/>
      <polygon points="{star_small}" fill="currentColor"/>
      <text font-family="Archivo, sans-serif" font-size="8" font-weight="800" letter-spacing="0.14em" fill="currentColor">
        <textPath href="#aboutStampRing" startOffset="0%">{text}</textPath>
      </text>
    </svg>'''

CHECK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M5 13l4 4L19 7" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
PIN = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="M12 21s7-6.1 7-11.5A7 7 0 0 0 5 9.5C5 14.9 12 21 12 21z" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="9.3" r="2.3" stroke="currentColor" stroke-width="2"/></svg>'
CLOCK = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="8.5" stroke="currentColor" stroke-width="2"/><path d="M12 7v5l3.2 2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'
IG = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none"><rect x="2" y="2" width="20" height="20" rx="6" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="2"/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor"/></svg>'
PHONE = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M6.5 3h3l1.5 4.5L9 9.5a11 11 0 0 0 5.5 5.5l2-2 4.5 1.5v3c0 1-1 2-2.2 1.9C11.8 19.2 4.8 12.2 4.6 5.2 4.5 4 5.5 3 6.5 3z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>'
CARD_PAY = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none"><rect x="3" y="5" width="18" height="14" rx="2.5" stroke="currentColor" stroke-width="2"/><path d="M3 9.5h18" stroke="currentColor" stroke-width="2"/></svg>'
STEP_ARROW = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="M5 12h13.5M13 6l6.5 6-6.5 6" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'

# repeating icon strip
strip_colors = ["#c1381f", "#2c5f4f", "#dda43e"]
strip_items = []
for i in range(20):
    c = strip_colors[i % 3]
    strip_items.append(f'<span style="color:{c}">{shell_icon("strip-icon")}</span>')
STRIP = "\n".join(strip_items)

bowls = [
    ("Shrimp Bowl", "Rejer, majs, kartofler", "150", "250", None),
    ("Crawfish Bowl", "Krebs, majs, kartofler", "150", "250", None),
    ("Craw Shrimp Bowl", "Rejer, krebs, majs, kartofler", "150", "250", None),
    ("Mix Bowl", "Rejer, baby blæksprutte, blåmuslinger, majs, kartofler", "170", "280", None),
    ("Blåmuslinger Bowl", "Blåmuslinger i hvidløgsovs, majs", "100", "160", None),
    ("Deluxe Bowl", "Rejer, krebs, baby blæksprutte, blåmuslinger, majs, kartofler, snekrabbeben", "190", "350", None),
    ("Luksus Bowl", "Hummer, snekrabbe, rejer, grønmuslinger, krebs, majs og kartofler", None, "600", "Kun 2 personer"),
]

bowl_cards = []
for name, ing, p1, p2, note in bowls:
    price_html = ""
    if p1:
        price_html += f'<div class="price-pill"><span class="who">1 person</span><span class="amt">{p1} kr</span></div>'
    else:
        price_html += '<div class="price-pill off"><span class="who">1 person</span><span class="amt">&mdash;</span></div>'
    price_html += f'<div class="price-pill"><span class="who">2 personer</span><span class="amt">{p2} kr</span></div>'
    note_html = f'<span class="bowl-note">{note}</span>' if note else ""
    bowl_cards.append(f'''
        <article class="bowl">
          {placeholder("Foto på vej", "4/3")}
          <div class="bowl-body">
            <div class="bowl-name">{name}{note_html}</div>
            <p class="bowl-ing">{ing}</p>
          </div>
          <div class="bowl-prices">{price_html}</div>
        </article>''')
BOWL_CARDS = "\n".join(bowl_cards)


HTML = f"""<!doctype html>
<html lang="da">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Aalborg Seafood Boil</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;0,9..144,700;0,9..144,800;1,9..144,500&family=Archivo:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&family=Caveat:wght@600;700&display=swap" rel="stylesheet">
<style>
  :root{{
    --cream:#f7efe0;
    --cream-2:#fbf6ec;
    --stripe:#efe3cc;
    --ink:#241b12;
    --ink-soft:#4a3c2c;
    --muted:#6f5f49;
    --line: rgba(36,27,18,0.14);
    --red:#c1381f;
    --red-deep:#9a2c17;
    --green:#2c5f4f;
    --green-deep:#204539;
    --gold:#dda43e;
    --gold-deep:#9c6414;
    --radius:16px;
  }}
  *{{box-sizing:border-box;}}
  html{{background:var(--cream); scroll-behavior:smooth; overflow-x:hidden;}}
  body{{overflow-x:hidden;}}
  @media (prefers-reduced-motion: reduce){{
    *, *::before, *::after{{ animation-duration:0.001ms !important; animation-iteration-count:1 !important; transition-duration:0.001ms !important; scroll-behavior:auto !important; }}
  }}
  body{{
    margin:0;
    background:var(--cream);
    color:var(--ink);
    font-family:"Archivo", ui-sans-serif, system-ui, sans-serif;
    -webkit-font-smoothing:antialiased;
    padding-left:max(20px, env(safe-area-inset-left, 0px));
    padding-right:max(20px, env(safe-area-inset-right, 0px));
    overflow-x:hidden;
  }}
  img,svg{{display:block;}}
  a{{color:inherit;}}
  h1,h2,h3{{margin:0; text-wrap:balance;}}
  p{{margin:0;}}
  .wrap{{max-width:1180px; margin:0 auto;}}
  .sr-only{{
    position:absolute; width:1px; height:1px; padding:0; margin:-1px;
    overflow:hidden; clip:rect(0,0,0,0); white-space:nowrap; border:0;
  }}
  section{{ padding-block: clamp(48px, 8vw, 88px); }}
  .rule{{ height:5px; background:var(--green); border:none; margin:0; }}

  .h-display{{
    font-family:"Fraunces", Georgia, serif;
    font-weight:600;
    font-optical-sizing:auto;
    letter-spacing:0.005em;
    line-height:1.04;
    text-transform:uppercase;
  }}
  .eyebrow-script{{
    font-family:"Caveat", cursive;
    font-weight:700;
    font-size:1.5rem;
    color:var(--red);
  }}
  .kicker{{
    font-family:"Fraunces", Georgia, serif; font-weight:600;
    color:var(--red);
    text-transform:uppercase;
    font-size:clamp(1.5rem,3.4vw,2.1rem);
    text-align:center;
  }}
  .kicker + .subkicker{{ margin-top:6px; }}
  .subkicker{{
    text-align:center;
    font-family:"Archivo", sans-serif;
    font-weight:800;
    letter-spacing:0.04em;
    text-transform:uppercase;
    font-size:0.95rem;
    color:var(--ink);
  }}

  .btn{{
    display:inline-flex; align-items:center; gap:10px;
    padding:15px 30px;
    min-height:48px;
    border-radius:999px;
    font-family:"Archivo", sans-serif;
    font-weight:800;
    font-size:0.92rem;
    letter-spacing:0.03em;
    text-transform:uppercase;
    text-decoration:none;
    border:2px solid transparent;
    cursor:pointer;
    white-space:nowrap;
    touch-action:manipulation;
    transition:background-color 200ms ease, color 200ms ease, border-color 200ms ease, transform 150ms ease;
  }}
  .btn:active{{ transform:scale(0.97); }}
  .btn-red{{ background:var(--red); color:var(--cream-2); }}
  .btn-red:hover{{ background:var(--red-deep); }}
  .btn-green{{ background:var(--green); color:var(--cream-2); }}
  .btn-green:hover{{ background:var(--green-deep); }}
  .btn-gold{{ background:var(--gold); color:var(--ink); }}
  .btn-gold:hover{{ background:var(--gold-deep); color:var(--cream-2); }}
  .btn-outline{{ background:transparent; border-color:var(--ink); color:var(--ink); }}
  .btn-outline:hover{{ background:var(--ink); color:var(--cream); }}
  .btn:focus-visible, a:focus-visible{{ outline:3px solid var(--gold-deep); outline-offset:2px; }}
  .nav-links a{{ transition:color 200ms ease; }}
  .foot-links a{{ transition:color 200ms ease; }}

  /* placeholder image tile */
  .ph{{
    width:100%;
    border-radius:var(--radius);
    background:repeating-linear-gradient(135deg, var(--cream-2) 0 14px, var(--stripe) 14px 28px);
    border:2px dashed rgba(36,27,18,0.22);
    display:flex; flex-direction:column; align-items:center; justify-content:center; gap:10px;
    color:var(--muted);
  }}
  .ph-icon{{ width:34%; max-width:64px; color:var(--muted); opacity:0.55; }}
  .ph-label{{
    font-size:0.72rem; font-weight:700; letter-spacing:0.08em; text-transform:uppercase;
  }}

  /* ---------- HEADER ---------- */
  header.site{{
    position:sticky; top:env(safe-area-inset-top, 0px); z-index:50;
    background:var(--cream);
    border-bottom:3px solid var(--ink);
  }}
  .nav{{
    max-width:1180px; margin:0 auto;
    display:flex; align-items:center; justify-content:space-between;
    padding:14px 0; gap:20px;
  }}
  .nav-links{{
    display:flex; align-items:center; gap:26px; list-style:none; margin:0; padding:0;
  }}
  .nav-links a{{
    text-decoration:none; font-weight:800; font-size:0.82rem; letter-spacing:0.04em;
    text-transform:uppercase; color:var(--ink);
  }}
  .nav-links a:hover{{ color:var(--red); }}
  .brand{{
    display:flex; align-items:center; gap:9px; text-decoration:none; color:var(--ink);
    font-family:"Fraunces", Georgia, serif; font-weight:600; font-size:1.05rem; letter-spacing:0.02em; text-transform:uppercase;
    justify-content:center;
  }}
  .brand svg{{ width:34px; height:34px; color:var(--red); flex:none; }}
  .brand img{{ width:34px; height:34px; object-fit:contain; flex:none; }}
  .nav-right{{ display:flex; align-items:center; gap:14px; }}
  .hours-chip{{
    display:flex; align-items:center; gap:7px;
    font-size:0.78rem; font-weight:700; color:var(--ink-soft);
    border:1.5px solid var(--line); border-radius:999px; padding:9px 14px;
  }}
  .hours-chip svg{{ color:var(--red); }}
  .nav-toggle{{
    display:none;
    align-items:center; justify-content:center;
    width:44px; height:44px;
    border-radius:10px;
    border:1.5px solid var(--ink);
    background:transparent;
    cursor:pointer;
    touch-action:manipulation;
    flex:none;
  }}
  .nav-toggle svg{{ width:22px; height:22px; color:var(--ink); }}
  .nav-toggle .icon-close{{ display:none; }}
  .nav-toggle[aria-expanded="true"] .icon-open{{ display:none; }}
  .nav-toggle[aria-expanded="true"] .icon-close{{ display:block; }}
  .mobile-panel{{
    display:none;
    flex-direction:column;
    gap:4px;
    padding:10px 0 18px;
    border-top:1px solid var(--line);
  }}
  .mobile-panel.open{{ display:flex; }}
  .mobile-panel a{{
    display:block;
    padding:13px 4px;
    font-weight:800; font-size:0.95rem; text-transform:uppercase; letter-spacing:0.03em;
    text-decoration:none; color:var(--ink);
    border-bottom:1px solid var(--line);
  }}
  .mobile-panel .mp-hours{{
    display:flex; align-items:center; gap:8px;
    padding:13px 4px; font-size:0.85rem; font-weight:700; color:var(--ink-soft);
  }}
  .mobile-panel .mp-hours svg{{ color:var(--red); }}
  .mobile-panel .btn{{ margin-top:10px; justify-content:center; }}
  @media (max-width:900px){{
    .nav-links{{ display:none; }}
    .hours-chip{{ display:none; }}
    .nav-toggle{{ display:flex; }}
  }}

  /* ---------- HERO ---------- */
  .hero{{
    background:linear-gradient(160deg, var(--green) 0%, var(--green-deep) 100%);
    color:var(--cream-2);
    padding-block:clamp(56px,9vw,104px);
    position:relative;
    overflow:hidden;
  }}
  .hero-video{{
    position:absolute; inset:0;
    width:100%; height:100%;
    object-fit:cover; object-position:center 38%;
    z-index:0;
  }}
  .hero-video-overlay{{
    position:absolute; inset:0;
    background:linear-gradient(160deg, rgba(44,95,79,0.87) 0%, rgba(32,69,57,0.84) 55%, rgba(32,69,57,0.92) 100%);
    z-index:1;
  }}
  .hero::before{{
    content:"";
    position:absolute; inset:0;
    background-image:
      radial-gradient(circle at 12% 20%, rgba(255,255,255,0.07) 0 2px, transparent 3px),
      radial-gradient(circle at 85% 30%, rgba(255,255,255,0.06) 0 2px, transparent 3px),
      radial-gradient(circle at 70% 80%, rgba(255,255,255,0.06) 0 2px, transparent 3px),
      radial-gradient(circle at 25% 75%, rgba(255,255,255,0.05) 0 2px, transparent 3px);
    pointer-events:none;
    z-index:2;
  }}
  .hero-inner{{
    position:relative;
    z-index:3;
    display:flex; flex-direction:column; align-items:center; text-align:center; gap:22px;
    max-width:900px; margin:0 auto;
  }}
  @media (prefers-reduced-motion: reduce){{
    .hero-video{{ display:none; }}
    .hero{{ background-image:linear-gradient(160deg, rgba(44,95,79,0.87) 0%, rgba(32,69,57,0.92) 100%), url("hero-poster.jpg"); background-size:cover; background-position:center 38%; }}
  }}
  .hero-shell{{ width:60px; height:60px; color:var(--gold); flex:none; }}
  .hero h1{{
    font-size:clamp(2.3rem, 6.6vw, 4rem);
    color:var(--cream-2);
    white-space:nowrap;
  }}
  @media (max-width:640px){{ .hero h1{{ white-space:normal; }} }}
  .hero h1 .accent{{ color:var(--gold); }}
  .hero-script{{
    font-family:"Caveat", cursive;
    font-weight:700;
    font-size:clamp(1.5rem, 3vw, 2rem);
    color:var(--cream-2);
    opacity:0.92;
  }}
  .hero-cta{{ display:flex; flex-wrap:wrap; justify-content:center; gap:14px; margin-top:6px; }}
  .hero-badges{{
    display:flex; flex-wrap:wrap; justify-content:center; gap:10px 26px;
    margin-top:22px; padding-top:22px; border-top:1px solid rgba(247,239,224,0.25);
    font-size:0.82rem; font-weight:700;
  }}
  .hero-badges span{{ display:flex; align-items:center; gap:8px; color:var(--cream-2); opacity:0.92; }}
  .hero-badges svg{{ color:var(--gold); }}

  /* ---------- ICON STRIP ---------- */
  .icon-strip{{
    background:var(--cream-2);
    border-top:1px solid var(--line); border-bottom:1px solid var(--line);
    overflow:hidden;
  }}
  .icon-strip-row{{
    display:flex; gap:26px; padding-block:16px; justify-content:center; flex-wrap:wrap;
  }}
  .strip-icon{{ width:20px; height:20px; }}

  /* ---------- BEST SELLERS ---------- */
  .best-grid{{
    margin-top:40px;
    display:grid; grid-template-columns:repeat(3,1fr); gap:34px;
  }}
  @media (max-width:860px){{ .best-grid{{ grid-template-columns:1fr; max-width:420px; margin-inline:auto; }} }}
  .best-card{{ display:flex; flex-direction:column; gap:16px; position:relative; }}
  .best-card .ph{{ aspect-ratio:1/1; }}
  .best-badge{{
    position:absolute; top:-14px; right:-14px; width:104px; height:104px; color:var(--gold);
    display:flex; align-items:center; justify-content:center;
  }}
  .best-badge span{{
    position:absolute; color:var(--ink); font-family:"Archivo",sans-serif; font-weight:800;
    font-size:0.68rem; line-height:1.15; text-align:center; text-transform:uppercase; width:64px;
  }}
  .best-name{{ font-family:"Fraunces", Georgia, serif; font-weight:600; font-size:1.3rem; text-transform:uppercase; text-align:center; }}
  .best-desc{{ text-align:center; color:var(--ink-soft); font-size:0.92rem; line-height:1.5; }}
  .best-cta{{ text-align:center; margin-top:44px; }}

  /* ---------- INTRO / ABOUT ---------- */
  .about-grid{{
    display:grid; grid-template-columns:1.05fr 0.9fr; gap:16px 64px; align-items:center;
  }}
  @media (max-width:900px){{ .about-grid{{ grid-template-columns:1fr; gap:56px; }} }}

  .about-text, .about-visual{{
    opacity:0; transform:translateY(30px);
    transition:opacity 750ms ease, transform 750ms cubic-bezier(.22,.8,.24,1);
  }}
  .about-grid.reveal-armed .about-text{{ transition-delay:0ms; }}
  .about-grid.reveal-armed .about-visual{{ transition-delay:120ms; }}
  .about-grid.reveal-armed .in-view{{ opacity:1; transform:translateY(0); }}
  .about-grid:not(.reveal-armed) .about-text,
  .about-grid:not(.reveal-armed) .about-visual{{ opacity:1; transform:none; }}

  .about-label{{
    font-family:"Archivo", sans-serif; font-weight:800; font-size:0.78rem;
    letter-spacing:0.14em; text-transform:uppercase; color:var(--red); margin-bottom:10px;
  }}
  .about-heading{{ font-size:clamp(1.9rem,4.1vw,2.6rem); text-transform:uppercase; line-height:1.14; }}
  .about-strike{{
    color:var(--ink-soft);
    text-decoration-line:line-through; text-decoration-color:var(--red);
    text-decoration-thickness:3px; text-underline-offset:0;
    transition:text-decoration-color 700ms ease 350ms;
  }}
  .about-grid.reveal-armed .about-strike{{ text-decoration-color:transparent; }}
  .about-grid.reveal-armed .in-view .about-strike{{ text-decoration-color:var(--red); }}
  .about-accent{{ display:block; color:var(--red); margin-top:6px; }}
  .about-text > p{{ margin-top:20px; color:var(--ink-soft); font-size:1.02rem; line-height:1.75; max-width:52ch; }}

  .about-badges{{
    margin-top:26px; display:flex; flex-direction:column; gap:12px;
  }}
  .about-badges span{{
    display:flex; align-items:center; gap:12px; font-size:0.9rem; font-weight:700; color:var(--ink);
  }}
  .about-badge-ico{{
    display:flex; align-items:center; justify-content:center; flex:none;
    width:32px; height:32px; border-radius:50%; background:var(--cream-2); border:1.5px solid var(--line); color:var(--green);
  }}
  .about-badge-ico svg{{ width:15px; height:15px; }}

  .about-visual{{ position:relative; }}
  .about-photo-stack{{ position:relative; max-width:400px; margin-inline:auto; }}
  .about-photo-stack .ph{{ border-radius:var(--radius); box-shadow:0 18px 38px rgba(36,27,18,0.18); }}
  .about-photo.ap1{{ transform:rotate(-4deg); }}
  .about-photo.ap2{{
    position:absolute; width:58%; right:-6%; bottom:-9%; z-index:2;
  }}
  .about-photo.ap2 .ph{{ transform:rotate(5deg); border:5px solid var(--cream); }}
  .about-stamp{{
    position:absolute; top:-24px; left:-20px; width:98px; height:98px; z-index:3; color:var(--red);
    animation:about-spin 17s linear infinite;
  }}
  .about-stamp-ring{{ width:100%; height:100%; display:block; }}
  @keyframes about-spin{{ to{{ transform:rotate(360deg); }} }}
  @media (prefers-reduced-motion: reduce){{ .about-stamp{{ animation:none; }} }}
  @media (max-width:900px){{ .about-photo-stack{{ margin-top:12px; }} }}
  @media (max-width:480px){{
    .about-stamp{{ top:-12px; left:-4px; width:64px; height:64px; }}
  }}

  /* ---------- STEPS ---------- */
  .steps{{ background:var(--cream-2); overflow:hidden; }}
  .steps-rail{{
    position:relative;
    margin-top:56px; display:grid; grid-template-columns:repeat(3,1fr); gap:34px;
  }}
  .steps-rail::before{{
    content:""; position:absolute; left:5%; right:5%; top:64px;
    border-top:2px dashed rgba(36,27,18,0.22); z-index:0;
  }}
  .step-arrow{{
    position:absolute; top:50px; width:28px; height:28px; z-index:1;
    background:var(--cream-2); border:2px solid var(--ink); border-radius:50%;
    display:flex; align-items:center; justify-content:center; color:var(--ink);
  }}
  .step-arrow.a1{{ left:calc(33.333% - 14px); }}
  .step-arrow.a2{{ left:calc(66.666% - 14px); }}
  @media (max-width:860px){{
    .steps-rail{{ grid-template-columns:1fr; max-width:400px; margin-inline:auto; gap:44px; }}
    .steps-rail::before, .step-arrow{{ display:none; }}
  }}
  .step-card{{ position:relative; z-index:1; }}
  .step-card:nth-child(1){{ --tone:var(--red); --tilt:-4deg; }}
  .step-card:nth-child(3){{ --tone:var(--green); --tilt:3deg; }}
  .step-card:nth-child(5){{ --tone:var(--gold-deep); --tilt:-3deg; }}
  .step-card-body{{
    position:relative; height:100%; overflow:hidden;
    background:var(--cream);
    border:1.5px solid var(--ink);
    border-radius:var(--radius);
    padding:26px 22px 24px;
  }}
  .step-bignum{{
    position:absolute; top:-0.22em; right:-0.03em;
    font-family:"Fraunces", Georgia, serif; font-weight:600; font-size:clamp(4.6rem,9vw,6.4rem);
    line-height:1; color:var(--tone, var(--red)); opacity:0.2;
    pointer-events:none; z-index:0; user-select:none;
  }}
  .step-photo{{
    position:relative; z-index:1; width:74px; aspect-ratio:1/1; margin-bottom:16px;
    transform:rotate(var(--tilt,-3deg));
    box-shadow:0 8px 16px rgba(36,27,18,0.18);
    transition:transform 260ms ease;
  }}
  .step-photo .ph{{ width:100%; height:100%; border-radius:10px; gap:0; }}
  .step-photo .ph-icon{{ width:44%; opacity:0.5; }}
  .step-photo .ph-label{{ display:none; }}
  .step-title{{ position:relative; z-index:1; font-family:"Fraunces", Georgia, serif; font-weight:600; font-size:1.05rem; text-transform:uppercase; }}
  .step-desc{{ position:relative; z-index:1; margin-top:10px; font-size:0.9rem; color:var(--ink-soft); line-height:1.6; }}

  /* scroll-reveal: only takes effect once JS arms it, so the section
     is fully visible by default without JavaScript */
  .steps-rail.reveal-armed .step-card{{
    opacity:0; transform:translateY(30px);
    transition:opacity 650ms cubic-bezier(.2,.7,.3,1), transform 650ms cubic-bezier(.2,.7,.3,1);
  }}
  .steps-rail.reveal-armed .step-card:nth-child(3){{ transition-delay:110ms; }}
  .steps-rail.reveal-armed .step-card:nth-child(5){{ transition-delay:220ms; }}
  .steps-rail.reveal-armed .step-card.in-view{{ opacity:1; transform:translateY(0); }}

  @media (hover:hover) and (pointer:fine){{
    .step-card-body{{ transition:transform 260ms ease, box-shadow 260ms ease; }}
    .step-card-body:hover{{ transform:translateY(-6px); box-shadow:0 16px 28px rgba(36,27,18,0.16); }}
    .step-card-body:hover .step-photo{{ transform:rotate(0deg) scale(1.06); }}
  }}

  /* ---------- MENU ---------- */
  .menu-head{{ text-align:center; }}
  .menu-head h2{{ font-size:clamp(2.1rem,5vw,3.1rem); text-transform:uppercase; margin-top:6px; }}
  .menu-note{{
    max-width:620px; margin:28px auto 0;
    display:flex; align-items:center; justify-content:center; gap:10px;
    background:var(--cream-2); border:1.5px dashed var(--gold-deep); color:var(--ink-soft);
    padding:12px 18px; border-radius:12px; font-size:0.88rem; font-weight:700;
  }}
  .menu-grid{{
    margin-top:38px;
    display:grid; grid-template-columns:repeat(auto-fill, minmax(250px,1fr)); gap:28px;
  }}
  .bowl{{ display:flex; flex-direction:column; gap:14px; }}
  .bowl-body{{ text-align:left; }}
  .bowl-name{{
    font-family:"Fraunces", Georgia, serif; font-weight:600; font-size:1.12rem; text-transform:uppercase; color:var(--ink);
    display:flex; flex-direction:column; gap:4px;
  }}
  .bowl-note{{ font-family:"Archivo",sans-serif; font-size:0.68rem; font-weight:700; letter-spacing:0.05em; text-transform:uppercase; color:var(--red); }}
  .bowl-ing{{ margin-top:4px; font-size:0.86rem; color:var(--ink-soft); line-height:1.5; }}
  .bowl-prices{{ display:flex; gap:10px; padding-top:12px; border-top:1.5px solid var(--line); }}
  .price-pill{{ flex:1; text-align:center; padding:9px 6px; border-radius:9px; background:var(--cream-2); border:1px solid var(--line); }}
  .price-pill .who{{ display:block; font-size:0.63rem; letter-spacing:0.06em; text-transform:uppercase; color:var(--muted); }}
  .price-pill .amt{{ font-family:"Fraunces", Georgia, serif; font-weight:600; font-size:1.05rem; color:var(--red); font-variant-numeric:tabular-nums; }}
  .price-pill.off .amt{{ color:var(--muted); }}

  .addons{{ margin-top:46px; padding-top:34px; border-top:3px solid var(--ink); max-width:900px; margin-inline:auto; }}
  .addons-title{{ font-family:"Fraunces", Georgia, serif; font-weight:600; font-size:1.15rem; text-transform:uppercase; text-align:center; color:var(--green); }}
  .addons-list{{
    list-style:none; margin:22px 0 0; padding:0;
    display:grid; grid-template-columns:repeat(auto-fill, minmax(230px,1fr)); gap:0 30px;
  }}
  .addons-list li{{
    display:flex; justify-content:space-between; align-items:baseline; padding:12px 0;
    border-bottom:1px dotted var(--line);
    font-family:"Fraunces", Georgia, serif; font-weight:500; font-size:1.05rem;
  }}
  .addons-list li b{{ font-weight:700; color:var(--red); font-variant-numeric:tabular-nums; }}

  /* ---------- TESTIMONIALS ---------- */
  .reviews-head{{ text-align:center; }}

  /* ---------- WORD-SWAP TAGLINE (feature) ---------- */
  .word-swap-wrap{{ margin-top:18px; text-align:center; padding-block:24px; }}
  .word-swap-line{{
    text-align:center;
    font-family:"Fraunces", Georgia, serif; font-weight:600; text-transform:uppercase;
    font-size:clamp(2.2rem,6.4vw,4.6rem); color:var(--ink);
  }}
  .word-swap-line > span:first-child{{ margin-right:0.32em; }}
  .word-swap{{
    display:inline-grid; overflow:hidden; text-align:center; vertical-align:bottom; padding-bottom:0.12em;
  }}
  .word-swap-item{{
    grid-area:1/1;
    color:var(--red);
    opacity:0; transform:translateY(55%);
    transition:transform 550ms cubic-bezier(.22,.8,.24,1), opacity 420ms ease;
    white-space:nowrap;
  }}
  .word-swap-item.is-active{{ opacity:1; transform:translateY(0); }}
  .reviews-trust{{
    margin-top:22px; display:flex; flex-direction:column; align-items:center; gap:6px;
  }}
  .reviews-trust .stars-row{{ color:var(--gold-deep); letter-spacing:3px; font-size:1.1rem; }}
  .reviews-trust .trust-caption{{
    font-size:0.78rem; font-weight:700; letter-spacing:0.06em; text-transform:uppercase; color:var(--muted);
  }}
  .word-swap-item.is-exiting{{ opacity:0; transform:translateY(-55%); }}
  @media (max-width:640px){{ .word-swap-line{{ font-size:clamp(2rem,10vw,2.8rem); }} }}

  /* ---------- CTA BAND ---------- */
  /* The idea: an order "ticket" you could tear off, not a row of pills.
     Live status (åbent nu / åbner om ...) is computed from the real
     Fri+Sat 15–20 Europe/Copenhagen hours, so the countdown is genuine,
     not decorative — the whole point is to make the wait (or the lack
     of one) feel real and worth acting on right now. */
  .cta-band{{ background:var(--red); color:var(--cream-2); overflow:hidden; }}
  .cta-grid{{
    display:grid; grid-template-columns:1.05fr 0.9fr; gap:20px 64px; align-items:center;
  }}
  @media (max-width:900px){{
    .cta-grid{{ grid-template-columns:1fr; gap:52px; text-align:center; }}
  }}
  .cta-text, .cta-ticket-wrap{{
    min-width:0;
    opacity:0; transform:translateY(28px);
    transition:opacity 750ms ease, transform 750ms cubic-bezier(.22,.8,.24,1);
  }}
  .cta-grid.reveal-armed .cta-ticket-wrap{{ transition-delay:110ms; }}
  .cta-grid.reveal-armed .in-view{{ opacity:1; transform:translateY(0); }}
  .cta-grid:not(.reveal-armed) .cta-text,
  .cta-grid:not(.reveal-armed) .cta-ticket-wrap{{ opacity:1; transform:none; }}

  .cta-kicker{{
    display:inline-flex; align-items:center; gap:9px;
    font-family:"Archivo",sans-serif; font-weight:800; font-size:0.76rem;
    letter-spacing:0.1em; text-transform:uppercase; color:var(--gold);
    background:rgba(247,239,224,0.14); border:1px solid rgba(247,239,224,0.4);
    padding:8px 16px; border-radius:999px;
  }}
  .order-dot{{
    width:9px; height:9px; border-radius:50%; flex:none; background:var(--gold);
    animation:order-pulse 2s ease-out infinite;
  }}
  @keyframes order-pulse{{
    0%{{ box-shadow:0 0 0 0 rgba(221,164,62,0.5); }}
    70%{{ box-shadow:0 0 0 9px rgba(221,164,62,0); }}
    100%{{ box-shadow:0 0 0 0 rgba(221,164,62,0); }}
  }}
  .order-dot.is-open{{ background:#6fcf97; animation-name:order-pulse-open; }}
  @keyframes order-pulse-open{{
    0%{{ box-shadow:0 0 0 0 rgba(111,207,151,0.55); }}
    70%{{ box-shadow:0 0 0 10px rgba(111,207,151,0); }}
    100%{{ box-shadow:0 0 0 0 rgba(111,207,151,0); }}
  }}

  .cta-text h2{{ margin-top:16px; font-size:clamp(2.1rem,5.4vw,3.4rem); color:var(--cream-2); }}
  .cta-copy{{
    margin-top:14px; max-width:44ch; color:rgba(251,246,236,0.86);
    font-size:1.05rem; line-height:1.6;
  }}
  @media (max-width:900px){{ .cta-copy{{ margin-inline:auto; }} }}
  .cta-buttons{{ margin-top:28px; display:flex; flex-wrap:wrap; gap:14px; }}
  @media (max-width:900px){{ .cta-buttons{{ justify-content:center; }} }}
  .phone-chip{{
    display:inline-flex; align-items:center; gap:9px; padding:15px 26px; border-radius:999px;
    border:2px dashed rgba(247,239,224,0.55); color:var(--cream-2); font-weight:800; font-size:0.88rem;
    text-transform:uppercase; letter-spacing:0.02em; text-decoration:none;
    transition:background-color 200ms ease, border-color 200ms ease;
  }}
  .phone-chip:hover, .phone-chip:focus-visible{{
    background:rgba(247,239,224,0.14); border-color:rgba(247,239,224,0.85);
  }}

  /* the ticket */
  .cta-ticket-wrap{{ display:flex; }}
  .cta-ticket{{
    position:relative; margin-inline:auto; width:100%; max-width:380px;
    background:var(--cream-2); color:var(--ink); border-radius:18px;
    padding:28px 26px 24px; box-shadow:0 26px 54px rgba(20,10,4,0.32);
    transform:rotate(-2.5deg);
    animation:ticket-sway 6.5s ease-in-out infinite;
  }}
  @keyframes ticket-sway{{
    0%, 100%{{ transform:rotate(-2.5deg); }}
    50%{{ transform:rotate(-1deg); }}
  }}
  .cta-ticket::before{{
    content:""; position:absolute; inset:9px; border-radius:10px;
    border:1.5px dashed rgba(36,27,18,0.22); pointer-events:none;
  }}
  .ticket-head{{
    display:flex; align-items:baseline; justify-content:space-between; gap:10px;
    padding-bottom:14px; border-bottom:2px dashed rgba(36,27,18,0.24);
    font-family:"Courier New",ui-monospace,Menlo,monospace;
  }}
  .ticket-eyebrow{{
    font-weight:700; font-size:0.68rem; letter-spacing:0.1em; text-transform:uppercase;
    color:var(--ink-soft);
  }}
  .ticket-date{{
    font-weight:700; font-size:0.68rem; letter-spacing:0.04em; color:var(--red); text-align:right;
  }}
  .ticket-lines{{ margin-top:6px; display:flex; flex-direction:column; }}
  .ticket-line{{
    display:flex; align-items:center; gap:7px; padding:9px 0;
    font-size:0.85rem;
  }}
  .ticket-line + .ticket-line{{ border-top:1px dashed rgba(36,27,18,0.14); }}
  .ticket-label{{
    display:flex; align-items:center; gap:7px; color:var(--ink-soft); white-space:nowrap; flex:none;
  }}
  .ticket-label svg{{ color:var(--red); flex:none; }}
  .ticket-fill{{ flex:1; min-width:10px; border-bottom:2px dotted rgba(36,27,18,0.28); margin-bottom:4px; }}
  .ticket-value{{ font-weight:800; white-space:nowrap; flex:none; }}

  .ticket-tear{{
    position:relative; margin:18px -26px 0; border-top:2px dashed rgba(36,27,18,0.3);
  }}
  .ticket-tear::before, .ticket-tear::after{{
    content:""; position:absolute; top:50%; transform:translateY(-50%);
    width:22px; height:22px; border-radius:50%; background:var(--red);
  }}
  .ticket-tear::before{{ left:-11px; }}
  .ticket-tear::after{{ right:-11px; }}

  .ticket-stub{{
    margin-top:18px; display:flex; align-items:center; justify-content:space-between; gap:10px;
  }}
  .stub-label{{
    font-family:"Courier New",ui-monospace,Menlo,monospace; font-weight:700; font-size:0.66rem;
    letter-spacing:0.1em; text-transform:uppercase; color:var(--ink-soft); flex:none;
  }}
  .stub-status{{
    font-family:"Fraunces",Georgia,serif; font-weight:600; font-size:1.05rem;
    color:var(--red); text-align:right; transition:color 300ms ease;
  }}
  .stub-status.is-open{{ color:var(--green); }}

  @media (prefers-reduced-motion: reduce){{
    .cta-ticket{{ animation:none; transform:rotate(-2.5deg); }}
  }}

  /* ---------- FOOTER ---------- */
  footer{{ padding-block:56px 30px; }}
  .foot-grid{{
    display:grid; grid-template-columns:1.4fr 1fr 1fr; gap:30px;
  }}
  @media (max-width:820px){{ .foot-grid{{ grid-template-columns:1fr 1fr; }} }}
  @media (max-width:520px){{ .foot-grid{{ grid-template-columns:1fr; }} }}
  .foot-brand{{ display:flex; align-items:center; gap:10px; margin-bottom:14px; }}
  .foot-brand svg{{ width:30px; height:30px; color:var(--red); }}
  .foot-brand img{{ width:34px; height:34px; object-fit:contain; }}
  .foot-brand span{{ font-family:"Fraunces", Georgia, serif; font-weight:600; text-transform:uppercase; font-size:1rem; }}
  .foot-tag{{ font-family:"Caveat", cursive; font-weight:700; font-size:1.2rem; color:var(--ink-soft); }}
  .foot-col-title{{ font-family:"Archivo", sans-serif; font-weight:800; font-size:0.76rem; letter-spacing:0.08em; text-transform:uppercase; color:var(--muted); margin-bottom:14px; }}
  .foot-links{{ list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:2px; }}
  .foot-links a{{ text-decoration:none; color:var(--ink); font-size:0.92rem; font-weight:600; display:inline-block; padding-block:8px; }}
  .foot-links a:hover{{ color:var(--red); }}
  .foot-fine{{
    margin-top:44px; padding-top:22px; border-top:1px solid var(--line);
    display:flex; flex-wrap:wrap; justify-content:space-between; gap:12px;
    font-size:0.78rem; color:var(--muted);
  }}
</style>
</head>
<body>

<header class="site">
  <nav class="nav wrap">
    <a class="brand" href="#top">
      <img src="logo-mark.png" alt="Aalborg Seafood Boil logo" width="34" height="34">
      Aalborg Seafood Boil
    </a>
    <ul class="nav-links">
      <li><a href="#menu">Menu</a></li>
      <li><a href="#koncept">Konceptet</a></li>
      <li><a href="#anmeldelser">Anmeldelser</a></li>
      <li><a href="#bestil">Kontakt</a></li>
    </ul>
    <div class="nav-right">
      <span class="hours-chip">{PIN} Aalborg &middot; {CLOCK} Fre&ndash;L&oslash;r</span>
      <a class="btn btn-red" href="https://instagram.com/seafoodboilaalborg" target="_blank" rel="noopener">Bestil nu</a>
      <button type="button" class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="mobilePanel" aria-label="&Aring;bn menu">
        <svg class="icon-open" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
        <svg class="icon-close" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
      </button>
    </div>
  </nav>
  <div class="wrap">
    <nav class="mobile-panel" id="mobilePanel" aria-label="Mobilmenu">
      <a href="#menu">Menu</a>
      <a href="#koncept">Konceptet</a>
      <a href="#anmeldelser">Anmeldelser</a>
      <a href="#bestil">Kontakt</a>
      <span class="mp-hours">{PIN} Aalborg &middot; {CLOCK} Fredag &amp; l&oslash;rdag, 15&ndash;20</span>
      <a class="btn btn-red" href="https://instagram.com/seafoodboilaalborg" target="_blank" rel="noopener">Bestil nu</a>
    </nav>
  </div>
</header>

<main id="top">

  <section class="hero">
    <video class="hero-video" autoplay muted loop playsinline preload="auto" poster="hero-poster.jpg" aria-hidden="true">
      <source src="hero-video.mp4" type="video/mp4">
    </video>
    <div class="hero-video-overlay" aria-hidden="true"></div>
    <div class="hero-inner">
      {shell_icon("hero-shell")}
      <h1 class="h-display">Seafood boil<br>i <span class="accent">Aalborg</span></h1>
      <p class="hero-script">Riv posen op &amp; del med dem du elsker!</p>
      <div class="hero-cta">
        <a class="btn btn-gold" href="https://instagram.com/seafoodboilaalborg" target="_blank" rel="noopener">{IG} Bestil på Instagram</a>
        <a class="btn btn-outline" style="border-color:var(--cream-2); color:var(--cream-2);" href="#menu">Se menuen</a>
      </div>
      <div class="hero-badges">
        <span>{CHECK} Registreret hos F&oslash;devarestyrelsen</span>
        <span>{CLOCK} Fredag &amp; l&oslash;rdag, 15&ndash;20</span>
        <span>{PIN} Afhentning i Aalborg</span>
      </div>
    </div>
  </section>

  <div class="icon-strip">
    <div class="icon-strip-row">
      {STRIP}
    </div>
  </div>

  <section class="best wrap">
    <p class="kicker h-display">Hvad alle snakker om</p>
    <p class="subkicker">ASB favoritter</p>
    <div class="best-grid">

      <div class="best-card">
        <div style="position:relative;">
          {placeholder("Foto på vej", "1/1")}
          <div class="best-badge">
            {star_svg()}
            <span>Mest bestilt</span>
          </div>
        </div>
        <p class="best-name h-display">Deluxe Bowl</p>
        <p class="best-desc">Rejer, krebs, blæksprutte, blåmuslinger, majs, kartofler og snekrabbeben i vores signatursauce.</p>
      </div>

      <div class="best-card">
        <div style="position:relative;">
          {placeholder("Foto på vej", "1/1")}
          <div class="best-badge">
            {star_svg()}
            <span>Kundernes favorit</span>
          </div>
        </div>
        <p class="best-name h-display">Mix Bowl</p>
        <p class="best-desc">Rejer, baby blæksprutte og blåmuslinger med majs og kartofler, lidt af det hele.</p>
      </div>

      <div class="best-card">
        <div style="position:relative;">
          {placeholder("Foto på vej", "1/1")}
          <div class="best-badge">
            {star_svg()}
            <span>For de sultne</span>
          </div>
        </div>
        <p class="best-name h-display">Luksus Bowl</p>
        <p class="best-desc">Hummer, snekrabbe, rejer, grønmuslinger og krebs. Den store gryde til to.</p>
      </div>

    </div>
    <div class="best-cta">
      <a class="btn btn-red" href="#menu">Se hele menuen</a>
    </div>
  </section>

  <hr class="rule">

  <section class="about wrap" id="koncept">
    <div class="about-grid" id="aboutGrid">
      <div class="about-text">
        <p class="about-label">Konceptet</p>
        <h2 class="about-heading h-display">
          <span class="about-strike">Ikke en restaurant.</span>
          <span class="about-accent">Et k&oslash;kken med ambitioner.</span>
        </h2>
        <p>Aalborg Seafood Boil bringer den r&aring; smag af en amerikansk seafood boil til Aalborg. Fra vores signatur cajun-sauce til friske rejer, krebs og bl&aring;muslinger: alt koges fra bunden i et privat k&oslash;kken, med samme ambition som en professionel restaurant. Bestil dagen f&oslash;r, hent fredag eller l&oslash;rdag, og riv posen op derhjemme.</p>
        <div class="about-badges">
          <span><span class="about-badge-ico">{CHECK}</span>Hobbyvirksomhed fra privat hjem</span>
          <span><span class="about-badge-ico">{CHECK}</span>Registreret hos F&oslash;devarestyrelsen</span>
          <span><span class="about-badge-ico">{CHECK}</span>Kogt til orden, ikke til lager</span>
        </div>
      </div>
      <div class="about-visual">
        <div class="about-photo-stack">
          <div class="about-photo ap1">{placeholder("Foto på vej", "4/5")}</div>
          <div class="about-photo ap2">{placeholder("Foto på vej", "1/1")}</div>
          <div class="about-stamp">{stamp_badge()}</div>
        </div>
      </div>
    </div>
  </section>

  <hr class="rule">

  <section class="steps">
    <div class="wrap">
      <p class="kicker h-display">Bestil i dag, spis i morgen</p>
      <p class="subkicker">S&aring;dan fungerer det</p>
      <div class="steps-rail" id="stepsRail">
        <div class="step-card">
          <div class="step-card-body">
            <span class="step-bignum" aria-hidden="true">01</span>
            <div class="step-photo">{placeholder("Foto på vej", "1/1")}</div>
            <p class="step-title h-display">Bestil på Instagram</p>
            <p class="step-desc">Send en besked til @seafoodboilaalborg, helst dagen f&oslash;r, s&aring; vi kan planl&aelig;gge friskt til jer.</p>
          </div>
        </div>
        <div class="step-arrow a1" aria-hidden="true">{STEP_ARROW}</div>
        <div class="step-card">
          <div class="step-card-body">
            <span class="step-bignum" aria-hidden="true">02</span>
            <div class="step-photo">{placeholder("Foto på vej", "1/1")}</div>
            <p class="step-title h-display">Vi koger frisk</p>
            <p class="step-desc">Fredag og l&oslash;rdag, kl. 15&ndash;20, bliver jeres boil kogt fra bunden i v&aring;rt k&oslash;kken.</p>
          </div>
        </div>
        <div class="step-arrow a2" aria-hidden="true">{STEP_ARROW}</div>
        <div class="step-card">
          <div class="step-card-body">
            <span class="step-bignum" aria-hidden="true">03</span>
            <div class="step-photo">{placeholder("Foto på vej", "1/1")}</div>
            <p class="step-title h-display">Afhent &amp; riv posen op</p>
            <p class="step-desc">Hent i Aalborg og betal med MobilePay eller kontant. Gratis ris og handsker f&oslash;lger med.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="menu wrap" id="menu">
    <div class="menu-head">
      <p class="kicker h-display">V&aelig;lg din bowl</p>
      <h2 class="h-display">Menukortet</h2>
      <div class="menu-note">{shell_icon("", 'width="18" height="18"')} Alle bowls serveres med gratis ris og handsker.</div>
    </div>
    <div class="menu-grid">
      {BOWL_CARDS}
    </div>
    <div class="addons">
      <p class="addons-title h-display">Tilf&oslash;jelser</p>
      <ul class="addons-list">
        <li>Hel hummer <b>200 kr</b></li>
        <li>Snekrabbe clutchers <b>100 kr</b></li>
        <li>Kyllingep&oslash;lse <b>10 kr/stk</b></li>
        <li>Ekstra sauce <b>20 kr/stk</b></li>
        <li>Ekstra skaldyr <b>10 kr/stk</b></li>
      </ul>
    </div>
  </section>

  <section class="reviews wrap" id="anmeldelser">
    <div class="reviews-head">
      <p class="kicker h-display">Kunderne siger</p>
    </div>
    <div class="word-swap-wrap">
      <p class="word-swap-line">
        <span>Maden er</span>
        <span class="word-swap" id="wordSwap" aria-hidden="true">
          <span class="word-swap-item is-active">l&aelig;kker</span>
          <span class="word-swap-item">frisk</span>
          <span class="word-swap-item">saftig</span>
          <span class="word-swap-item">m&aelig;ttende</span>
          <span class="word-swap-item">autentisk</span>
          <span class="word-swap-item">gener&oslash;s</span>
        </span>
      </p>
      <span class="sr-only">Maden er l&aelig;kker, frisk, saftig, m&aelig;ttende, autentisk og gener&oslash;s.</span>
      <div class="reviews-trust">
        <span class="stars-row" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
        <span class="trust-caption">Efter ord fra vores kunder p&aring; Instagram</span>
      </div>
    </div>
  </section>

  <section class="cta-band" id="bestil">
    <div class="wrap cta-grid" id="ctaGrid">
      <div class="cta-text">
        <p class="cta-kicker"><span class="order-dot" id="orderDot" aria-hidden="true"></span><span id="orderStatusText">Fredag &amp; l&oslash;rdag, 15&ndash;20</span></p>
        <h2 class="h-display">Vi er kun en pose v&aelig;k</h2>
        <p class="cta-copy">Sig til n&aring;r sulten melder sig, s&aring; pakkes posen frisk, lige n&aring;r du bestiller den.</p>
        <div class="cta-buttons">
          <a class="btn btn-gold" href="https://instagram.com/seafoodboilaalborg" target="_blank" rel="noopener">{IG} @seafoodboilaalborg</a>
          <a class="phone-chip" href="tel:+4550109468">{PHONE} +45 50 10 94 68</a>
        </div>
      </div>

      <div class="cta-ticket-wrap">
        <div class="cta-ticket">
          <div class="ticket-head">
            <span class="ticket-eyebrow">Bestillings-kvittering</span>
            <span class="ticket-date" id="ticketDate">Frisk i weekenden</span>
          </div>
          <div class="ticket-lines">
            <div class="ticket-line">
              <span class="ticket-label">{CLOCK}&Aring;bningstid</span>
              <span class="ticket-fill" aria-hidden="true"></span>
              <span class="ticket-value">Fre &amp; l&oslash;r, 15&ndash;20</span>
            </div>
            <div class="ticket-line">
              <span class="ticket-label">{PIN}Afhentning</span>
              <span class="ticket-fill" aria-hidden="true"></span>
              <span class="ticket-value">Aalborg</span>
            </div>
            <div class="ticket-line">
              <span class="ticket-label">{CARD_PAY}Betaling</span>
              <span class="ticket-fill" aria-hidden="true"></span>
              <span class="ticket-value">MobilePay / kontant</span>
            </div>
          </div>
          <div class="ticket-tear" aria-hidden="true"></div>
          <div class="ticket-stub">
            <span class="stub-label">Status</span>
            <span class="stub-status" id="ticketStatus">&Aring;bner fredag kl. 15</span>
          </div>
        </div>
      </div>
    </div>
  </section>

</main>

<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="foot-brand"><img src="logo-mark.png" alt="Aalborg Seafood Boil logo" width="34" height="34"><span>Aalborg<br>Seafood Boil</span></div>
        <p class="foot-tag">Taste. Share. Enjoy.</p>
      </div>
      <div>
        <p class="foot-col-title">Menu</p>
        <ul class="foot-links">
          <li><a href="#menu">Alle bowls</a></li>
          <li><a href="#menu">Tilf&oslash;jelser</a></li>
          <li><a href="#koncept">Konceptet</a></li>
        </ul>
      </div>
      <div>
        <p class="foot-col-title">Bestil</p>
        <ul class="foot-links">
          <li><a href="https://instagram.com/seafoodboilaalborg" target="_blank" rel="noopener">Instagram DM</a></li>
          <li><a href="tel:+4550109468">+45 50 10 94 68</a></li>
          <li><a href="#bestil">&Aring;bningstider</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-fine">
      <span>&copy; 2026 Aalborg Seafood Boil &middot; Hobbyvirksomhed fra privat k&oslash;kken</span>
      <span>Registreret hos F&oslash;devarestyrelsen</span>
    </div>
  </div>
</footer>

<script>
  (function(){{
    var toggle = document.getElementById('navToggle');
    var panel = document.getElementById('mobilePanel');
    if(!toggle || !panel) return;
    function closePanel(){{
      panel.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-label', '\\u00c5bn menu');
    }}
    function openPanel(){{
      panel.classList.add('open');
      toggle.setAttribute('aria-expanded', 'true');
      toggle.setAttribute('aria-label', 'Luk menu');
    }}
    toggle.addEventListener('click', function(){{
      if(panel.classList.contains('open')){{ closePanel(); }} else {{ openPanel(); }}
    }});
    panel.querySelectorAll('a').forEach(function(a){{
      a.addEventListener('click', closePanel);
    }});
    document.addEventListener('keydown', function(e){{
      if(e.key === 'Escape') closePanel();
    }});
    window.addEventListener('resize', function(){{
      if(window.innerWidth > 900) closePanel();
    }});
  }})();
</script>

<script>
  // Rich smooth-scroll engine: eases mouse-wheel scrolling and internal anchor
  // navigation with the same inertia curve. Touch and keyboard scrolling are
  // left fully native. Disabled entirely when the visitor prefers reduced motion.
  (function(){{
    var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if(reduceMotion) return;
    if(!('scrollTo' in window)) return;

    var ease = 0.085;
    var current = window.scrollY || window.pageYOffset || 0;
    var target = current;
    var raf = null;
    var headerEl = document.querySelector('header.site');

    function maxScroll(){{
      return Math.max(0, document.documentElement.scrollHeight - window.innerHeight);
    }}
    function clamp(v){{
      return Math.min(Math.max(v, 0), maxScroll());
    }}
    function setScroll(y){{
      // behavior:'instant' forces an immediate jump for this call. 'auto' is NOT
      // the same thing -- it honors the CSS scroll-behavior on the scrolling box,
      // so with html{{scroll-behavior:smooth}} set, 'auto' would trigger the
      // browser's own native smooth-scroll animation on top of our easing loop.
      window.scrollTo({{top:y, left:0, behavior:'instant'}});
    }}
    function loop(){{
      current += (target - current) * ease;
      if(Math.abs(target - current) < 0.4){{
        current = target;
        setScroll(current);
        raf = null;
        return;
      }}
      setScroll(current);
      raf = requestAnimationFrame(loop);
    }}
    function ensureLoop(){{
      if(raf === null){{ raf = requestAnimationFrame(loop); }}
    }}

    window.addEventListener('wheel', function(e){{
      if(e.ctrlKey) return; // let pinch-zoom / ctrl+wheel pass through untouched
      var delta = e.deltaY;
      if(e.deltaMode === 1) delta *= 18;       // line mode
      else if(e.deltaMode === 2) delta *= window.innerHeight; // page mode
      e.preventDefault();
      target = clamp(target + delta);
      ensureLoop();
    }}, {{passive:false}});

    // Stay in sync with native scrolling (touch, keyboard, scrollbar drag).
    var syncTimer = null;
    window.addEventListener('scroll', function(){{
      if(raf !== null) return;
      clearTimeout(syncTimer);
      syncTimer = setTimeout(function(){{
        target = window.scrollY;
        current = target;
      }}, 60);
    }}, {{passive:true}});

    window.addEventListener('resize', function(){{
      target = clamp(target);
    }});

    document.querySelectorAll('a[href^="#"]').forEach(function(a){{
      a.addEventListener('click', function(e){{
        var id = a.getAttribute('href');
        if(!id || id.length < 2) return;
        var el = document.querySelector(id);
        if(!el) return;
        e.preventDefault();
        var offset = headerEl ? headerEl.offsetHeight : 0;
        var rectTop = el.getBoundingClientRect().top + window.scrollY;
        current = window.scrollY;
        target = clamp(rectTop - offset - 12);
        ensureLoop();
        if(history.pushState){{ history.pushState(null, '', id); }}
      }});
    }});
  }})();
</script>
<script>
  // Reveal the "Bestil i dag, spis i morgen" step cards as they scroll into view.
  // Progressive enhancement only: the section stays fully visible in CSS by default,
  // and this script "arms" the hidden/reveal state itself, so nothing depends on JS
  // running for the content to be readable.
  (function(){{
    var rail = document.getElementById('stepsRail');
    if(!rail || !('IntersectionObserver' in window)) return;
    var cards = rail.querySelectorAll('.step-card');
    if(!cards.length) return;
    rail.classList.add('reveal-armed');
    var io = new IntersectionObserver(function(entries){{
      entries.forEach(function(entry){{
        if(entry.isIntersecting){{
          entry.target.classList.add('in-view');
          io.unobserve(entry.target);
        }}
      }});
    }}, {{threshold:0.2, rootMargin:'0px 0px -60px 0px'}});
    cards.forEach(function(c){{ io.observe(c); }});
  }})();
</script>
<script>
  // Reveal the "Ikke en restaurant" intro block (text + photo stack) as it scrolls
  // into view. Same progressive-enhancement pattern as the step cards above.
  (function(){{
    var grid = document.getElementById('aboutGrid');
    if(!grid || !('IntersectionObserver' in window)) return;
    var parts = grid.querySelectorAll('.about-text, .about-visual');
    if(!parts.length) return;
    grid.classList.add('reveal-armed');
    var io = new IntersectionObserver(function(entries){{
      entries.forEach(function(entry){{
        if(entry.isIntersecting){{
          entry.target.classList.add('in-view');
          io.unobserve(entry.target);
        }}
      }});
    }}, {{threshold:0.25, rootMargin:'0px 0px -60px 0px'}});
    parts.forEach(function(p){{ io.observe(p); }});
  }})();
</script>
<script>
  // "Vi er kun en pose væk" ticket: reveal-on-scroll for the two columns,
  // plus a genuinely live status line computed from the real opening hours
  // (Fri+Sat 15–20, Europe/Copenhagen) rather than a static label. If any of
  // this fails (old browser, no Intl support) the static HTML text already
  // in the markup stays exactly as it is — nothing here is load-bearing.
  (function(){{
    var grid = document.getElementById('ctaGrid');
    if(!grid) return;

    if('IntersectionObserver' in window){{
      var parts = grid.querySelectorAll('.cta-text, .cta-ticket-wrap');
      if(parts.length){{
        grid.classList.add('reveal-armed');
        var io = new IntersectionObserver(function(entries){{
          entries.forEach(function(entry){{
            if(entry.isIntersecting){{
              entry.target.classList.add('in-view');
              io.unobserve(entry.target);
            }}
          }});
        }}, {{threshold:0.25, rootMargin:'0px 0px -60px 0px'}});
        parts.forEach(function(p){{ io.observe(p); }});
      }}
    }}

    var dot = document.getElementById('orderDot');
    var kickerText = document.getElementById('orderStatusText');
    var stubStatus = document.getElementById('ticketStatus');
    var dateEl = document.getElementById('ticketDate');

    function fmtMins(total){{
      var d = Math.floor(total / 1440), rem = total % 1440;
      var h = Math.floor(rem / 60), m = rem % 60;
      var parts = [];
      if(d > 0) parts.push(d + 'd');
      if(h > 0 || d > 0) parts.push(h + 't');
      parts.push(m + 'm');
      return parts.join(' ');
    }}

    function setStatus(isOpen, kickerMsg, stubMsg){{
      if(dot) dot.classList.toggle('is-open', isOpen);
      if(kickerText) kickerText.textContent = kickerMsg;
      if(stubStatus){{
        stubStatus.textContent = stubMsg;
        stubStatus.classList.toggle('is-open', isOpen);
      }}
    }}

    function refreshStatus(){{
      try{{
        var fmt = new Intl.DateTimeFormat('en-US', {{
          timeZone:'Europe/Copenhagen', weekday:'short', hour:'2-digit', minute:'2-digit', hour12:false
        }});
        var map = {{}};
        fmt.formatToParts(new Date()).forEach(function(p){{ map[p.type] = p.value; }});
        var weekdayIndex = {{Sun:0, Mon:1, Tue:2, Wed:3, Thu:4, Fri:5, Sat:6}};
        var day = weekdayIndex[map.weekday];
        var hour = parseInt(map.hour, 10) % 24;
        var minute = parseInt(map.minute, 10);
        if(day === undefined || isNaN(hour) || isNaN(minute)) return;

        var t = day * 1440 + hour * 60 + minute;
        var friStart = 5 * 1440 + 900, friEnd = 5 * 1440 + 1200;
        var satStart = 6 * 1440 + 900, satEnd = 6 * 1440 + 1200;
        var WEEK = 10080;

        if(t >= friStart && t < friEnd){{
          setStatus(true, 'Åbent nu · lukker om ' + fmtMins(friEnd - t), 'Åbent til kl. 20 i aften');
          return;
        }}
        if(t >= satStart && t < satEnd){{
          setStatus(true, 'Åbent nu · lukker om ' + fmtMins(satEnd - t), 'Åbent til kl. 20 i aften');
          return;
        }}
        var candidates = [friStart, satStart, friStart + WEEK].filter(function(s){{ return s > t; }});
        var next = Math.min.apply(null, candidates);
        var day2 = (next === satStart) ? 'lørdag' : 'fredag';
        setStatus(false, 'Åbner ' + day2 + ' · om ' + fmtMins(next - t), 'Åbner ' + day2 + ' kl. 15');
      }} catch(e){{ /* static fallback text stays put */ }}
    }}

    function refreshDate(){{
      try{{
        var fmt = new Intl.DateTimeFormat('da-DK', {{
          timeZone:'Europe/Copenhagen', weekday:'long', day:'numeric', month:'short'
        }});
        var str = fmt.format(new Date());
        if(dateEl) dateEl.textContent = str.charAt(0).toUpperCase() + str.slice(1);
      }} catch(e){{ /* static fallback text stays put */ }}
    }}

    refreshStatus();
    refreshDate();
    setInterval(refreshStatus, 60000);
    setInterval(refreshDate, 600000);
  }})();
</script>
<script>
  // Cycles the "Maden er ___" adjective under the reviews. The first word is
  // marked is-active in the HTML, so it reads correctly even if this never runs.
  (function(){{
    var wrap = document.getElementById('wordSwap');
    if(!wrap) return;
    var items = Array.prototype.slice.call(wrap.querySelectorAll('.word-swap-item'));
    if(items.length < 2) return;
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if(reduce) return;
    var current = 0;
    setInterval(function(){{
      var prevEl = items[current];
      var next = (current + 1) % items.length;
      prevEl.classList.remove('is-active');
      prevEl.classList.add('is-exiting');
      items[next].classList.add('is-active');
      setTimeout(function(){{ prevEl.classList.remove('is-exiting'); }}, 600);
      current = next;
    }}, 2200);
  }})();
</script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(HTML)

print("wrote", len(HTML), "bytes")
