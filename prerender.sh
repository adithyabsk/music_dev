python prerendermary.py
cd marypossibleframes
lilypond -fpng *.ly
cd ..
python prerenderphrase.py
cd phrasepossibleframes
lilypond -fpng *.ly
cd ..
python prerendernote.py
cd notepossibleframes
lilypond -fpng *.ly
cd ..
