from abjad import *
def rightnote():
        print("WAS THE NOTE RIGHT?")
        return int(input())
line = abjad.Staff()
for i in range(2):
        line.append(abjad.Measure((4,4),[]))
line[0].extend("e''4 d''4 c''4 d''4")
line[1].extend("e''4 e''4 e''2")
allnotes = []
for measure in line:
        for note in measure:
                allnotes.append(note)
for i in range(len(allnotes)):
        while(not rightnote()):
                tweak(allnotes[i].note_head).color = 'red'
                show(line)
        tweak(allnotes[i].note_head).color = 'green'
        show(line)
        tweak(allnotes[i].note_head).color = 'black'
