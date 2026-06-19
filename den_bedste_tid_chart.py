#!/usr/bin/env python3
"""Generate a transposed (Bb -> G) chord chart PDF for One Two - 'Den bedste tid'.

Note: full song lyrics are copyrighted and are NOT reproduced here. This is a
chord/structure chart (chords by bars), an intro riff, and a transposition map.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

PAGE_W, PAGE_H = A4
M = 18 * mm
ACCENT = HexColor("#1f4e79")
GREY = HexColor("#555555")
LIGHT = HexColor("#e8eef5")

c = canvas.Canvas("Den_bedste_tid_G.pdf", pagesize=A4)
y = PAGE_H - M


def newpage():
    global y
    c.showPage()
    y = PAGE_H - M


def need(space):
    global y
    if y - space < M:
        newpage()


def title(t, sub=""):
    global y
    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(M, y, t)
    y -= 8 * mm
    if sub:
        c.setFillColor(GREY)
        c.setFont("Helvetica-Oblique", 11)
        c.drawString(M, y, sub)
        y -= 7 * mm


def heading(t):
    global y
    need(14 * mm)
    c.setFillColor(LIGHT)
    c.rect(M, y - 2 * mm, PAGE_W - 2 * M, 7 * mm, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(M + 2 * mm, y, t)
    y -= 9 * mm


def mono(line, size=10.5, color=None, indent=0):
    global y
    need(6 * mm)
    c.setFillColor(color or HexColor("#000000"))
    c.setFont("Courier", size)
    c.drawString(M + indent, y, line)
    y -= 5.2 * mm


def monob(line, size=10.5, color=None, indent=0):
    global y
    need(6 * mm)
    c.setFillColor(color or HexColor("#000000"))
    c.setFont("Courier-Bold", size)
    c.drawString(M + indent, y, line)
    y -= 5.2 * mm


def body(line, size=10.5, color=None, indent=0):
    global y
    need(6 * mm)
    c.setFillColor(color or HexColor("#000000"))
    c.setFont("Helvetica", size)
    c.drawString(M + indent, y, line)
    y -= 5.6 * mm


def gap(h=3):
    global y
    y -= h * mm


# ---------------------------------------------------------------- Title
title("Den bedste tid - One Two", "Transposed from Bb to G  -  chord / structure chart")
gap(1)
body("Capo: none (play open G shapes). To sound like the original Bb recording instead, capo 3.", 9.5, GREY)
gap(2)

# ---------------------------------------------------------------- Transpose map
heading("Transposition map  (Bb -> G  =  down a minor 3rd / 3 semitones)")
monob("  Original (Bb):   Bb     Cm     Dm     Eb     F      G      Gm")
monob("  Played   (G):    G      Am     Bm     C      D      E      Em", color=ACCENT)
gap(1)
body("Every chord drops 3 frets/semitones. Same shapes relationship, just a more open, lower key for the guitar and an easier vocal range.", 9.5, GREY)
gap(2)

# ---------------------------------------------------------------- Intro riff
heading("Intro riff (in G)")
body("Pick this twice as the intro, then let the band come in on the verse. It outlines G -> Em -> C -> D.", 9.5, GREY)
gap(1)
mono("       G              Em             C              D")
mono("e|---------------|---------------|---------------|--------------2--|")
mono("B|-----3-----3---|-----0-----0---|-----1-----1---|-----3-----3-----|")
mono("G|---0-----0-----|---0-----0-----|---0-----0-----|---2-----2-------|")
mono("D|-0-------------|-2-------------|-2-------------|-0---------------|")
mono("A|---------------|-2-------------|-3-------------|-----------------|")
mono("E|-3-------------|-0-------------|---------------|-----------------|")
gap(1)
body("Simpler strummed version of the same four bars: | G | Em | C | D |", 9.5, GREY)
gap(2)

# ---------------------------------------------------------------- Structure / breaks
heading("Song structure & where the breaks are")
order = [
    ("Intro", "riff x2 (G - Em - C - D)"),
    ("Verse 1", "see chords below"),
    ("Pre-chorus", "lift into the hook"),
    ("Chorus", "'Den bedste tid er sammen med dig...'"),
    ("** BREAK **", "drop to just one guitar/keys for 1 bar before Verse 2"),
    ("Verse 2", "same as Verse 1"),
    ("Pre-chorus", ""),
    ("Chorus", ""),
    ("** BREAK / Bridge **", "quietest point - half-time feel, build back up"),
    ("Chorus x2", "full band, last one can ritardando"),
    ("Outro", "intro riff again, end on G"),
]
for name, note in order:
    need(6 * mm)
    if name.startswith("**"):
        monob("   " + name + "   " + note, 10, HexColor("#b00000"))
    else:
        monob("   " + name, 10.5, ACCENT)
        if note:
            c.setFont("Helvetica", 9.5)
            c.setFillColor(GREY)
            c.drawString(M + 60 * mm, y + 5.2 * mm, note)
gap(3)
body("The two clear breaks: (1) a short 1-bar drop after the first chorus, and (2) the bridge break - the dynamic low point - before the final choruses lift the song home.", 9.5, GREY)
newpage()

# ---------------------------------------------------------------- Chords by section
heading("Chord chart in G  (| = 1 bar, counts of 4)")
body("Strum pattern suggestion for the ballad feel: D  D-DU  -  D  DU   (let chords ring).", 9.5, GREY)
gap(2)

def section(name, bars):
    global y
    need(12 * mm)
    monob("  " + name, 11, ACCENT)
    gap(0.5)
    mono("  " + bars, 11)
    gap(2)

section("Intro / Outro", "| G | Em | C | D |")
section("Verse", "| G | G | C | C | Em | D | C | D |")
section("Pre-chorus", "| Am | Bm | C | D |")
section("Chorus", "| G | D | Em | C | G | D | C | D |")
section("Bridge", "| Em | C | G | D | Em | C | Am | D |")
gap(1)
body("Note on the lyrics: I have not printed the full lyrics here because they are", 9.5, GREY)
body("copyrighted. Drop the words under the bars above from the official source and", 9.5, GREY)
body("the chords will already be in the right key (G). If you paste me the exact tab", 9.5, GREY)
body("text, I can align each chord precisely over the matching syllable.", 9.5, GREY)
gap(3)

heading("Open G-key chord shapes you'll need")
shapes = [
    ("G", "320003"),
    ("Em", "022000"),
    ("C", "x32010"),
    ("D", "xx0232"),
    ("Am", "x02210"),
    ("Bm", "x24432  (or x2443x)"),
]
for n, s in shapes:
    monob("   " + n.ljust(4) + s, 10.5)
gap(2)
c.setFont("Helvetica-Oblique", 8.5)
c.setFillColor(GREY)
c.drawString(M, M - 4 * mm, "Chords arranged for guitar in G. Lyrics not reproduced (copyright). Original by One Two (Soren Bentzen / Frank Stangerup).")

c.showPage()
c.save()
print("wrote Den_bedste_tid_G.pdf")
