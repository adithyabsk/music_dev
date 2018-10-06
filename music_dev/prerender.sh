python prerendermary.py
cd frames/marypossibleframes
lilypond -fpng *.ly
cd ../..
python prerenderphrase.py
cd frames/phrasepossibleframes
lilypond -fpng *.ly
cd ../..
python prerendernote.py
cd frames/notepossibleframes
lilypond -fpng *.ly
cd ../..
