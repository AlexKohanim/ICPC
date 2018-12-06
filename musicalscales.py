#!/usr/bin/env python3
notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#" ]
scales = dict()
steps = [2,2,1,2,2,2,1]

for i, n in enumerate(notes):
    notes_len = len(notes)
    start = i
    scale_notes = {n}
    for s in steps:
        start += s
        scale_notes.add(notes[start % notes_len])
    scales[n] = scale_notes
#print (scales)

input()
s = set(input().split())
found = False
proper_scales = set()
for k, v in scales.items():
    if s.issubset(v):
        proper_scales.add(k)
        found = True
if not found:
    print("none")
else:
    {print(item, end=" ") for item in sorted(proper_scales)}
    print()