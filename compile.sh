if [ $2 == "yesbib" ]; then
    biber $1
fi
pdflatex $1.tex
if [ $2 == "yesbib" ]; then
    biber $1
    pdflatex $1.tex
    biber $1
else
    echo "Nessun file bibliografico da compilare"
fi
pdflatex $1.tex
