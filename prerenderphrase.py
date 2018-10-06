from abjad import *
import PyQt5
line = abjad.Staff()
score = abjad.Score()
score.append(line)
for i in range(1):
        line.append(abjad.Measure((4,4),[]))
line[0].extend("e''4 g''4 g''2")
score.add_final_bar_line()
allnotes = []
for measure in line:
        for note in measure:
                allnotes.append(note)
to_write = abjad.LilyPondFile.new(score)
writefile = open('phrasepossibleframes/ground.ly','w')
writefile.write(format(to_write))
writefile.close()
for i in range(len(allnotes)):
        tweak(allnotes[i].note_head).color = 'red'
        to_write = abjad.LilyPondFile.new(score)
        writefile = open('phrasepossibleframes/' + str(i) + 'wrong.ly','w')
        writefile.write(format(to_write))
        writefile.close()
        tweak(allnotes[i].note_head).color = 'green'
        to_write = abjad.LilyPondFile.new(score)
        writefile = open('phrasepossibleframes/' + str(i) + 'right.ly','w')
        writefile.write(format(to_write))
        writefile.close()
        tweak(allnotes[i].note_head).color = 'black'
