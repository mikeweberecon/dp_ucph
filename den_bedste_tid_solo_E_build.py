#!/usr/bin/env python3
"""Best-effort transcription of the 'Den bedste tid' keyboard solo (bars 37-44),
transposed from the source key G major DOWN A MINOR THIRD to E major.

The source is a low-resolution image; dense bars (dyads, pitch-bender slides,
fast 16th runs) are an approximate reading. Contour, rhythm, the triplet and the
8va are captured. Verify against the original; MusicXML is provided to correct.
"""
from fractions import Fraction as F
from music21 import (stream, note, chord, meter, key, clef, metadata, bar,
                     interval, tie, articulations, expressions, spanner)

p = stream.Part()

def N(name, ql, st=False):
    n = note.Note(name, quarterLength=ql)
    if st: n.articulations.append(articulations.Staccato())
    return n
def CH(names, ql):
    return chord.Chord(list(names), quarterLength=ql)
def R(ql):
    return note.Rest(quarterLength=ql)

def measure(num, elems, head=False):
    m = stream.Measure(number=num)
    if head:
        m.insert(0.0, clef.TrebleClef()); m.insert(0.0, key.Key('G'))
        m.insert(0.0, meter.TimeSignature('4/4'))
    for e in elems: m.append(e)
    return m

# ---- written pitches read from the source (G major). Bars 41-44 are written
#      8va in the original (sound an octave higher) -> encoded +1 octave here. ----
c37 = CH(['B4','D5'],1); h37 = CH(['A4','C5'],2); h37.tie = tie.Tie('start')
m37 = measure(37, [R(1), c37, h37], head=True)

h38 = CH(['A4','C5'],1); h38.tie = tie.Tie('stop')
m38 = measure(38, [h38, CH(['B4','D5'],0.5), CH(['A4','C5'],0.5),
                   N('B4',0.5), N('A4',0.5), N('C5',0.5), N('A4',0.5)])

m39 = measure(39, [R(1), R(0.5), N('A4',0.5), N('A4',1),
                   N('A4',0.25), N('B-4',0.25), N('A4',0.25), N('F4',0.25, st=True)])

m40 = measure(40, [N('C5',0.25), N('B4',0.25), N('A4',0.25), N('G4',0.25),
                   N('F4',0.5, st=True), N('E4',0.5, st=True),
                   R(0.5), N('D#4',0.25), N('E4',0.25),
                   N('G4',0.25), N('A4',0.25), N('G4',0.25), N('F4',0.25)])

# bars 41-44: +1 octave for the 8va
c41 = CH(['B5','D6'],1); c41.tie = tie.Tie('start')
m41 = measure(41, [N('G5',0.5, st=True), R(0.5), N('D6',0.5), R(0.5),
                   N('D6',0.5), R(0.5), c41])

c42 = CH(['B5','D6'],1); c42.tie = tie.Tie('stop')
m42 = measure(42, [c42, CH(['B5','D6'],0.5), N('A5',0.5),
                   N('C6',0.5), N('D6',0.5), N('C6',0.5, st=True), R(0.5)])

trip = [N('D6',F(1,3)), N('E6',F(1,3)), N('D6',F(1,3))]
m43 = measure(43, [R(0.5), N('E6',0.5), N('E6',2)] + trip)

m44 = measure(44, [N('E6',0.5), N('F6',0.5), N('D6',0.5), N('E6',0.5),
                   N('D6',0.5), N('E6',0.5), N('D6',0.5), N('E6',0.5)])
m44.rightBarline = bar.Barline('final')

# chord symbols (transposed down a minor 3rd), one per bar as in the original
def chordtext(txt):
    te = expressions.TextExpression(txt); te.placement='above'
    te.style.fontWeight='bold'; return te
for m, lab in [(m37,'Esus2/4'),(m38,'–/c#'),(m39,'F#m7'),(m40,'E/G#'),
               (m41,'Esus2/4'),(m42,'–/c#'),(m43,'F#m7'),(m44,'E/G#')]:
    m.insert(0.0, chordtext(lab))

for m in [m37,m38,m39,m40,m41,m42,m43,m44]:
    p.append(m)

# ---- transpose DOWN a minor third (G -> E), diatonically (correct E-major spelling) ----
down_m3 = interval.Interval(noteStart=note.Note('G4'), noteEnd=note.Note('E4'))
pe = p.transpose(down_m3)

sc = stream.Score()
sc.metadata = metadata.Metadata()
sc.metadata.title = 'Den bedste tid - Keyboard solo (E-dur)'
sc.metadata.composer = 'One Two - transponeret G til E (lille terts ned)'
sc.insert(0, pe)
sc.write('musicxml', fp='/home/user/dp_ucph/Den_bedste_tid_keyboardsolo_E.musicxml')
print('musicxml written')
