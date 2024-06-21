pdflatex $1.tex
if [ $2 == "yesbib" ]; then
    biber $1
    pdflatex $1.tex
else
    echo "Nessun file bibliografico da compilare"
fi
pdflatex $1.tex
rm $1.aux
rm $1.bcf
rm $1.log
rm $1.out
rm $1.run.xml
if [ $2 == "yesbib" ]; then
    rm $1.bbl
    rm $1.blg
else
    echo "nessun file bibliografico da rimuovere"
fi