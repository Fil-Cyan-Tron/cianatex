# cianatex
Il mio preambolo per LaTeX, richiede TexLive 2024 perchè è basato su alcuni pacchetti molto fichi e moderni come [quiver](https://q.uiver.app/) (quindi se usate Linux con una distro basata su Debian come me, il comando ```sudo apt-get install texlive-full``` non va bene, in quanto vi carica TexLive 2022)

## Compilazione assistita

Per compilare includo il mio super-casalingo script ```compile.sh``` che va semplicemente chiamato nel terminale come ```./compile.sh FILENAME BIB``` e compila i file ```FILENAME.tex``` e se ```BIB == yesbib``` allora compila pure ```FILENAME.bib``` un paio di volte per sopprimere gli errori.

### Debugging

Ho incluso anche lo script ```debug.sh``` che va chiamato nel terminale come ```./debug.sh FILENAME BIB RECOMPILE``` che rimuove i file di supporto per pulire errori vari e nel caso in cui si abbia ```RECOMPILE == yesrecompile``` chiama ```./compile.sh FILENAME BIB```

## Opzioni

Il pacchetto supporta diverse opzioni per quanto riguarda la palette per gli ambienti, di default usa una palette dai colori accesi ma offre anche le opzioni ```pastel``` per avere dei colori pastello, ```depression``` per avere uniformemente grigio e ```zun``` per avere sempre il colore #c8d6fd.

## Demo

Il file ```categories.tex``` funge da demo per molti comandi, mentre il file ```provacolori.tex``` serve semplicemente per provare le palette.