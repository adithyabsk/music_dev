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
                \tweak color #black
                d''4
                \tweak color #black
                c''4
                \tweak color #black
                d''4
            }   % measure
            {   % measure
                \tweak color #black
                e''4
                \tweak color #black
                e''4
                \tweak color #black
                e''2
            }   % measure
            {   % measure
                \tweak color #black
                d''4
                \tweak color #black
                d''4
                \tweak color #black
                d''2
            }   % measure
            {   % measure
                \tweak color #black
                e''4
                \tweak color #black
                g''4
                \tweak color #black
                g''2
            }   % measure
            {   % measure
                \tweak color #black
                e''4
                \tweak color #black
                d''4
                \tweak color #black
                c''4
                \tweak color #red
                d''4
            }   % measure
            {   % measure
                \tweak color #yellow
                e''4
                e''4
                e''4
                e''4
            }   % measure
            {   % measure
                d''4
                d''4
                e''4
                d''4
            }   % measure
            {   % measure
                c''1
                \bar "|." %! SCORE1
            }   % measure
        }
    >>
}