#!/usr/bin/env python3
"""Static site generator for Luxe Cleaning Co.

Purpose: renders every HTML page of the marketing site from shared templates
and the content defined below, so header/footer/nav stay consistent.

Usage:  python3 build.py        (run from anywhere; writes next to this file)

Safety profile: writes only *.html files inside this directory. No network
access, no secrets, idempotent (re-running overwrites with identical output).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EMAIL = "Luxecleaningcoltd@gmail.com"
BRAND = "Luxe Cleaning Co"

CITIES = ["London", "Birmingham", "Manchester", "Leeds", "Liverpool",
          "Sheffield", "Bristol", "Newcastle"]

SERVICES = [
    dict(slug="domestic-cleaning", name="Domestic Cleaning", icon="✦",
         short="Regular, reliable home cleaning tailored to your routine.",
         intro="A beautifully kept home, without lifting a finger. Our regular domestic cleaning keeps every room fresh, polished and welcoming — weekly, fortnightly or monthly, on a schedule that suits you.",
         includes=["Dusting of all surfaces, frames and ornaments", "Vacuuming and mopping of all floors", "Kitchen worktops, hob, sink and exterior of appliances", "Bathroom, shower, toilet and tiles descaled and shined", "Bedrooms tidied and beds made on request", "Mirrors, glass and handles polished", "Bins emptied and fresh finish throughout"],
         ideal="Busy professionals, families and anyone who wants to come home to a spotless space."),
    dict(slug="deep-cleaning", name="Deep Cleaning", icon="✧",
         short="A meticulous top-to-bottom clean for the details others miss.",
         intro="Our deep clean goes well beyond the everyday. We work room by room, reaching the places that routine cleaning leaves behind, to reset your home or workspace to a true fresh start.",
         includes=["Skirting boards, door frames and light switches", "Inside kitchen cupboards and drawers (on request)", "Behind and underneath movable furniture and appliances", "Limescale and grime removal in bathrooms", "Detailed cleaning of tiles and grout", "Window sills, tracks and internal glass", "Thorough floor and edge cleaning"],
         ideal="Spring cleans, seasonal refreshes, new-year resets or homes that haven't had a professional clean in a while."),
    dict(slug="end-of-tenancy-cleaning", name="End of Tenancy Cleaning", icon="❖",
         short="Move out with confidence and give your deposit its best chance.",
         intro="Moving out is stressful enough. Our end of tenancy service is carried out to the standard agents and landlords expect, working through a detailed checklist so nothing is overlooked.",
         includes=["Full kitchen deep clean including oven, hob and extractor", "Inside fridge, freezer and cupboards", "Bathrooms descaled, sanitised and polished", "All floors cleaned; carpet cleaning available", "Internal windows, sills and frames", "Doors, skirting boards, switches and radiators", "Checklist walkthrough on request"],
         ideal="Tenants, landlords and letting agents preparing a property for inspection or the next occupant."),
    dict(slug="office-commercial-cleaning", name="Office & Commercial Cleaning", icon="◆",
         short="Professional, discreet cleaning for workplaces and commercial spaces.",
         intro="First impressions matter. We keep offices, studios, clinics and retail spaces immaculate, with flexible schedules that fit around your team — early mornings, evenings or weekends.",
         includes=["Desks, workstations and shared surfaces sanitised", "Reception and meeting rooms presented to a high standard", "Kitchenettes and break rooms", "Washrooms cleaned and restocked", "Floors vacuumed, mopped and maintained", "Waste and recycling removal", "Bespoke contracts and flexible hours"],
         ideal="Offices, clinics, salons, showrooms, co-working spaces and small to mid-size businesses."),
    dict(slug="carpet-upholstery-cleaning", name="Carpet & Upholstery Cleaning", icon="❂",
         short="Deep extraction to revive carpets, sofas and soft furnishings.",
         intro="Fibres hold on to dirt, allergens and odours. Our hot-water extraction process lifts them out, brightening colours and extending the life of your carpets, rugs and upholstery.",
         includes=["Pre-inspection and spot treatment of stains", "Deep hot-water extraction for carpets and rugs", "Sofas, armchairs and fabric dining chairs", "Mattress refresh on request", "Odour removal and freshening", "Fast drying times", "Safe for families and pets"],
         ideal="Homes with children or pets, rental properties and offices with high foot traffic."),
    dict(slug="post-construction-cleaning", name="Post-Construction Cleaning", icon="⬥",
         short="Dust, debris and residue cleared so the finished result shines.",
         intro="After the builders leave, the real finishing begins. We remove fine dust, paint splashes, adhesive and debris so your renovated space is ready to enjoy or hand over.",
         includes=["Removal of builders' dust from every surface", "Paint, plaster and adhesive residue removal", "Window, frame and glazing clean", "Fixtures, fittings and appliances polished", "Floors cleaned and protected", "Cupboards and shelving wiped inside and out", "Final detail walkthrough"],
         ideal="Homeowners, developers, contractors and property managers completing a refurbishment or new build."),
    dict(slug="window-cleaning", name="Window Cleaning", icon="◇",
         short="Streak-free glass that lets the light in.",
         intro="Clear windows transform a space. We clean glass, frames and sills for a crisp, streak-free finish that brightens every room.",
         includes=["Interior and exterior glass", "Frames, sills and tracks", "Conservatory and patio doors", "Skylights where safely accessible", "Regular or one-off visits", "Residential and commercial"],
         ideal="Homes, shops, offices and conservatories, as a standalone service or an add-on."),
    dict(slug="oven-appliance-cleaning", name="Oven & Appliance Cleaning", icon="✺",
         short="Baked-on grease removed and appliances restored.",
         intro="Ovens, hobs and extractors build up stubborn grease. We strip it away safely, so your appliances look and perform like new.",
         includes=["Oven interior, racks, trays and door glass", "Hob and extractor hood degreased", "Microwave and fridge interiors", "Washing machine and dishwasher refresh", "Food-safe, low-odour products"],
         ideal="Home cooks, landlords, and anyone preparing for a move or a special occasion."),
    dict(slug="holiday-let-airbnb-cleaning", name="Holiday Let & Airbnb Cleaning", icon="❋",
         short="Fast, hotel-standard turnovers between guests.",
         intro="Five-star reviews start with a spotless arrival. We handle changeovers promptly and to hotel-level standards, so your guests always walk into a pristine home.",
         includes=["Full clean between guest stays", "Linen change and bed making", "Restocking of toiletries and essentials", "Kitchen, bathroom and living areas reset", "Damage and missing-item reporting", "Flexible same-day scheduling"],
         ideal="Holiday let owners, Airbnb hosts and short-let property managers."),
]

FAQS = [
    ("What areas do you cover?", "We serve " + ", ".join(CITIES[:-1]) + " and " + CITIES[-1] + ". If you're nearby but not listed, get in touch and we'll let you know what we can do."),
    ("How do I get a quote?", "Send us an enquiry through the contact form or email " + EMAIL + " with a few details about your property and the service you need. We'll come back to you with a clear, no-obligation quote."),
    ("Do I need to be at home during the clean?", "No. Many clients provide access instructions or a key arrangement. We're happy to work whichever way you prefer."),
    ("Do you bring your own equipment and products?", "Yes. We arrive fully equipped with professional-grade equipment and quality products. If you prefer particular products, just let us know."),
    ("Can I book a regular clean?", "Of course. Domestic and commercial clients can book weekly, fortnightly or monthly visits, or choose a one-off clean."),
    ("Are your cleaners trained and trusted?", "Our team is carefully selected and trained to a consistent, high standard. We take pride in being reliable, discreet and respectful of your space."),
    ("What if I'm not happy with the result?", "Your satisfaction matters. If anything isn't right, tell us within 48 hours and we'll work with you to put it right."),
    ("Do you offer end of tenancy cleaning?", "Yes. We follow a detailed checklist designed to meet the expectations of letting agents and landlords."),
]

NAV = [("Home", "index.html"), ("About", "about.html"), ("Services", "services.html"),
       ("Areas", "areas.html"), ("FAQ", "faq.html"), ("Contact", "contact.html")]


def photo(base, name, cls="", label=""):
    """Photo slot: shows assets/photos/<name>.jpg; falls back to a navy panel if the file is absent."""
    if not (ROOT / "assets" / "photos" / f"{name}.jpg").exists():
        return ""
    bg = f"url({base}assets/photos/{name}.jpg) center 22%/cover no-repeat, linear-gradient(150deg,#13296b,#0a1b45)"
    cap = f'<span class="cap">{label}</span>' if label else ""
    return f'<div class="photo {cls}" role="img" aria-label="{label}" style="background:{bg}">{cap}</div>'


def hero_bg(base, name):
    return 'style="background:linear-gradient(160deg,#0a1b45,#13296b)"'


def head(title, desc, base):
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0a1b45">
<link rel="icon" href="{base}assets/logo-mark.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/style.css">
</head>
<body>
"""


def header(base, active):
    items = []
    for label, href in NAV:
        cls = ' class="active"' if label == active else ""
        if label == "Services":
            subs = "".join(f'<a href="{base}services/{s["slug"]}.html">{s["name"]}</a>' for s in SERVICES)
            items.append(f'<li class="has-sub"><a href="{base}{href}"{cls}>Services</a><div class="sub">{subs}</div></li>')
        elif label == "Contact":
            continue
        else:
            items.append(f'<li><a href="{base}{href}"{cls}>{label}</a></li>')
    items.append(f'<li><a class="btn btn-gold" href="{base}contact.html">Get a Quote</a></li>')
    return f"""<div class="topbar">Premium cleaning across the UK's major cities · <a href="mailto:{EMAIL}">{EMAIL}</a></div>
<header class="site"><div class="wrap nav">
<a class="brand" href="{base}index.html" aria-label="{BRAND} home"><img src="{base}assets/logo-mark.png" alt=""><span class="brand-text"><b>LUXE</b><small>CLEANING CO</small></span></a>
<button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
<nav class="main" aria-label="Main"><ul>{''.join(items)}</ul></nav>
</div></header>
<main>
"""


def footer(base):
    svc = "".join(f'<li><a href="{base}services/{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES[:6])
    cit = "".join(f'<li><a href="{base}areas.html">{c}</a></li>' for c in CITIES)
    return f"""</main>
<footer class="site"><div class="wrap">
<div class="foot">
<div><a class="brand" href="{base}index.html"><img src="{base}assets/logo-mark.png" alt=""><span class="brand-text"><b>LUXE</b><small>CLEANING CO</small></span></a>
<p style="margin-top:18px;max-width:34ch">Premium cleaning for homes and businesses. Immaculate results, delivered with care.</p>
<p style="margin-top:14px"><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<div><h4>Services</h4><ul>{svc}<li><a href="{base}services.html">View all →</a></li></ul></div>
<div><h4>Cities</h4><ul>{cit}</ul></div>
<div><h4>Company</h4><ul><li><a href="{base}about.html">About us</a></li><li><a href="{base}faq.html">FAQ</a></li><li><a href="{base}contact.html">Contact</a></li><li><a href="{base}privacy.html">Privacy policy</a></li></ul></div>
</div>
<div class="legal"><span>© 2026 {BRAND} Ltd. All rights reserved.</span><span>Enquiries: <a href="mailto:{EMAIL}">{EMAIL}</a></span></div>
</div></footer>
<script src="{base}assets/main.js"></script>
</body></html>
"""


def page_hero(title, sub, crumbs, base="", img="hero"):
    return f"""<section class="page-hero" {hero_bg(base, img)}><div class="wrap">
<div class="crumbs">{crumbs}</div>
<h1>{title}</h1><p>{sub}</p></div></section>
"""


def cta(base, text="Request your free, no-obligation quote today."):
    return f"""<section class="cta" {hero_bg(base, "cta")}><div class="wrap rv">
<div class="eyebrow" style="justify-content:center;color:var(--gold-light)">Ready when you are</div>
<h2>Experience the Luxe difference</h2><p>{text}</p>
<a class="btn btn-gold" href="{base}contact.html">Get a Quote</a></div></section>
"""


def service_cards(base, items):
    out = ""
    for s in items:
        out += f"""<a class="card rv" href="{base}services/{s['slug']}.html"><div class="ico">{s['icon']}</div>
<h3>{s['name']}</h3><p>{s['short']}</p><span class="more">Learn more</span></a>
"""
    return out


def form(base, service=""):
    opts = "".join(f'<option{" selected" if s["name"] == service else ""}>{s["name"]}</option>' for s in SERVICES)
    cit = "".join(f"<option>{c}</option>" for c in CITIES)
    return f"""<form class="panel" data-enquiry>
<input type="hidden" name="_subject" value="New website enquiry — {BRAND}">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_captcha" value="false">
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="row"><div class="field"><label for="n">Full name</label><input id="n" name="Name" required autocomplete="name"></div>
<div class="field"><label for="e">Email</label><input id="e" type="email" name="email" required autocomplete="email"></div></div>
<div class="row"><div class="field"><label for="p">Phone</label><input id="p" type="tel" name="Phone" autocomplete="tel"></div>
<div class="field"><label for="c">City</label><select id="c" name="City" required><option value="">Select your city</option>{cit}<option>Other</option></select></div></div>
<div class="field"><label for="s">Service required</label><select id="s" name="Service" required><option value="">Select a service</option>{opts}</select></div>
<div class="field"><label for="m">How can we help?</label><textarea id="m" name="Message" required placeholder="Tell us about your property, preferred dates and any special requests."></textarea></div>
<button class="btn btn-gold" type="submit">Send Enquiry</button>
<div class="form-msg" role="status" aria-live="polite"></div>
</form>"""


def write(path, html):
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


def build():
    b = ""
    # ---------- Home ----------
    why = [("01", "Meticulous attention to detail", "Every skirting board, tap and mirror receives the care it deserves."),
           ("02", "Trusted, trained team", "Courteous, discreet cleaners who respect your home and your time."),
           ("03", "Tailored to you", "Flexible schedules and bespoke checklists built around your needs."),
           ("04", "Satisfaction promised", "If something isn't perfect, we'll make it right.")]
    why_html = "".join(f'<div class="card rv"><div class="num">{n}</div><h3>{t}</h3><p>{d}</p></div>' for n, t, d in why)
    steps = [("Enquire", "Tell us what you need through our quick form or by email."),
             ("Quote", "Receive a clear, tailored quote with no hidden extras."),
             ("Book", "Choose a date and time that works for you."),
             ("Enjoy", "Return to a flawless space and relax.")]
    steps_html = "".join(f'<div class="card rv"><div class="ico">{i+1}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))
    cities_html = "".join(f'<a class="city" href="areas.html">{c}</a>' for c in CITIES)
    gal = photo(b, "kitchen", "", "Kitchens") + photo(b, "bathroom", "", "Bathrooms") + photo(b, "living", "", "Living spaces")
    gallery = f'<section style="padding-top:0"><div class="wrap"><div class="grid g3 gallery rv">{gal}</div></div></section>' if gal.count("class=\"photo") == 3 else ""
    tm = "".join(photo(b, f"team{i}", "tall") for i in range(1, 5))
    team = (f'<section style="background:var(--white);border-block:1px solid var(--line)"><div class="wrap"><div class="sec-head center rv"><div class="eyebrow">Our team</div><h2>Trained, uniformed and trusted</h2>'
            f'<p class="lead">Courteous professionals who treat your space as their own.</p></div><div class="grid g4 rv">{tm}</div></div></section>') if tm.count('class="photo') == 4 else ""
    home = head(f"{BRAND} | Premium Cleaning Services in the UK's Major Cities",
                "Luxe Cleaning Co delivers premium domestic, deep, end of tenancy and commercial cleaning across the UK's major cities. Request a quote today.", b)
    home += header(b, "Home")
    home += f"""<section class="hero"><div class="wrap hero-grid">
<div><div class="eyebrow">Premium cleaning, impeccably done</div>
<h1>Where every space <em>shines</em></h1>
<p class="lead">Luxe Cleaning Co brings a refined, meticulous standard of cleaning to homes and businesses across the UK's major cities. Spotless results, elegant service.</p>
<div class="hero-cta"><a class="btn btn-gold" href="contact.html">Get a Free Quote</a><a class="btn btn-line" href="services.html">Explore Services</a></div>
<div class="trust"><div><i>✦</i> Fully equipped</div><div><i>✦</i> Flexible scheduling</div><div><i>✦</i> Satisfaction promised</div></div></div>
<div class="logo-card"><img src="assets/logo-full.png" alt="Luxe Cleaning Co"></div>
</div></section>
<section><div class="wrap"><div class="sec-head center rv"><div class="eyebrow">Our services</div><h2>Cleaning crafted to perfection</h2>
<p class="lead">From everyday home care to specialist commercial cleans, discover a service designed around you.</p></div>
<div class="grid g3">{service_cards(b, SERVICES[:6])}</div>
<div class="center rv" style="margin-top:44px"><a class="btn btn-line" href="services.html">View all services</a></div></div></section>
{gallery}
<section class="dark"><div class="wrap split">
<div class="rv"><div class="eyebrow">Why Luxe</div><h2>The standard your space deserves</h2>
<p class="lead" style="margin-top:18px">We believe cleaning is a craft. Our approach blends professional technique with a genuinely personal service.</p>
<ul class="checks"><li>Professional-grade equipment and quality products</li><li>Detailed checklists so nothing is missed</li><li>Clear, honest quotes with no hidden extras</li><li>One-off or regular visits, domestic or commercial</li></ul>
<a class="btn btn-light" style="margin-top:34px" href="about.html">About us</a></div>
<div class="grid g2">{why_html}</div></div></section>
{team}
<section><div class="wrap"><div class="sec-head center rv"><div class="eyebrow">How it works</div><h2>Effortless from start to finish</h2></div>
<div class="grid g4">{steps_html}</div></div></section>
<section style="background:var(--white);border-block:1px solid var(--line)"><div class="wrap center rv"><div class="eyebrow">Where we work</div><h2>Serving the major cities</h2>
<p class="lead" style="margin:16px auto 40px">Premium cleaning in the UK's largest cities.</p><div class="cities">{cities_html}</div></div></section>
{cta(b)}"""
    home += footer(b)
    write("index.html", home)

    # ---------- About ----------
    p = head(f"About Us | {BRAND}", "Learn about Luxe Cleaning Co: our values, our approach and our commitment to premium cleaning.", b)
    p += header(b, "About") + page_hero("About Luxe Cleaning Co", "Premium cleaning with a personal touch.", '<a href="index.html">Home</a> / About', b, "about")
    vals = [("Excellence", "We hold ourselves to a high, consistent standard on every visit."),
            ("Integrity", "Honest quotes, reliable timekeeping and respect for your property."),
            ("Care", "We treat your space as we would our own, with discretion and courtesy."),
            ("Detail", "The finishing touches are what set a great clean apart.")]
    vh = "".join(f'<div class="card rv"><div class="ico">✦</div><h3>{t}</h3><p>{d}</p></div>' for t, d in vals)
    p += f"""<section><div class="wrap split"><div class="rv"><div class="eyebrow">Our story</div><h2>Cleaning, elevated</h2>
<p style="margin-top:20px;color:var(--muted)">Luxe Cleaning Co was created with a simple belief: a clean space should feel like a luxury. We combine professional methods with an eye for detail and a warm, dependable service to deliver results our clients are proud of.</p>
<p style="margin-top:16px;color:var(--muted)">Whether it's a family home, a city apartment, a rental property or a busy office, we tailor every clean to the space and the person behind it. Our team arrives fully equipped, works carefully and leaves things immaculate.</p>
<ul class="checks"><li>Homes and businesses in the UK's major cities</li><li>Regular, one-off and bespoke cleaning</li><li>Quality products and professional equipment</li></ul></div>
<div class="rv">{photo(b, "about", "tall", "Our team at work") or '<div class="logo-card"><img src="assets/logo-full.png" alt="Luxe Cleaning Co"></div>'}</div></div></section>
<section class="dark"><div class="wrap"><div class="sec-head center rv"><div class="eyebrow">Our values</div><h2>What we stand for</h2></div><div class="grid g4">{vh}</div></div></section>
{cta(b)}"""
    p += footer(b)
    write("about.html", p)

    # ---------- Services index ----------
    p = head(f"Cleaning Services | {BRAND}", "Explore Luxe Cleaning Co's full range of services: domestic, deep, end of tenancy, commercial, carpet, post-construction, windows, ovens and holiday lets.", b)
    p += header(b, "Services") + page_hero("Our Services", "A complete range of premium cleaning for homes and businesses.", '<a href="index.html">Home</a> / Services')
    p += f'<section><div class="wrap"><div class="grid g3">{service_cards(b, SERVICES)}</div></div></section>' + cta(b) + footer(b)
    write("services.html", p)

    # ---------- Service pages ----------
    sb = "../"
    for s in SERVICES:
        others = [o for o in SERVICES if o is not s][:3]
        inc = "".join(f"<li>{i}</li>" for i in s["includes"])
        p = head(f"{s['name']} | {BRAND}", s["short"] + " Serving the UK's major cities.", sb)
        p += header(sb, "Services") + page_hero(s["name"], s["short"], f'<a href="{sb}index.html">Home</a> / <a href="{sb}services.html">Services</a> / {s["name"]}', sb, s["slug"])
        p += f"""<section><div class="wrap split" style="align-items:start"><div class="rv">{photo(sb, s['slug'], "wide")}<div class="eyebrow" style="margin-top:36px">The service</div><h2>{s['name']}</h2>
<p style="margin-top:18px;color:var(--muted)">{s['intro']}</p>
<h3 style="margin-top:34px">What's included</h3><ul class="checks">{inc}</ul>
<h3 style="margin-top:34px">Ideal for</h3><p style="color:var(--muted);margin-top:8px">{s['ideal']}</p>
<p style="margin-top:22px;color:var(--muted)">Available in {', '.join(CITIES[:-1])} and {CITIES[-1]}.</p></div>
<div class="rv"><h3 style="margin-bottom:18px">Request a quote</h3>{form(sb, s['name'])}</div></div></section>
<section class="dark"><div class="wrap"><div class="sec-head center rv"><div class="eyebrow">Also from Luxe</div><h2>Other services</h2></div>
<div class="grid g3">{service_cards(sb, others)}</div></div></section>"""
        p += footer(sb)
        write(f"services/{s['slug']}.html", p)

    # ---------- Areas ----------
    p = head(f"Areas We Cover | {BRAND}", "Luxe Cleaning Co provides premium cleaning in London, Birmingham, Manchester, Leeds, Liverpool, Sheffield, Bristol and Newcastle.", b)
    p += header(b, "Areas") + page_hero("Areas We Cover", "Premium cleaning across the UK's major cities.", '<a href="index.html">Home</a> / Areas')
    cards = "".join(f'<div class="card rv"><div class="ico">✦</div><h3>{c}</h3><p>Domestic, deep, end of tenancy and commercial cleaning in {c}.</p><a class="more" href="contact.html">Request a quote</a></div>' for c in CITIES)
    p += f"""<section><div class="wrap"><div class="sec-head center rv"><div class="eyebrow">Our cities</div><h2>Find us near you</h2>
<p class="lead">Don't see your city? Get in touch, we may still be able to help.</p></div><div class="grid g4">{cards}</div></div></section>""" + cta(b) + footer(b)
    write("areas.html", p)

    # ---------- FAQ ----------
    p = head(f"FAQ | {BRAND}", "Answers to common questions about Luxe Cleaning Co's services, quotes, booking and coverage.", b)
    p += header(b, "FAQ") + page_hero("Frequently Asked Questions", "Everything you need to know before you book.", '<a href="index.html">Home</a> / FAQ')
    fq = "".join(f"<details class='rv'><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQS)
    p += f'<section><div class="wrap" style="max-width:820px">{fq}</div></section>' + cta(b, "Still have a question? We'd love to hear from you.") + footer(b)
    write("faq.html", p)

    # ---------- Contact ----------
    p = head(f"Contact & Get a Quote | {BRAND}", "Request a free quote from Luxe Cleaning Co. Send us your enquiry and we'll be in touch shortly.", b)
    p += header(b, "Contact") + page_hero("Get in Touch", "Request your free, no-obligation quote.", '<a href="index.html">Home</a> / Contact')
    p += f"""<section><div class="wrap contact-grid"><div class="rv"><div class="eyebrow">Contact</div><h2>Let's make your space shine</h2>
<p style="margin:18px 0 34px;color:var(--muted)">Send us a few details and we'll reply with a tailored quote.</p>
<div class="info-item"><h3>Email</h3><a href="mailto:{EMAIL}">{EMAIL}</a></div>
<div class="info-item"><h3>Cities</h3><p>{', '.join(CITIES)}</p></div>
<div class="info-item"><h3>Response</h3><p>We aim to reply to every enquiry promptly.</p></div></div>
<div class="rv">{form(b)}</div></div></section>""" + footer(b)
    write("contact.html", p)

    # ---------- Privacy ----------
    p = head(f"Privacy Policy | {BRAND}", "How Luxe Cleaning Co collects and uses your enquiry information.", b)
    p += header(b, "") + page_hero("Privacy Policy", "How we handle your information.", '<a href="index.html">Home</a> / Privacy')
    p += f"""<section><div class="wrap" style="max-width:780px;color:var(--muted)">
<h3 style="color:var(--navy)">What we collect</h3><p style="margin:8px 0 24px">When you submit an enquiry we collect the details you provide: your name, email, phone number, city, service required and message.</p>
<h3 style="color:var(--navy)">How we use it</h3><p style="margin:8px 0 24px">We use this information only to respond to your enquiry, provide a quote and deliver our services. We do not sell your data.</p>
<h3 style="color:var(--navy)">Third-party processing</h3><p style="margin:8px 0 24px">Enquiry forms are delivered to our mailbox through a form-relay service (FormSubmit). Fonts are loaded from Google Fonts.</p>
<h3 style="color:var(--navy)">Your rights</h3><p style="margin:8px 0 24px">You may ask us to access, correct or delete your information at any time by emailing <a href="mailto:{EMAIL}"><u>{EMAIL}</u></a>.</p></div></section>""" + footer(b)
    write("privacy.html", p)


if __name__ == "__main__":
    build()
    print("Built site in", ROOT)
