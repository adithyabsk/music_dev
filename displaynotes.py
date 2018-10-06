from abjad import *
score = abjad.Score()
staff = abjad.StaffGroup([], lilypond_type = 'PianoStaff')
line = abjad.Staff()
staff.append(line)
score.append(staff)
for i in range(2):
        line.append(abjad.Measure((4,4),[]))
line[0].extend("e'4 d'4 c'4 d'4")
line[1].extend("e'4 e'4 e'2")
show(score)
