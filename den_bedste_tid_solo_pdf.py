#!/usr/bin/env python3
import verovio
from svglib.svglib import svg2rlg
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.graphics import renderPDF

# 1) staff only (no verovio header/footer); we add our own titles
tk = verovio.toolkit()
tk.setOptions({
    'pageWidth': 1800, 'pageHeight': 600, 'scale': 60,
    'adjustPageHeight': True, 'header': 'none', 'footer': 'none',
    'pageMarginLeft': 40, 'pageMarginRight': 40, 'pageMarginTop': 20,
})
assert tk.loadFile('/tmp/solo_bb.musicxml')
open('/tmp/solo_staff.svg', 'w').write(tk.renderToSVG(1))
draw = svg2rlg('/tmp/solo_staff.svg')

PAGE_W, PAGE_H = A4
M = 18 * mm
c = canvas.Canvas('/home/user/dp_ucph/Den_bedste_tid_keyboardsolo_Bb.pdf', pagesize=A4)

# Title block
c.setFillColor(HexColor('#000000'))
c.setFont('Helvetica-Bold', 17)
c.drawString(M, PAGE_H - M, 'Den bedste tid — Keyboard-solo (Bb)')
c.setFont('Helvetica', 10.5)
c.setFillColor(HexColor('#555555'))
c.drawString(M, PAGE_H - M - 7*mm,
             'One Two · forslag til solo-linje · transponeret G → Bb · spil ×2')

# Scale the staff drawing to the printable width and place it under the title
avail_w = PAGE_W - 2*M
scale = min(1.0, avail_w / draw.width)
draw.scale(scale, scale)
draw.width *= scale
draw.height *= scale
top_y = PAGE_H - M - 16*mm
renderPDF.draw(draw, c, M, top_y - draw.height)

# Footnote with chord tones / how to use it
y = top_y - draw.height - 12*mm
c.setFont('Helvetica-Bold', 10); c.setFillColor(HexColor('#1F4E79'))
c.drawString(M, y, 'Akkorder (Bb-dur):')
c.setFont('Helvetica', 10); c.setFillColor(HexColor('#000000'))
for line in [
    'Bb = Bb D F     Gm = G Bb D     Cm7 = C Eb G Bb     Bb/Eb = Bb D F over Eb-bas',
    '',
    'Improvisér over hele loopet med Bb-dur pentatonisk: Bb  C  D  F  G',
    '(tilføj Eb over Cm7, og A som ledetone tilbage til Bb).',
    '',
    'Bemærk: dette er en foreslået solo-linje der passer til akkorderne — ikke en',
    'transskription af den indspillede solo (kildens nodeblad kunne ikke aflæses).',
]:
    y -= 5.4*mm
    if line.startswith('Bemærk') or line.startswith('(kilde'):
        c.setFillColor(HexColor('#555555')); c.setFont('Helvetica-Oblique', 9)
    elif line.startswith('transsk'):
        c.setFillColor(HexColor('#555555')); c.setFont('Helvetica-Oblique', 9)
    else:
        c.setFillColor(HexColor('#000000')); c.setFont('Helvetica', 10)
    c.drawString(M, y, line)

c.showPage(); c.save()
print('saved final PDF')
