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
if [ $3 == "yesrecompile" ]; then
    ./compile.sh $1 $2
else
    echo "nessuna ricompilazione"
fi