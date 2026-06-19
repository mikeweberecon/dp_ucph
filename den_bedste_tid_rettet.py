#!/usr/bin/env python3
"""Corrected 'Den bedste tid' (One Two) chord chart - fully in G major.

Fix: the second half of each verse, both bridges, and verse 3 were left in the
original Bb key in the source PDF. They are transposed down a minor third to G
(Bb->G, Gm->Em, F->D, Eb->C, Cm->Am) so the whole song is consistently in G.
Chord horizontal positions are kept identical to the source, so the timing of
each chord change is preserved.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

PAGE_W, PAGE_H = A4
M = 18 * mm
RED = HexColor("#8B0000")      # section headers (0x8B0000)
BLUE = HexColor("#1F4E79")     # chords (0x1F4E79)
BLACK = HexColor("#000000")
GREY = HexColor("#555555")

c = canvas.Canvas("Den_bedste_tid_G_rettet.pdf", pagesize=A4)
y = PAGE_H - M
CH = 4.6 * mm  # line height

def nl(h=CH):
    global y
    y -= h

def need():
    global y
    if y < M + CH:
        c.showPage(); y = PAGE_H - M

# content is a list of tuples (kind, text)
# kinds: title, sub, header, chord, lyric, riff, blank, note
def draw(kind, text=""):
    global y
    need()
    if kind == "title":
        c.setFont("Helvetica-Bold", 16); c.setFillColor(BLACK)
        c.drawString(M, y, text); nl(7*mm)
    elif kind == "sub":
        c.setFont("Courier", 9); c.setFillColor(BLACK)
        c.drawString(M, y, text); nl(7*mm)
    elif kind == "header":
        c.setFont("Helvetica-Bold", 10); c.setFillColor(RED)
        c.drawString(M, y, text); nl()
    elif kind == "chord":
        c.setFont("Courier-Bold", 9); c.setFillColor(BLUE)
        c.drawString(M, y, text); nl()
    elif kind in ("lyric", "riff"):
        c.setFont("Courier", 9); c.setFillColor(BLACK)
        c.drawString(M, y, text); nl()
    elif kind == "note":
        c.setFont("Helvetica-Oblique", 8.5); c.setFillColor(GREY)
        c.drawString(M, y, text); nl()
    elif kind == "blank":
        nl(text or CH)

# C = chord line, L = lyric line, H = header, B = blank
song = [
    ("title", "DEN BEDSTE TID — One Two"),
    ("sub",   "G-dur · 4/4 · transponeret en lille terts ned fra original (Bb)."),

    ("header", "[Intro]"),
    ("chord", "| Gsus2 · Em · | Am7 · Gsus4 · |"),
    ("blank", 3*mm),

    ("header", "[Vers 1]"),
    ("chord", "G            Em"),
    ("lyric", "Mærker disse tider"),
    ("chord", "Am7         Gsus4"),
    ("lyric", "Mærker mer' og mer'"),
    ("chord", "G                   Em"),
    ("lyric", "At du har givet mig lysten til"),
    ("chord", "Am7     Gsus4 G"),
    ("lyric", "At være den, jeg er"),
    ("blank", 2.5*mm),
    ("chord", "G               Em"),            # was Bb / Gm
    ("lyric", "Dengang jeg var alene"),
    ("chord", "D                       C"),     # was F / Eb
    ("lyric", "Var det så svært at se, hva' der sku' til"),
    ("chord", "G                        Em"),   # was Bb / Gm
    ("lyric", "Nu det' klart, at når jeg ser på dig"),
    ("chord", "D"),                             # was F
    ("lyric", "Og hører, hva' du si'r, og mærker det, du gi'r"),
    ("blank", 3*mm),

    ("header", "[Bro]"),
    ("chord", "Am                        Em"),  # was Cm / Gm
    ("lyric", "Du ved det nok ikke selv, nej-nej"),
    ("chord", "Am                                              D"),  # was Cm / D
    ("lyric", "Du er det, som gør, at jeg for dig bli'r he-elt speciel"),
    ("blank", 3*mm),

    ("header", "[Omkvæd]"),
    ("chord", "G                 Am7        D"),
    ("lyric", "Den bedste tid er sammen med dig"),
    ("chord", "Em        C"),
    ("lyric", "Lykkelig, fordi—"),
    ("chord", "D                       G"),
    ("lyric", "Jeg ved, når vi er hver for sig—"),
    ("chord", "Am7"),
    ("lyric", "Er du med inden i"),
    ("chord", "D                     C       C/B"),
    ("lyric", "Ja, den bedste tid er den, vi har"),
    ("chord", "Am7                  D"),
    ("lyric", "For alt det gi'r sig selv"),
    ("chord", "G"),
    ("lyric", "Uh-yeah, å-åh"),
    ("blank", 3*mm),

    ("header", "[Vers 2]"),
    ("chord", "G                Em"),
    ("lyric", "Langt inde i mit hjerte, åh-uh"),
    ("chord", "Am7                Gsus4"),
    ("lyric", "Der plantede du et træ"),
    ("chord", "G               Em"),
    ("lyric", "Så rigtig og så inderligt"),
    ("chord", "Am7            Gsus4 G"),
    ("lyric", "Der vokser det hver dag"),
    ("blank", 2.5*mm),
    ("chord", "G               Em"),            # was Bb / Gm
    ("lyric", "Engang var svære tider"),
    ("chord", "D                          C"),  # was F / Eb
    ("lyric", "Brændte vennerne af, havde ikke noget at sige"),
    ("chord", "G                          Em"), # was Bb / Gm
    ("lyric", "Men 'det så let, nu når jeg ser på dig"),
    ("chord", "D"),                             # was F
    ("lyric", "Og hører, hvad du si'r, og mærker det, du gi'r, åh-ja"),
    ("blank", 3*mm),

    ("header", "[Bro]"),
    ("chord", "Am               Em"),           # was Cm / Gm
    ("lyric", "Du ved nok ikk', min ven"),
    ("chord", "Am                                 D"),   # was Cm / D
    ("lyric", "At du er den som gør, de andre kan holde mig ud igen"),
    ("blank", 3*mm),

    ("header", "[Omkvæd]"),
    ("chord", "G                 Am7        D"),
    ("lyric", "Den bedste tid er sammen med dig"),
    ("chord", "Em        C"),
    ("lyric", "Lykkelig, fordi—"),
    ("chord", "D                       G"),
    ("lyric", "Jeg ved, når vi er hver for sig—"),
    ("chord", "Am7"),
    ("lyric", "Er du med inden i"),
    ("chord", "D                     C       C/B"),
    ("lyric", "Ja, den bedste tid er den, vi har"),
    ("chord", "Am7                  D"),
    ("lyric", "For alt det gi'r sig selv"),
    ("chord", "G"),
    ("lyric", "Uh-yeah, å-åh"),
    ("blank", 3*mm),

    ("header", "[Solo MIKE  (keyboard-solo ×2)]"),
    ("chord", "| G · Em · | Am7 · G/C · |   | G · Em · | Am7 · G/C · |"),
    ("blank", 2*mm),
    ("header", "[Solo JAMES  (guitar-solo)]"),
    ("chord", "| G · Em · | D · C · |   | G · Em · | D · · · |"),
    ("blank", 3*mm),

    ("header", "[Vers 3]"),
    ("chord", "C"),                             # was Eb
    ("lyric", "Mmh, ved du måske selv, na-na-na-nej"),
    ("chord", "Em"),                            # was Gm
    ("lyric", "At du' min bedste ven? Åh-ja-ha"),
    ("chord", "Am                     Em             Am"),  # was Cm / Gm / Cm
    ("lyric", "Åh, du ved måske ikk', at det, som du åbner i mig"),
    ("chord", "Em                                                D"),  # was Gm / D
    ("lyric", "At det er det, som gør, at jeg for dig bli'r helt speciel, uh, åh"),
    ("blank", 3*mm),

    ("header", "[Break]"),
    ("chord", "| D · · · | D · · · |"),
    ("blank", 3*mm),

    ("header", "[Modulation → A-dur · Omkvæd ×3]"),
    ("chord", "A                 Bm7        E"),
    ("lyric", "Den bedste tid er sammen med dig"),
    ("chord", "F#m       D"),
    ("lyric", "Lykkelig, fordi—"),
    ("chord", "E                       A"),
    ("lyric", "Jeg ved, når vi er hver for sig—"),
    ("chord", "Bm7"),
    ("lyric", "Er du med inden i"),
    ("chord", "E                     D       D/C#"),
    ("lyric", "Ja, den bedste tid er den, vi har"),
    ("chord", "Bm7                  E"),
    ("lyric", "For alt det gi'r sig selv"),
    ("chord", "A"),
    ("lyric", "Uh-yeah, ye-yeah, det' det, det gør"),
    ("note", "(gentag omkvædet i A-dur ×3 – sidste gang kan slutte på A)"),
]

for kind, *rest in song:
    draw(kind, rest[0] if rest else "")

c.showPage()
c.save()
print("wrote Den_bedste_tid_G_rettet.pdf")
