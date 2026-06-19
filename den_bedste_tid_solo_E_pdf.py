#!/usr/bin/env python3
import verovio
from svglib.svglib import svg2rlg
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.graphics import renderPDF

tk = verovio.toolkit()
tk.setOptions({'pageWidth':1700,'pageHeight':1100,'scale':46,'adjustPageHeight':True,
               'header':'none','footer':'none','pageMarginLeft':30,'pageMarginRight':30,
               'pageMarginTop':20})
assert tk.loadFile('/home/user/dp_ucph/Den_bedste_tid_keyboardsolo_E.musicxml')
open('/tmp/soloE.svg','w').write(tk.renderToSVG(1))
draw = svg2rlg('/tmp/soloE.svg')

PAGE_W, PAGE_H = A4
M = 16 * mm
c = canvas.Canvas('/home/user/dp_ucph/Den_bedste_tid_keyboardsolo_E.pdf', pagesize=A4)

c.setFillColor(HexColor('#000000')); c.setFont('Helvetica-Bold', 16)
c.drawString(M, PAGE_H - M, 'Den bedste tid — Keyboard solo (E-dur)')
c.setFont('Helvetica', 10.5); c.setFillColor(HexColor('#555555'))
c.drawString(M, PAGE_H - M - 6.5*mm,
             'One Two · bar 37–44 · transponeret G → E (lille terts ned) · "Slide with the pitch bender"')

avail_w = PAGE_W - 2*M
scale = min(1.0, avail_w / draw.width)
draw.scale(scale, scale); draw.width *= scale; draw.height *= scale
top_y = PAGE_H - M - 14*mm
renderPDF.draw(draw, c, M, top_y - draw.height)

y = top_y - draw.height - 10*mm
lines = [
    ('h', 'Transponering (lille terts ned, G-dur → E-dur, 4 kryds F# C# G# D#):'),
    ('n', 'G→E   A→F#   B→G#   C→A   D→B   E→C#   F#→D#     (akkorder: Esus2/4 · F#m7 · E/G#)'),
    ('s', ''),
    ('h', 'Bemærk:'),
    ('i', '• Bar 41–44 er noteret 8va (en oktav op) i originalen — her skrevet i klingende toneleje.'),
    ('i', '• Skråstregerne i originalen = pitch-bender slides (scoop/fald); ikke gengivet som node-glyffer her.'),
    ('w', '• BEDST-MULIGE AFLÆSNING fra et lavopløst billede: kontur, rytme, triol og 8va er fanget, men de'),
    ('w', '  tætte takter (dobbeltgreb i 37–38/41–42 og de hurtige 16-dele i 40) kan have unøjagtige toner.'),
    ('w', '  Tjek mod originalen — rettelser kan laves nemt i den vedlagte MusicXML-fil.'),
]
for kind, txt in lines:
    y -= 5.4*mm
    if kind=='h': c.setFont('Helvetica-Bold',10); c.setFillColor(HexColor('#1F4E79'))
    elif kind=='n': c.setFont('Courier',9.5); c.setFillColor(HexColor('#000000'))
    elif kind=='i': c.setFont('Helvetica',9.5); c.setFillColor(HexColor('#000000'))
    elif kind=='w': c.setFont('Helvetica-Oblique',9.5); c.setFillColor(HexColor('#8B0000'))
    else: continue
    c.drawString(M, y, txt)

c.showPage(); c.save(); print('final E PDF saved')
