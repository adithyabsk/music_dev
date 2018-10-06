\version "2.18.2"
\language "english"

\header {
    tagline = ##f
}

\layout {}

\paper {}

\score {
    \new Score
    <<
        \new Staff
        {
            {   % measure
                \time 4/4
                \tweak color #black
                e''4
                \tweak color #red
                g''4
                \tweak color #yellow
                g''2
                \bar "|." %! SCORE1
            }   % measure
        }
    >>
}