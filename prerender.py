from abjad import *
import PyQt5
def rightnote():
        print("WAS THE NOTE RIGHT?")
        return int(input())
line = abjad.Staff()
for i in range(8):
        line.append(abjad.Measure((4,4),[]))
line[0].extend("e''4 d''4 c''4 d''4")
line[1].extend("e''4 e''4 e''2")
line[2].extend("d''4 d''4 d''2")
line[3].extend("e''4 g''4 g''2")
line[4].extend("e''4 d''4 c''4 d''4")
line[5].extend("e''4 e''4 e''4 e''4")
line[6].extend("d''4 d''4 e''4 d''4")
line[7].extend("c''1")
allnotes = []
for measure in line:
        for note in measure:
                allnotes.append(note)
for i in range(len(allnotes)):
        tweak(allnotes[i].note_head).color = 'red'
        to_write = abjad.LilyPondFile.new(line)
        writefile = open('possibleframes/' + str(i) + 'wrong.ly','w')
        writefile.write(format(to_write))
        writefile.close()
        tweak(allnotes[i].note_head).color = 'green'
        to_write = abjad.LilyPondFile.new(line)
        writefile = open('possibleframes/' + str(i) + 'right.ly','w')
        writefile.write(format(to_write))
        writefile.close()
        tweak(allnotes[i].note_head).color = 'black'
writefile = open('possibleframes/data.txt')
writefile.write(str(len(allnotes)))
