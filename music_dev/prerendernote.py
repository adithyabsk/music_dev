from abjad import *
import PyQt5
line = abjad.Staff()
score = abjad.Score()
score.append(line)
for i in range(1):
        line.append(abjad.Measure((4,4),[]))
line[0].extend("c''1")
score.add_final_bar_line()
allnotes = []
for measure in line:
        for note in measure:
                allnotes.append(note)
tweak(allnotes[0].note_head).color = 'yellow'
to_write = abjad.LilyPondFile.new(score)
writefile = open('frames/notepossibleframes/ground.ly','w')
writefile.write(format(to_write))
writefile.close()
for i in range(len(allnotes)):
        if(i < len(allnotes)-1):
                tweak(allnotes[i+1].note_head).color = 'yellow'
        tweak(allnotes[i].note_head).color = 'red'
        to_write = abjad.LilyPondFile.new(score)
        writefile = open('frames/notepossibleframes/' + str(i) + 'wrong.ly','w')
        writefile.write(format(to_write))
        writefile.close()
        tweak(allnotes[i].note_head).color = 'green'
        to_write = abjad.LilyPondFile.new(score)
        writefile = open('frames/notepossibleframes/' + str(i) + 'right.ly','w')
        writefile.write(format(to_write))
        writefile.close()
        tweak(allnotes[i].note_head).color = 'black'
