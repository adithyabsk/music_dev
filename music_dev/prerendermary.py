from abjad import *
import PyQt5
line = abjad.Staff()
score = abjad.Score()
score.append(line)
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
score.add_final_bar_line()
allnotes = []
for measure in line:
        for note in measure:
                allnotes.append(note)
tweak(allnotes[0].note_head).color = 'yellow'
to_write = abjad.LilyPondFile.new(score)
writefile = open('frames/marypossibleframes/ground.ly','w')
writefile.write(format(to_write))
writefile.close()
for i in range(len(allnotes)):
        if(i < len(allnotes)-1):
                tweak(allnotes[i+1].note_head).color = 'yellow'
        tweak(allnotes[i].note_head).color = 'red'
        to_write = abjad.LilyPondFile.new(score)
        writefile = open('frames/marypossibleframes/' + str(i) + 'wrong.ly','w')
        writefile.write(format(to_write))
        writefile.close()
        tweak(allnotes[i].note_head).color = 'green'
        to_write = abjad.LilyPondFile.new(score)
        writefile = open('frames/marypossibleframes/' + str(i) + 'right.ly','w')
        writefile.write(format(to_write))
        writefile.close()
        tweak(allnotes[i].note_head).color = 'black'
