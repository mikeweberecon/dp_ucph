#!/usr/bin/env python3
"""Engrave the suggested keyboard-solo line for 'Den bedste tid', in Bb major.

This is the solo line composed to fit the progression (Bbsus2/4 - Gm - Cm7 - Bb/Eb),
the Bb transposition of the line previously given in G. Two bars, played x2.
"""
from music21 import stream, note, meter, key, clef, metadata, bar, expressions

p = stream.Part()

def mk(num, notes):
    """num: measure number, notes: list of (name, quarterLength)"""
    m = stream.Measure(number=num)
    for name, ql in notes:
        m.append(note.Note(name, quarterLength=ql))
    return m

# Bar 1: Bb (beats 1-2) / Gm (beats 3-4)
m1 = mk(1, [('B-4',1),('D5',0.5),('F5',0.5),('G5',1),('F5',0.5),('D5',0.5)])
# clef / key / time live at the head of measure 1
m1.insert(0.0, clef.TrebleClef())
m1.insert(0.0, key.Key('B-'))      # Bb major (2 flats)
m1.insert(0.0, meter.TimeSignature('4/4'))
# Bar 2: Cm7 (beats 1-2) / Bb/Eb (beats 3-4)
m2 = mk(2, [('E-5',1),('G5',0.5),('B-5',0.5),('F5',1),('D5',0.5),('B-4',0.5)])

# chord names as plain text (ASCII 'b' for flat -> always renders)
def chord(txt):
    te = expressions.TextExpression(txt)
    te.placement = 'above'
    te.style.fontWeight = 'bold'
    return te

m1.insert(0.0, chord('Bb'))
m1.insert(2.0, chord('Gm'))
m2.insert(0.0, chord('Cm7'))
m2.insert(2.0, chord('Bb/Eb'))

# repeat the two bars (x2)
m1.leftBarline = bar.Repeat(direction='start')
m2.rightBarline = bar.Repeat(direction='end', times=2)

p.append(m1)
p.append(m2)

sc = stream.Score()
sc.metadata = metadata.Metadata()
sc.metadata.title = 'Den bedste tid - Keyboard-solo (Bb)'
sc.metadata.composer = 'One Two  -  forslag til solo-linje, transponeret G til Bb  -  spil x2'
sc.insert(0, p)

sc.write('musicxml', fp='/tmp/solo_bb.musicxml')
print('musicxml written')
