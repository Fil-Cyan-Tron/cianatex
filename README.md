# cianatex
Il mio preambolo per LaTeX, richiede TexLive 2024 perchè è basato su alcuni pacchetti molto fichi e moderni come [quiver](https://q.uiver.app/) (quindi se usate Linux con una distro basata su Debian come me, il comando ```sudo apt-get install texlive-full``` non va bene, in quanto vi carica TexLive 2022)

Per compilare includo il mio super-casalingo script ```compile.sh``` che va semplicemente chiamato nel terminale come ```./compile.sh FILENAME``` e compila i file ```FILENAME.tex``` e ```FILENAME.bib``` un paio di volte per sopprimere gli errori.